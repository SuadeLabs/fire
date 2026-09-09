"""Registers the FIRE mapping-assistant tools against an MCPServer instance."""

from __future__ import annotations

from dataclasses import asdict
from typing import Any

from mcp.server import MCPServer

from . import catalog, search, validation


def register(mcp: MCPServer) -> None:
    @mcp.tool()
    def list_entities() -> list[dict[str, Any]]:
        """List all FIRE entities (top-level schemas) with a short description."""
        return [asdict(entity) for entity in catalog.list_entities()]

    @mcp.tool()
    def search_fields(query: str, limit: int = 10) -> list[dict[str, Any]]:
        """Search FIRE field names, descriptions and enum values for a query string."""
        return [asdict(result) for result in search.search_fields(query, limit=limit)]

    @mcp.tool()
    def get_field(entity: str, field: str) -> dict[str, Any]:
        """Get full detail (type, format, enum, monetary flag, description, doc) for one FIRE field."""
        return asdict(catalog.get_field(entity, field))

    @mcp.tool()
    def validate_record(
        entity: str, record: dict[str, Any], jurisdiction: str | None = None
    ) -> list[dict[str, Any]]:
        """Validate a JSON record against a FIRE entity schema.

        Returns a list of validation issues (empty if the record is valid).
        """
        issues = validation.validate_record(entity, record, jurisdiction=jurisdiction)
        return [asdict(issue) for issue in issues]

    @mcp.tool()
    def suggest_mapping(
        entity: str,
        source_fields: list[str],
        sample_values: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        """Suggest FIRE field mappings for a list of internal/source field names.

        Ranked, non-authoritative candidates -- a starting point for a mapping
        table, not a substitute for review.
        """
        candidates = search.suggest_mapping(
            entity, source_fields, sample_values=sample_values
        )
        return [asdict(candidate) for candidate in candidates]
