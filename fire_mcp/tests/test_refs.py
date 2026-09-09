from __future__ import annotations

import pytest

from fire_mcp import loader, refs


def test_resolves_common_json_leaf_ref():
    resolved = refs.resolve_entity_schema("loan")
    accounting_treatment = resolved["properties"]["accounting_treatment"]
    expected = loader.load_schema("common")["accounting_treatment"]
    assert "$ref" not in accounting_treatment
    assert accounting_treatment["enum"] == expected["enum"]


def test_resolves_cross_entity_property_ref_with_sibling_overrides():
    resolved = refs.resolve_extension_only("collateral")
    orig = resolved["properties"]["orig_valuation_type"]
    base_valuation_type = loader.load_schema("collateral")["properties"][
        "valuation_type"
    ]

    assert "$ref" not in orig
    # Sibling keys on the extension property win over the referenced fragment's own.
    assert orig["description"] == "The value type at origination."
    assert orig["jurisdictions"] == ["US"]
    # Type/enum still come through from the referenced base property.
    assert orig["type"] == base_valuation_type["type"]
    assert orig["enum"] == base_valuation_type["enum"]


def _has_ref(node) -> bool:
    if isinstance(node, dict):
        return "$ref" in node or any(_has_ref(v) for v in node.values())
    if isinstance(node, list):
        return any(_has_ref(v) for v in node)
    return False


def test_extension_composition_merges_base_and_extension_fields():
    resolved = refs.resolve_entity_schema("loan", with_extension=True)
    properties = resolved["properties"]

    assert "accrual_status" in properties  # base-only field
    assert "anchor_tenant" in properties  # US-extension-only field
    assert resolved["extended"] is True
    assert not _has_ref(properties)


def test_unrecognised_ref_raises_without_network(no_network):
    with pytest.raises(refs.RefResolutionError):
        refs._load_ref_target("https://example.com/not-fire/schemas/loan.json#/x")


def test_no_network_access_during_resolution_and_validation(no_network):
    from fire_mcp import validation

    refs.resolve_entity_schema("loan", with_extension=True)
    validation.validate_record("loan", {"id": "x", "date": "2020-01-01T00:00:00Z"})
