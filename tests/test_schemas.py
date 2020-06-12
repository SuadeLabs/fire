import json
import os
import re
import unittest
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
        ]
        long_names = [
            "independent_collateral_amount",
            "interest_repayment_frequency",
            "buy_to_let_house_purchase",
            "buy_to_let_further_advance",
            "cancelled_payout_agreed",
            "firm_operating_expenses",
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

    def test_property_has_docs(self):
        """TODO: add documentation for adjustment schema"""
        properties = all_properties()

        self.assertTrue(properties)

        no_docs = []
        for p in properties:
            if p not in DOC_NAMES:
                no_docs.append(p)

        print("No documenation found for properties: {}".format(no_docs))
        # TODO: Add docs!
        # self.assertFalse(
        #     no_docs,
        #     "No documenation found for properties: {}".format(no_docs)
        # )
        # for doc in DOC_NAMES:
        #     self.assertIn(doc, properties)
