"""Entity/field catalog built on top of the eagerly-resolved schemas."""

from __future__ import annotations

from dataclasses import dataclass

from . import docs, loader, refs


class UnknownEntityError(ValueError):
    def __init__(self, entity: str):
        super().__init__(
            f"Unknown FIRE entity: {entity!r}. Use list_entities to see valid names."
        )
        self.entity = entity


class UnknownFieldError(ValueError):
    def __init__(self, entity: str, field_name: str):
        super().__init__(f"Unknown field {field_name!r} on entity {entity!r}.")
        self.entity = entity
        self.field_name = field_name


@dataclass
class Entity:
    name: str
    title: str | None
    description: str | None
    has_extension: bool


@dataclass
class Field:
    name: str
    entity: str
    type: str | None = None
    format: str | None = None
    enum: list[str] | None = None
    monetary: bool = False
    description: str | None = None
    doc_excerpt: str | None = None
    jurisdictions: list[str] | None = None


_KNOWN_ENTITIES = set(loader.list_schema_names())


def ensure_known_entity(entity: str) -> None:
    if entity not in _KNOWN_ENTITIES:
        raise UnknownEntityError(entity)


def list_entities() -> list[Entity]:
    extension_names = set(loader.list_extension_names())
    entities = []
    for name in sorted(_KNOWN_ENTITIES):
        schema = loader.load_schema(name)
        entities.append(
            Entity(
                name=name,
                title=schema.get("title"),
                description=schema.get("description"),
                has_extension=name in extension_names,
            )
        )
    return entities


def _field_from_spec(name: str, entity: str, spec: dict, is_extension: bool) -> Field:
    doc = docs.load_field_doc(name, extension=is_extension)
    return Field(
        name=name,
        entity=entity,
        type=spec.get("type"),
        format=spec.get("format"),
        enum=spec.get("enum"),
        monetary=bool(spec.get("monetary", False)),
        description=spec.get("description"),
        doc_excerpt=doc.excerpt if doc else None,
        jurisdictions=spec.get("jurisdictions"),
    )


def list_fields(entity: str, with_extension: bool = True) -> list[Field]:
    ensure_known_entity(entity)
    resolved = refs.resolve_entity_schema(entity, with_extension=with_extension)
    extension = loader.load_extension_schema(entity) if with_extension else None
    extension_field_names = set(extension.get("properties", {})) if extension else set()
    return [
        _field_from_spec(name, entity, spec, name in extension_field_names)
        for name, spec in resolved.get("properties", {}).items()
    ]


def get_field(entity: str, field_name: str) -> Field:
    ensure_known_entity(entity)
    resolved = refs.resolve_entity_schema(entity, with_extension=True)
    properties = resolved.get("properties", {})
    if field_name not in properties:
        raise UnknownFieldError(entity, field_name)
    extension = loader.load_extension_schema(entity)
    is_extension = bool(extension and field_name in extension.get("properties", {}))
    return _field_from_spec(field_name, entity, properties[field_name], is_extension)
