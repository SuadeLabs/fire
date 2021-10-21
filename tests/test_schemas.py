import json
import os
import re
import unittest
from collections import OrderedDict
from . import (
    DOC_NAMES,
    EXAMPLES_DIR,
    EXAMPLE_FILES,
    SCHEMAS_DIR,
    SCHEMA_FILES,
    SCHEMA_NAMES,
    all_properties,
    schema_enum_registry,
)


class TestSchemas(unittest.TestCase):

    def test_schemas_and_docs_found(self):
        self.assertTrue(SCHEMA_NAMES)
        self.assertTrue(DOC_NAMES)

    def test_jsons_are_valid(self):
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                self.assertTrue(json.load(json_schema))

        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as json_schema:
                self.assertTrue(json.load(json_schema))

    def test_enum_registry(self):
        for schema in SCHEMA_FILES:
            enums = schema_enum_registry(schema)
            if schema in ["batch.json", "guarantor.json", "issuer.json"]:
                self.assertFalse(enums)
            else:
                self.assertTrue(enums)

    def test_enums(self):
        """
        Enums should be snake_case (mostly)
        Enums should be less than 24 characters
        """
        def snake_error(schema, enum, value):
            return "{} > {} > {} isn't snake_case!".format(
                schema, enum, value)

        def len_error(schema, enum, value, length):
            return "{} > {} > {} longer than 22 chars! ({})".format(
                schema, enum, value, length)

        exceptions = [
            "country_code",  # ISO 3166
            "currency_code",  # ISO 4217
            "base_currency_code",  # ISO 4217
            "quote_currency_code",  # ISO 4217
            "underlying_index_tenor",  # day convention
            "base_rate",  # Bloomberg tickers,
            "nace_code"  # Nace code format: A.01.10
        ]
        long_names = [
            "independent_collateral_amount",
            "interest_repayment_frequency",
            "buy_to_let_house_purchase",
            "buy_to_let_further_advance",
            "cancelled_payout_agreed",
            "firm_operating_expenses",
            "acquired_credit_impaired"
        ]

        snake_pattern = re.compile("[a-z][a-z0-9]*(_[a-z0-9]*)*")
        for schema in SCHEMA_FILES:
            enums = schema_enum_registry(schema)
            for enum, values in enums.items():
                match = re.match(snake_pattern, enum)
                self.assertIsNotNone(match, snake_error(schema, enum, ""))
                self.assertEqual(
                    0, match.start(), snake_error(schema, enum, ""))
                self.assertEqual(
                    len(enum), match.end(), snake_error(schema, enum, ""))

                if enum not in long_names:
                    self.assertLessEqual(
                        len(enum), 22,
                        len_error(schema, enum, "", len(enum))
                    )
                if enum in exceptions:
                    continue
                for v in values:
                    match = re.match(snake_pattern, v)
                    self.assertIsNotNone(match, snake_error(schema, enum, v))
                    self.assertEqual(
                        0, match.start(), snake_error(schema, enum, v))
                    self.assertEqual(
                        len(v), match.end(), snake_error(schema, enum, v))

                    if v not in long_names:
                        self.assertLessEqual(
                            len(v), 22,
                            len_error(schema, enum, v, len(v))
                        )

    def test_schema_properties_are_alphabetical(self):
        """
        JSON may not care about order, but we do. For the schemas to be
        human readable, it helps when properties are in alphabetical order.
        """
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                schema = json.load(json_schema, object_pairs_hook=OrderedDict)  # noqa
                if "properties" in schema:
                    properties = schema["properties"].keys()
                else:
                    properties = schema.keys()

                properties = list(properties)

                if "id" in properties:
                    self.assertEqual(properties[0], "id")
                    self.assertEqual(properties[1], "date")
                    properties.pop(1)
                    properties.pop(0)

                self.assertEqual(properties, sorted(properties))

    def test_schema_enums_are_alphabetical(self):
        """
        Oh yeah, Enums, too.

        Except if the order has a mathematical relationship (eg. frequencies)
        """
        exceptions = [
            "underlying_index_tenor",
            "margin_frequency",
            "repayment_frequency",
            "interest_repayment_frequency",
            "moodys_lt",
            "moodys_st",
            "snp_lt",
            "snp_st",
            "fitch_st",
            "fitch_lt"
        ]
        for schema_name in SCHEMA_FILES:
            enums = schema_enum_registry(schema_name)
            for enum in enums:
                if enum in exceptions:
                    continue
                # print(sorted([str(e) for e in enums[enum]]))
                self.assertEqual(enums[enum], sorted(enums[enum]))

    def test_property_has_docs(self):
        """
        Ensure there are docs for every new attribute

        TODO: add docs and remove legacy exceptions
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
            "encumbrance_end_date",
            "facility_currency_code",
            "forward_rate",
            "gamma",
            "guarantor_id",
            "insolvency_rank",
            "interest_repayment_frequency",
            "intra_group",
            "issuer_id",
            "ledger_code",
            "leg",
            "legal_entity_name",
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
            "provision_type",
            "report_type",
            "reporting_relationship",
            "reset_date",
            "rho",
            "risk_weight_irb",
            "risk_weight_std",
            "row",
            "seniority",
            "settlement_type",
            "stay_protocol",
            "theta",
            "underlying_derivative_id",
            "underlying_issuer_id",
            "underlying_price",
            "underlying_security_id",
            "underlying_strike",
            "values",
            "vega",
            "vol_adj",
            "vol_adj_fx"
        ]

        properties = all_properties()
        self.assertTrue(properties)

        no_docs = []
        for p in properties:
            if p not in DOC_NAMES + exceptions:
                no_docs.append(p)

        self.assertFalse(
            no_docs,
            "No documenation found for properties: {}".format(no_docs)
        )
        for doc in DOC_NAMES:
            self.assertTrue(
                doc in properties,
                "No property found for documenation: {}".format(doc)
            )
