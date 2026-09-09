# fire-mcp

An [MCP](https://modelcontextprotocol.io) server that exposes the FIRE data standard so a data
engineering team's own AI assistant can look up fields, validate draft records, and get mapping
suggestions while mapping an internal data format onto FIRE.

It reads `schemas/`, `extensions/`, `documentation/` and `examples/` directly from this repo
checkout at runtime -- there's no build step and no network access, so pin it to a release tag
(e.g. `git checkout v26.07`) if you want a specific version of the standard.

## Install

From inside a clone of this repo:

```bash
pip install -e fire_mcp/
```

For local development (running the MCP inspector, tests):

```bash
pip install -e "fire_mcp/[dev]"
```

## Run

```bash
fire-mcp
# or
python -m fire_mcp.server
```

This serves over stdio by default. Point an MCP client at it, for example a `mcp.json`/client
config entry like:

```json
{
  "mcpServers": {
    "fire": {
      "command": "fire-mcp",
      "cwd": "/path/to/your/clone/of/fire"
    }
  }
}
```

If the server is installed somewhere other than inside the FIRE checkout you want it to read,
set `FIRE_REPO_ROOT` to point at the clone instead of relying on `cwd`.

## What it exposes

Resources:
- `fire://schemas/{entity}` -- an entity's schema, with all `$ref`s resolved inline
- `fire://properties/{field}` -- the markdown documentation for one field
- `fire://examples/{name}` -- a worked example payload
- `fire://extensions/{entity}` -- an entity's jurisdiction-specific extension fields, if any

Tools:
- `list_entities` -- every FIRE entity with a short description
- `search_fields(query)` -- fuzzy search over field names, descriptions and enum values
- `get_field(entity, field)` -- full detail on one field
- `validate_record(entity, record)` -- validate a JSON record against a FIRE schema
- `suggest_mapping(entity, source_fields)` -- ranked, non-authoritative mapping candidates for a
  list of your own field names
