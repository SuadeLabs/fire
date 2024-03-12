import json
import os
import re
import unittest
import pytest
from collections import OrderedDict
from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError
from . import (
    DOC_NAMES,
    EXAMPLES_DIR,
    EXAMPLE_FILES,
    SCHEMAS_DIR,
    SCHEMA_FILES,
    SCHEMA_NAMES,
    schema_enum_registry,
    fire_stats,
)


class TestSchemas(unittest.TestCase):
    def test_schemas_and_docs_found(self):
        assert SCHEMA_NAMES
        assert DOC_NAMES

    def test_jsons_are_valid(self):
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                assert json.load(json_schema)

        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as json_schema:
                assert json.load(json_schema)

    def test_enum_registry(self):
        for schema in SCHEMA_FILES:
            enums = schema_enum_registry(schema)
            if schema in [
                "batch.json",
                "example.json",
                "guarantor.json",
                "issuer.json",
            ]:
                assert not enums
            else:
                assert enums

    def test_enums(self):
        """
        Enums should be snake_case (mostly)
        Enums should be less than 24 characters
        """

        def snake_error(schema, enum, value):
            return "{} > {} > {} isn't snake_case!".format(schema, enum, value)

        def len_error(schema, enum, value, length):
            return "{} > {} > {} longer than 22 chars! ({})".format(
                schema, enum, value, length
            )

        exceptions = [
            "country_code",  # ISO 3166
            "currency_code",  # ISO 4217
            "base_currency_code",  # ISO 4217
            "quote_currency_code",  # ISO 4217
            "underlying_index_tenor",  # day convention
            "base_rate",  # Bloomberg tickers,
            "nace_code",  # Nace code format: A.01.10
        ]
        legacy_long_names = [
            "independent_collateral_amount",
            "interest_repayment_frequency",
            "buy_to_let_house_purchase",
            "buy_to_let_further_advance",
            "cancelled_payout_agreed",
            "firm_operating_expenses",
            # DO NOT ADD TO THIS LIST, FIX YOUR ENUM INSTEAD
        ]

        snake_pattern = re.compile("[a-z][a-z0-9]*(_[a-z0-9]*)*")
        for schema in SCHEMA_FILES:
            enums = schema_enum_registry(schema)
            for enum, values in enums.items():
                match = re.match(snake_pattern, enum)
                assert match is not None, snake_error(schema, enum, "")
                assert 0 == match.start(), snake_error(schema, enum, "")
                assert len(enum) == match.end(), snake_error(schema, enum, "")

                if enum not in legacy_long_names:
                    assert len(enum) <= 22, len_error(
                        schema, enum, "", len(enum)
                    )  # noqa: E501

                if enum in exceptions:
                    continue
                for v in values:
                    match = re.match(snake_pattern, v)
                    assert match is not None, snake_error(schema, enum, v)
                    assert 0 == match.start(), snake_error(schema, enum, v)
                    assert len(v) == match.end(), snake_error(schema, enum, v)

                    if v not in legacy_long_names:
                        assert len(v) <= 22, len_error(schema, enum, v, len(v))

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
                    assert properties[0] == "id"
                    assert properties[1] == "date"
                    properties.pop(1)
                    properties.pop(0)

                assert properties == sorted(properties)

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
            "fitch_lt",
            "dbrs_lt",
            "dbrs_st",
            "kbra_lt",
            "kbra_st",
        ]
        for schema_name in SCHEMA_FILES:
            enums = schema_enum_registry(schema_name)
            for enum in enums:
                if enum in exceptions:
                    continue
                # print(sorted([str(e) for e in enums[enum]]))
                assert enums[enum] == sorted(enums[enum])

    def test_property_count(self):
        stats = fire_stats()
        print(f"\n\n    ======== FIRE STATISTICS =======\n\n{stats}\n\n")
        assert stats

    def test_required_fields(self):
        """
        Every property in a schema should have a type and description
        """
        errs = []
        required = ["description", "type"]
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                schema = json.load(json_schema)

            if schema_name != "common.json":
                for prop, fields in schema["properties"].items():
                    if "$ref" in fields:
                        continue
                    errs += [
                        (schema_name, prop, r) for r in required if r not in fields
                    ]
            else:
                errs += [(schema_name, prop, r) for r in required if r not in fields]

        assert (
            not errs
        ), "The following schemata are missing required fields:\n\t" + "\n\t".join(
            "- {} schema has property '{}' missing required field '{}'".format(
                e[0], e[1], e[2]
            )
            for e in errs
        )


class TestExamples:
    with open(os.path.join(SCHEMAS_DIR, "example.json")) as ff:
        example_schema = json.load(ff)

    validator = Draft4Validator(example_schema)

    def test_validating_all_examples(self):
        """
        Examples should match the example schema found in /v1-dev/example.json
        """
        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
                ex = json.load(ff)

            self.validator.validate(instance=ex)

    def test_ex_titles_match_filenames(self):
        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
                ex = json.load(ff)

            assert ex["title"] + ".json" == example_name

    def test_ex_titles_are_unique(self):
        titles = []
        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
                ex = json.load(ff)

            assert ex["title"] not in titles

            titles.append(ex["title"])

    def test_bad_examples(self):
        """
        Examples can be bad in lots of ways, here we test the most
        common cases...

        Feel free to add more.
        """
        no_data = {"title": "check", "comment": "check"}
        with pytest.raises(ValidationError):
            self.validator.validate(no_data)

        empty_data = {"title": "check", "comment": "check", "data": {}}
        with pytest.raises(ValidationError):
            self.validator.validate(empty_data)

        no_title = {
            "description": "check",
            "comment": "check",
            "data": {"account": [{"id": "123", "date": "2020-02-02"}]},
        }
        with pytest.raises(ValidationError):
            self.validator.validate(no_title)

        bad_data_type = {
            "title": "check",
            "comment": "check",
            "data": {"blah": [{"id": "123", "date": "2020-02-02"}]},
        }
        with pytest.raises(ValidationError):
            self.validator.validate(bad_data_type)

        bad_nested_data = {
            "title": "check",
            "comment": "check",
            "data": {"account": [{"id": 123, "date": "2020-02-02"}]},
        }
        with pytest.raises(ValidationError):
            self.validator.validate(bad_nested_data)

        bad_nested_enum_value = {
            "title": "check",
            "comment": "check",
            "data": {
                "account": [{"id": "123", "date": "2020-02-02", "type": "coorent"}]
            },
        }
        with pytest.raises(ValidationError):
            self.validator.validate(bad_nested_enum_value)

        nested_null_value = {
            "title": "check",
            "comment": "check",
            "data": {"account": [{"id": "123", "date": "2020-02-02", "type": None}]},
        }
        with pytest.raises(ValidationError):
            self.validator.validate(nested_null_value)

        some_bad_data = {
            "title": "check",
            "comment": "check",
            "data": {
                "account": [
                    {"id": "123", "date": "2020-02-02", "type": "current"},
                    {"id": "123", "date": "2020-02-02", "type": None},
                ]
            },
        }
        with pytest.raises(ValidationError):
            self.validator.validate(some_bad_data)

        empty_data = {"title": "check", "comment": "check", "data": {"account": []}}
        with pytest.raises(ValidationError):
            self.validator.validate(empty_data)
