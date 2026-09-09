"""Registers the fire:// resource URIs against an MCPServer instance."""

from __future__ import annotations

import json

from mcp.server import MCPServer

from . import catalog, docs, loader, refs


def register(mcp: MCPServer) -> None:
    @mcp.resource("fire://schemas/{entity}")
    def schema_resource(entity: str) -> str:
        """The FIRE schema for one entity, with all $refs resolved inline."""
        catalog.ensure_known_entity(entity)
        return json.dumps(
            refs.resolve_entity_schema(entity, with_extension=False), indent=2
        )

    @mcp.resource("fire://extensions/{entity}")
    def extension_resource(entity: str) -> str:
        """The jurisdiction-specific extension fields for one entity, if any."""
        catalog.ensure_known_entity(entity)
        resolved = refs.resolve_extension_only(entity)
        if resolved is None:
            raise ValueError(f"No extension schema exists for entity {entity!r}.")
        return json.dumps(resolved, indent=2)

    @mcp.resource("fire://properties/{field}")
    def property_resource(field: str) -> str:
        """The markdown documentation for one FIRE field."""
        doc = docs.load_field_doc(field)
        if doc is None:
            raise ValueError(f"No documentation found for field {field!r}.")
        return doc.full

    @mcp.resource("fire://examples/{name}")
    def example_resource(name: str) -> str:
        """A worked example FIRE payload, as stored in examples/."""
        try:
            example = loader.load_example(name)
        except FileNotFoundError as exc:
            raise ValueError(f"No example named {name!r}.") from exc
        return json.dumps(example, indent=2)
