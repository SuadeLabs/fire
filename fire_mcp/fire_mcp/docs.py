"""Lookup and light parsing of documentation/properties/*.md files."""

from __future__ import annotations

import re
from dataclasses import dataclass

from . import loader

_FRONT_MATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)


@dataclass
class Doc:
    field: str
    excerpt: str
    full: str


def _strip_front_matter(text: str) -> str:
    return _FRONT_MATTER_RE.sub("", text, count=1).strip()


def _first_paragraph(text: str) -> str:
    for paragraph in text.split("\n\n"):
        paragraph = paragraph.strip()
        if not paragraph or paragraph.startswith("#") or set(paragraph) <= {"-"}:
            continue
        return paragraph
    return ""


def load_field_doc(field: str, extension: bool = False) -> Doc | None:
    raw = loader.load_extension_doc(field) if extension else loader.load_doc(field)
    if raw is None and extension:
        raw = loader.load_doc(field)
    if raw is None:
        return None
    body = _strip_front_matter(raw)
    return Doc(field=field, excerpt=_first_paragraph(body), full=body)
