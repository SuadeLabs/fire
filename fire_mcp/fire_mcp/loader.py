"""Thin, cached file-IO over the FIRE repo's schemas/extensions/docs/examples.

Every function here takes a bare name (no file extension) and returns parsed
content, or None/raises FileNotFoundError depending on whether the caller can
sensibly expect the file to be missing (extensions and docs are optional;
base schemas and examples are not).
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from . import repo


def _load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


@lru_cache(maxsize=None)
def load_schema(entity: str) -> dict:
    return _load_json(repo.SCHEMAS_DIR / f"{entity}.json")


@lru_cache(maxsize=None)
def load_extension_schema(entity: str) -> dict | None:
    path = repo.EXTENSION_SCHEMAS_DIR / f"{entity}.json"
    if not path.exists():
        return None
    return _load_json(path)


@lru_cache(maxsize=None)
def load_doc(field: str) -> str | None:
    path = repo.DOCS_DIR / f"{field}.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=None)
def load_extension_doc(field: str) -> str | None:
    path = repo.EXTENSION_DOCS_DIR / f"{field}.md"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


@lru_cache(maxsize=None)
def load_example(name: str) -> dict:
    return _load_json(repo.EXAMPLES_DIR / f"{name}.json")


def list_schema_names() -> list[str]:
    # common.json holds shared field definitions referenced via $ref by the
    # other schemas; it isn't itself an entity (no properties/title/records).
    return sorted(p.stem for p in repo.SCHEMAS_DIR.glob("*.json") if p.stem != "common")


def list_extension_names() -> list[str]:
    return sorted(p.stem for p in repo.EXTENSION_SCHEMAS_DIR.glob("*.json"))


def list_example_names() -> list[str]:
    return sorted(p.stem for p in repo.EXAMPLES_DIR.glob("*.json"))
