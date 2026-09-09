from __future__ import annotations

import copy

from fire_mcp import loader, validation

CASES = [
    ("bond_future", "derivative"),
    ("current_account_with_guarantee", "account"),
]


def _records(example_name: str, entity: str) -> list[dict]:
    example = loader.load_example(example_name)
    return example["data"][entity]


def test_examples_validate_cleanly():
    for example_name, entity in CASES:
        for record in _records(example_name, entity):
            issues = validation.validate_record(entity, record)
            assert issues == [], f"{example_name}/{entity}: {issues}"


def test_missing_required_field_detected():
    example_name, entity = CASES[0]
    record = copy.deepcopy(_records(example_name, entity)[0])
    del record["id"]
    issues = validation.validate_record(entity, record)
    assert any(issue.kind == "missing_required" for issue in issues)


def test_wrong_type_detected():
    example_name, entity = CASES[0]
    record = copy.deepcopy(_records(example_name, entity)[0])
    record["notional_amount"] = "not-a-number"
    issues = validation.validate_record(entity, record)
    assert any(issue.kind == "type_mismatch" for issue in issues)


def test_bad_enum_detected():
    example_name, entity = CASES[0]
    record = copy.deepcopy(_records(example_name, entity)[0])
    record["asset_class"] = "not_a_real_asset_class"
    issues = validation.validate_record(entity, record)
    assert any(issue.kind == "enum_mismatch" for issue in issues)
