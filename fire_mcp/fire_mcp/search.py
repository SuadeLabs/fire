"""Fuzzy search over FIRE fields, for `search_fields` and `suggest_mapping`.

FIRE field names are abbreviated snake_case (`cust_id`, `mtm_dirty`,
`acc_fv_change_before_taxes`), so token-based fuzzy scoring (rapidfuzz) does
much better here than a plain character-diff ratio.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from rapidfuzz import fuzz, process

from . import catalog, loader, refs

_INDEX_CACHE: list[tuple[str, str, dict]] | None = None


def _build_index() -> list[tuple[str, str, dict]]:
    entries = []
    for entity in loader.list_schema_names():
        resolved = refs.resolve_entity_schema(entity, with_extension=True)
        for field_name, spec in resolved.get("properties", {}).items():
            entries.append((entity, field_name, spec))
    return entries


def _get_index() -> list[tuple[str, str, dict]]:
    global _INDEX_CACHE
    if _INDEX_CACHE is None:
        _INDEX_CACHE = _build_index()
    return _INDEX_CACHE


@dataclass
class SearchResult:
    entity: str
    field: str
    score: float
    matched_on: str
    type: str | None
    enum: list[str] | None
    description: str | None


def _candidate_texts(field_name: str, spec: dict) -> list[tuple[str, str]]:
    texts = [("name", field_name)]
    description = spec.get("description")
    if description:
        texts.append(("description", description))
    for value in spec.get("enum") or []:
        texts.append(("enum", value))
    return texts


# A single short enum value can score deceptively high against a longer
# query under plain WRatio (e.g. the enum value "customer" scores higher
# against "customer id" than the field "customer_id" does). Down-weight
# enum/description matches slightly so a genuine field-name match wins ties.
_CHANNEL_WEIGHT = {"name": 1.0, "description": 0.92, "enum": 0.85}


def search_fields(query: str, limit: int = 10) -> list[SearchResult]:
    scored = []
    for entity, field_name, spec in _get_index():
        best_score = 0.0
        best_on = "name"
        for kind, text in _candidate_texts(field_name, spec):
            score = fuzz.WRatio(query, text) * _CHANNEL_WEIGHT[kind]
            if score > best_score:
                best_score, best_on = score, kind
        scored.append((best_score, entity, field_name, spec, best_on))
    scored.sort(key=lambda row: row[0], reverse=True)

    results = []
    for score, entity, field_name, spec, matched_on in scored[:limit]:
        results.append(
            SearchResult(
                entity=entity,
                field=field_name,
                score=round(score, 1),
                matched_on=matched_on,
                type=spec.get("type"),
                enum=spec.get("enum"),
                description=spec.get("description"),
            )
        )
    return results


@dataclass
class MappingCandidate:
    source_field: str
    entity_field: str
    score: float
    reason: str


def suggest_mapping(
    entity: str,
    source_fields: list[str],
    sample_values: dict[str, Any] | None = None,
    limit_per_field: int = 3,
) -> list[MappingCandidate]:
    catalog.ensure_known_entity(entity)
    resolved = refs.resolve_entity_schema(entity, with_extension=True)
    properties = resolved.get("properties", {})
    field_names = list(properties.keys())
    sample_values = sample_values or {}

    results = []
    for source in source_fields:
        matches = process.extract(
            source, field_names, scorer=fuzz.token_set_ratio, limit=limit_per_field
        )
        sample = sample_values.get(source)
        for candidate_name, score, _ in matches:
            enum = properties[candidate_name].get("enum")
            is_enum_match = sample is not None and enum and str(sample) in enum
            adjusted = min(100.0, score + 15) if is_enum_match else score
            results.append(
                MappingCandidate(
                    source_field=source,
                    entity_field=candidate_name,
                    score=round(adjusted, 1),
                    reason="enum value match" if is_enum_match else "name similarity",
                )
            )
    return results
