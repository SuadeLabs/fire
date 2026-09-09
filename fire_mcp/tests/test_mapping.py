from __future__ import annotations

from fire_mcp import search


def test_suggest_mapping_finds_plausible_candidates():
    results = search.suggest_mapping("loan", ["cust_id", "loan_bal", "orig_date"])
    by_source: dict[str, list] = {}
    for result in results:
        by_source.setdefault(result.source_field, []).append(result)

    assert set(by_source) == {"cust_id", "loan_bal", "orig_date"}
    for source, candidates in by_source.items():
        assert candidates, source
        assert candidates[0].score > 0


def test_suggest_mapping_boosts_enum_value_match():
    results = search.suggest_mapping(
        "loan",
        ["accounting_basis"],
        sample_values={"accounting_basis": "held_for_trading"},
    )
    matches = [r for r in results if r.entity_field == "accounting_treatment"]
    assert matches
    assert any(r.reason == "enum value match" for r in matches)
