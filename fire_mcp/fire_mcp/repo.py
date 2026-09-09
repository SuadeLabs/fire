"""Locates the FIRE repo on disk so the rest of the package can read schemas,
extensions, documentation and examples without ever making a network call."""

from __future__ import annotations

import os
from pathlib import Path


def _looks_like_fire_repo(path: Path) -> bool:
    return (path / "schemas").is_dir() and (path / "documentation").is_dir()


def _find_repo_root() -> Path:
    override = os.environ.get("FIRE_REPO_ROOT")
    if override:
        path = Path(override).expanduser().resolve()
        if not _looks_like_fire_repo(path):
            raise RuntimeError(
                f"FIRE_REPO_ROOT={path} does not look like a FIRE repo "
                "(expected schemas/ and documentation/ subdirectories)."
            )
        return path

    here = Path(__file__).resolve()
    for candidate in (here, *here.parents):
        if _looks_like_fire_repo(candidate):
            return candidate

    raise RuntimeError(
        "Could not locate the FIRE repo root. Run fire-mcp from inside a "
        "clone of the FIRE repo, or set the FIRE_REPO_ROOT environment "
        "variable to point at one."
    )


REPO_ROOT = _find_repo_root()
SCHEMAS_DIR = REPO_ROOT / "schemas"
EXTENSION_SCHEMAS_DIR = REPO_ROOT / "extensions" / "schemas"
DOCS_DIR = REPO_ROOT / "documentation" / "properties"
EXTENSION_DOCS_DIR = REPO_ROOT / "extensions" / "documentation" / "properties"
EXAMPLES_DIR = REPO_ROOT / "examples"
