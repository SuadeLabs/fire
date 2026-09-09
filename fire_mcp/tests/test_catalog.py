from __future__ import annotations

import pytest

from fire_mcp import catalog, loader


def test_list_entities_covers_all_schema_files():
    entities = catalog.list_entities()
    names = {entity.name for entity in entities}
    assert names == set(loader.list_schema_names())
    assert all(entity.description for entity in entities)


def test_get_field_returns_expected_detail():
    field = catalog.get_field("loan", "accrued_interest_balance")
    assert field.type == "integer"
    assert field.monetary is True
    assert field.doc_excerpt
    assert "accrued interest" in field.doc_excerpt.lower()


def test_get_field_unknown_entity_raises():
    with pytest.raises(catalog.UnknownEntityError):
        catalog.get_field("not_a_real_entity", "id")


def test_get_field_unknown_field_raises():
    with pytest.raises(catalog.UnknownFieldError):
        catalog.get_field("loan", "not_a_real_field")


def test_get_field_extension_field_carries_jurisdictions():
    field = catalog.get_field("loan", "anchor_tenant")
    assert field.jurisdictions == ["US"]
