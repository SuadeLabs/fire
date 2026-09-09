"""Local resolution of FIRE's `$ref`s.

Every `$ref` in this repo points at
``https://raw.githubusercontent.com/SuadeLabs/fire/<ref>/schemas/<file>.json``,
optionally with a JSON-pointer fragment (a bare key into common.json, a
``#/properties/<name>`` reference into another entity's schema, or an empty
fragment used by extension files to pull in the whole base schema via
``allOf``). There is never more than one hop of indirection and no ``$id`` is
declared anywhere, so a small, purpose-built resolver is enough here -- a
general JSON Schema resolver is not needed.

Two resolution strategies live in this module:

* :func:`build_resolver` hands jsonschema its own lazy resolver (via a
  ``handlers`` callback that reads local files instead of the network) for
  use during validation, where jsonschema's built-in fragment handling should
  do the work.
* :func:`resolve_entity_schema` / :func:`resolve_extension_only` eagerly walk
  a schema and replace every ``$ref`` with its resolved value, producing a
  self-contained schema with no ``$ref`` left -- used for the `fire://schemas`
  resource, `get_field`, and the search index.
"""

from __future__ import annotations

import re
from typing import Any

import jsonschema

from . import loader

_FIRE_URL_RE = re.compile(
    r"^https://raw\.githubusercontent\.com/SuadeLabs/fire/[^/]+/schemas/(?P<file>[\w.]+)\.json$"
)


class RefResolutionError(ValueError):
    pass


def _match_ref_url(url: str) -> str:
    match = _FIRE_URL_RE.match(url)
    if not match:
        raise RefResolutionError(f"Unrecognised FIRE $ref: {url!r}")
    return match.group("file")


# --- Lazy resolution, for jsonschema validation --------------------------


def _remote_handler(uri: str) -> dict:
    """jsonschema RefResolver handler for the https:// scheme.

    jsonschema strips any fragment before calling this (see
    ``RefResolver.resolve_from_url``), so `uri` is always a bare schema URL
    here; jsonschema resolves the fragment itself afterwards via
    ``resolve_fragment``, which already does the right thing for both
    common.json's flat keys and ``#/properties/<name>`` pointers.
    """
    entity = _match_ref_url(uri)
    return loader.load_schema(entity)


def build_resolver(schema: dict) -> jsonschema.RefResolver:
    # TODO: jsonschema.RefResolver is soft-deprecated in favour of the
    # `referencing` library (still works as of 4.25.1, via a back-compat
    # shim, but emits a DeprecationWarning). Revisit once the mcp SDK's
    # jsonschema floor and our own needs make a `referencing.Registry`
    # based rewrite worthwhile.
    return jsonschema.RefResolver(
        base_uri="", referrer=schema, handlers={"https": _remote_handler}
    )


# --- Eager resolution, for presentation/search ----------------------------


def _resolve_pointer(document: Any, fragment: str) -> Any:
    node = document
    for part in (p for p in fragment.split("/") if p):
        node = node[part]
    return node


def _load_ref_target(ref: str) -> Any:
    url, _, fragment = ref.partition("#")
    entity = _match_ref_url(url)
    return _resolve_pointer(loader.load_schema(entity), fragment)


def _inline_resolve(node: Any) -> Any:
    if isinstance(node, dict):
        if "$ref" in node:
            resolved = _inline_resolve(_load_ref_target(node["$ref"]))
            extra = {k: v for k, v in node.items() if k != "$ref"}
            if extra and isinstance(resolved, dict):
                # A handful of extension properties attach a $ref alongside
                # their own "description"/"jurisdictions" -- those sibling
                # keys should win over whatever the referenced fragment says.
                return {**resolved, **extra}
            return resolved
        return {key: _inline_resolve(value) for key, value in node.items()}
    if isinstance(node, list):
        return [_inline_resolve(value) for value in node]
    return node


def resolve_entity_schema(entity: str, with_extension: bool = False) -> dict:
    base = loader.load_schema(entity)
    result: dict[str, Any] = {
        "title": base.get("title"),
        "description": base.get("description"),
        "type": base.get("type", "object"),
        "required": base.get("required", []),
        "properties": _inline_resolve(base.get("properties", {})),
    }
    if with_extension:
        extension = loader.load_extension_schema(entity)
        if extension is not None:
            ext_properties = _inline_resolve(extension.get("properties", {}))
            result["properties"] = {**result["properties"], **ext_properties}
            result["extended"] = True
    return result


def resolve_extension_only(entity: str) -> dict | None:
    extension = loader.load_extension_schema(entity)
    if extension is None:
        return None
    return {
        "title": extension.get("title"),
        "description": extension.get("description"),
        "properties": _inline_resolve(extension.get("properties", {})),
    }
