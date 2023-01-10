import os
import unittest
from . import (
    SCHEMA_NAMES,
    all_properties,
    DOCS_DIR,
    DOC_NAMES,
    property_doc_name,
    schema_enum_registry,
)


class TestDocs(unittest.TestCase):
    def test_property_has_docs(self):
        """
        Ensure there are docs for every new attribute
        """
        exceptions = [
            "account_ids",
            "accrued_interest_balance",
            "behavioral_curve_id",
            "cb_haircut",
            "ccf",
            "col",
            "comment",
            "contribution_amount",
            "contribution_text",
            "customers",
            "data",
            "delta",
            "derivative_id",
            "el_irb",
            "encumbrance_end_date",
            "facility_currency_code",
            "forward_rate",
            "gamma",
            "guarantor_id",
            "insolvency_rank",
            "intra_group",
            "issuer_id",
            "ledger_code",
            "leg",
            "legal_entity_name",
            "lgd_downturn",
            "lgd_irb",
            "links",
            "loan_id",
            "loan_ids",
            "national_reporting_code",
            "next_exercise_date",
            "next_payment_amount",
            "next_receive_amount",
            "next_receive_date",
            "next_repricing_date",
            "next_reset_date",
            "page",
            "payment_date",
            "pd_irb",
            "pd_retail_irb",
            "report_type",
            "reset_date",
            "rho",
            "risk_weight_irb",
            "risk_weight_std",
            "row",
            "settlement_type",
            "theta",
            "title",
            "underlying_derivative_id",
            "underlying_issuer_id",
            "underlying_security_id",
            "underlying_strike",
            "values",
            "vega",
            "vol_adj",
            "vol_adj_fx",
        ]

        properties = all_properties()
        self.assertTrue(properties)

        no_docs = []
        for p in properties:
            if p not in DOC_NAMES + exceptions:
                no_docs.append(p)

        self.assertFalse(
            no_docs, "No documenation found for properties: {}".format(no_docs)
        )
        for doc in DOC_NAMES:
            self.assertTrue(
                doc in properties, "No property found for documenation: {}".format(doc)
            )

    def test_enums_documented(self):
        """
        Each enum value should have a corresponding level 3 header (###) in the
        documentation markdown file.

        eg. ### enum_value
        """

        def error_msg(schema_name, value, enum):
            return (
                "Could not find a level-3 header (###) entry for "
                "{}:'{}' in {}.md.\n\n".format(schema_name, value, enum)
            )

        exceptions = [
            "country_code",  # TL;DR
            "currency_code",  # TL;DR
            "nace_code",  # TL;DR
            "interest_repayment_frequency",  # Same as repayment_frequency
            "reporting_relationship",  # same as relationship
        ]
        for schema_name in SCHEMA_NAMES:
            for enum, values in schema_enum_registry(schema_name).items():
                if enum in exceptions:
                    continue

                property_docs = property_doc_name(enum)

                if not property_docs:
                    raise FileNotFoundError(
                        f"Could not find documentation for: {schema_name} :: {enum}"
                    )  # noqa

                _file = os.path.join(DOCS_DIR, property_docs)

                for v in values:
                    with open(_file) as enum_doc:
                        assert "### {}".format(v) in enum_doc.read(), error_msg(
                            schema_name, v, enum
                        )  # noqa
