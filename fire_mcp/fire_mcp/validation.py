"""Validate a record against a FIRE entity schema, without any network access."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import jsonschema
import jsonschema.exceptions

from . import catalog, loader, refs


@dataclass
class ValidationIssue:
    path: str
    message: str
    kind: str
    expected: Any = None
    got: Any = None


def _issue_kind(error: jsonschema.exceptions.ValidationError) -> str:
    if error.validator == "required":
        return "missing_required"
    if error.validator == "type":
        return "type_mismatch"
    if error.validator == "enum":
        return "enum_mismatch"
    return "other"


def _schema_for(entity: str, jurisdiction: str | None) -> dict:
    schema = loader.load_schema(entity)
    if jurisdiction is None:
        return schema
    extension = loader.load_extension_schema(entity)
    if extension is None:
        return schema
    merged_properties = dict(schema.get("properties", {}))
    for name, spec in extension.get("properties", {}).items():
        if jurisdiction in (spec.get("jurisdictions") or []):
            merged_properties[name] = spec
    return {**schema, "properties": merged_properties}


def validate_record(
    entity: str, record: dict, jurisdiction: str | None = None
) -> list[ValidationIssue]:
    catalog.ensure_known_entity(entity)
    schema = _schema_for(entity, jurisdiction)
    resolver = refs.build_resolver(schema)
    validator = jsonschema.Draft7Validator(schema, resolver=resolver)

    issues = []
    for error in validator.iter_errors(record):
        path = "/".join(str(part) for part in error.absolute_path) or "<root>"
        issues.append(
            ValidationIssue(
                path=path,
                message=error.message,
                kind=_issue_kind(error),
                expected=error.validator_value,
                got=error.instance,
            )
        )
    return issues
