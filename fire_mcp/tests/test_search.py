from __future__ import annotations

from fire_mcp import search


def test_search_fields_typo_still_finds_target():
    results = search.search_fields("acc_fv_chnge_credit_risk")
    fields = {r.field for r in results}
    assert "acc_fv_change_credit_risk" in fields


def test_search_fields_matches_on_enum_value():
    results = search.search_fields("fv_thru_pnl")
    assert any(
        r.field == "accounting_treatment" and r.matched_on == "enum" for r in results
    )


def test_search_fields_short_id_query_ranks_id_fields_first():
    results = search.search_fields("customer id", limit=5)
    assert results
    assert results[0].field in {"id", "customer_id"}
