import json
import os
import re
from string import digits

import pytest
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError
from . import (
    ALLOWED_PROPERTY_CHARS,
    DOC_NAMES,
    EXAMPLES_DIR,
    EXAMPLE_FILES,
    SCHEMAS_DIR,
    SCHEMA_FILES,
    SCHEMA_NAMES,
    check_schema_fields,
    fire_stats,
    load_jsons,
    schema_enum_registry,
    schema_properties,
)


class TestSchemas:
    def test_schemas_and_docs_found(self):
        assert SCHEMA_NAMES
        assert DOC_NAMES

    def test_jsons_are_valid(self):
        load_jsons(SCHEMA_FILES, SCHEMAS_DIR)
        load_jsons(EXAMPLE_FILES, EXAMPLES_DIR)

    @pytest.mark.parametrize("schema", SCHEMA_FILES)
    def test_enum_registry(self, schema):
        enums = schema_enum_registry(schema)
        if schema in (
            "batch.json",
            "example.json",
            "guarantor.json",
            "issuer.json",
            "risk_rating.json",
        ):
            assert not enums
        else:
            assert enums

    @pytest.mark.parametrize("schema", SCHEMA_FILES)
    def test_enums(self, schema):
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
            "legal_form",  # Nace code format: A.01.10
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

    @pytest.mark.parametrize("schema_name", SCHEMA_FILES)
    def test_schema_properties_are_alphabetical(self, schema_name):
        """
        JSON may not care about order, but we do. For the schemas to be
        human readable, it helps when properties are in alphabetical order.

        We ignore inheritance, because we just care about how each individual schema "looks"
        """
        properties = list(schema_properties(schema_name, with_inheritance=False))

        if "id" in properties:
            assert properties.pop(0) == "id"
            assert properties.pop(0) == "date"

        assert properties == sorted(properties)

        for property in properties:
            assert ALLOWED_PROPERTY_CHARS.issuperset(property)
            assert property
            assert property[0] not in digits + "_"
            assert property[-1] != "_"
            assert "__" not in property

    @pytest.mark.parametrize("schema_name", SCHEMA_FILES)
    def test_schema_enums_are_alphabetical(self, schema_name):
        """
        Oh yeah, Enums, too.

        Except if the order has a mathematical relationship (eg. frequencies)
        """
        exceptions = {
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
        }
        enums = schema_enum_registry(schema_name)
        for enum in enums:
            if enum in exceptions:
                continue
            # print(sorted([str(e) for e in enums[enum]]))
            assert enums[enum] == sorted(enums[enum])

    @pytest.mark.parametrize("schema_name", SCHEMA_FILES)
    def test_required_fields(self, schema_name):
        check_schema_fields(SCHEMAS_DIR, schema_name)


class TestExamples:
    with open(os.path.join(SCHEMAS_DIR, "example.json")) as ff:
        example_schema = json.load(ff)

    validator = Draft7Validator(example_schema)

    @pytest.mark.parametrize("example_name", EXAMPLE_FILES)
    def test_validating_all_examples(self, example_name):
        """
        Examples should match the example schema found in /schemas/example.json
        """
        with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
            ex = json.load(ff)

        self.validator.validate(instance=ex)

    @pytest.mark.parametrize("example_name", EXAMPLE_FILES)
    def test_ex_titles_match_filenames(self, example_name):
        with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
            ex = json.load(ff)

        assert ex["title"] + ".json" == example_name

    def test_ex_titles_are_unique(self):
        titles = set()
        for example_name in EXAMPLE_FILES:
            with open(os.path.join(EXAMPLES_DIR, example_name)) as ff:
                ex = json.load(ff)

            assert ex["title"] not in titles

            titles.add(ex["title"])

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


class TestCurveSchema:
    with open(os.path.join(SCHEMAS_DIR, "curve.json")) as ff:
        curve_schema = json.load(ff)

    validator = Draft7Validator(curve_schema)

    def test_valid_risk_rating_curve(self):
        """Test a valid risk rating curve with string values"""
        valid_risk_rating_curve = {
            "id": "risk_curve_1",
            "date": "2024-03-20T00:00:00Z",
            "type": "risk_rating",
            "values": [
                {"reference": "1m", "value": "AAA"},
                {"reference": "3m", "value": "AA"},
                {"reference": "6m", "value": "A"},
            ],
        }
        self.validator.validate(instance=valid_risk_rating_curve)

    def test_valid_rate_curve(self):
        """Test a valid rate curve with number values"""
        valid_rate_curve = {
            "id": "rate_curve_1",
            "date": "2024-03-20T00:00:00Z",
            "type": "rate",
            "values": [
                {"reference": "1m", "value": 0.01},
                {"reference": "3m", "value": 0.015},
                {"reference": "6m", "value": 0.02},
            ],
        }
        self.validator.validate(instance=valid_rate_curve)

    def test_unknown_curve_type(self):
        # Unknown curve type: numbers are default for backwards compatibility
        unknown_curve = {
            "id": "rate_curve_1",
            "date": "2024-03-20T00:00:00Z",
            "values": [{"reference": "1m", "value": 0.01}],
        }
        self.validator.validate(instance=unknown_curve)

        unknown_curve["values"] = [{"reference": "1m", "value": "AAA"}]
        with pytest.raises(
            ValidationError, match="is not valid under any of the given schemas"
        ):
            self.validator.validate(instance=unknown_curve)

    def test_invalid_mixed_value_types(self):
        """Test an invalid curve with mixed string and number values"""
        invalid_mixed_curve = {
            "id": "mixed_curve_1",
            "date": "2024-03-20T00:00:00Z",
            "type": "rate",
            "values": [
                {"reference": "1m", "value": 0.01},
                {"reference": "3m", "value": "AAA"},
                {"reference": "6m", "value": 0.02},
            ],
        }
        with pytest.raises(
            ValidationError, match="is not valid under any of the given schemas"
        ):
            self.validator.validate(instance=invalid_mixed_curve)


class TestRunStats:
    def test_property_count(self):
        stats = fire_stats()
        print(f"\n\n    ======== FIRE STATISTICS =======\n\n{stats}\n\n")
        assert stats
