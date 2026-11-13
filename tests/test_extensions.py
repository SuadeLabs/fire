from string import digits

import iso3166
import pytest
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError
from . import (
    ALLOWED_PROPERTY_CHARS,
    SCHEMA_FILES,
    EXTENSION_DOCS_DIR,
    EXTENSION_DOC_NAMES,
    EXTENSION_SCHEMAS_DIR,
    EXTENSION_FILES,
    DOC_NAMES,
    check_schema_fields,
    fire_load,
    load_jsons,
    schema_properties,
)
import os

_ABSTRACT_SCHEMAS = frozenset(
    ("batch.json", "common.json", "entity.json", "example.json")
)
_VALID_COUNTRY_CODES = frozenset((c[1] for c in iso3166.countries))


def test_schemas_and_docs_found():
    assert EXTENSION_FILES
    assert EXTENSION_DOC_NAMES


def test_jsons_are_valid():
    assert load_jsons(EXTENSION_FILES, EXTENSION_SCHEMAS_DIR)


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_required_fields(schema_name):
    check_schema_fields(EXTENSION_SCHEMAS_DIR, schema_name)


@pytest.mark.parametrize("schema", SCHEMA_FILES)
def test_all_extensions_defined(schema):
    """
    For simplicity we should define an extended version of the schema for
    each non-abstract fire schema, even if that extended version is the same
    as the original (consumers can choose which directory to load from).

    On the other hand extensions should not be defined for certain non-extendable
    schemas like "batch", where jurisdiction-specific additions don't make sense.
    """
    if schema in _ABSTRACT_SCHEMAS:
        assert (
            schema not in EXTENSION_FILES
        ), f"{schema} should not have an extension defined"
    else:
        assert schema in EXTENSION_FILES, f"{schema} should have an extension defined"


@pytest.mark.parametrize("schema", EXTENSION_FILES)
def test_extension_schemas_extend_originals(schema):
    """
    Extended schemas should just be the compsite of the original fire
    schema and extra properties.
    """

    json_schema = fire_load(schema, schemas_dir=EXTENSION_SCHEMAS_DIR)
    # extended schema is extending the original one
    assert "allOf" in json_schema
    components = json_schema["allOf"]
    assert len(components) == 1
    ref = components[0]["$ref"]
    assert ref.endswith(f"/schemas/{schema}")


def test_extended_schema_validations():
    """
    Check that the "required" property of our schemas is respected,
    and other validations work too.
    """

    json_schema = fire_load("customer.json", schemas_dir=EXTENSION_SCHEMAS_DIR)

    Draft7Validator.check_schema(json_schema)
    validator = Draft7Validator(json_schema)

    # missing date
    with pytest.raises(ValidationError, match="date"):
        validator.validate({"id": "missing date"})

    # malformed date
    with pytest.raises(ValidationError, match="date"):
        validator.validate({"id": "bad date", "date": 3})

    # malformed postal code
    with pytest.raises(ValidationError, match="postal_code"):
        validator.validate(
            {"id": "ok", "date": "2000-01-01", "mailing_postal_code": 123}
        )

    # good example
    validator.validate({"id": "ok", "date": "2000-01-01", "mailing_postal_code": "123"})


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_schema_property_names(schema_name):
    """
    JSON may not care about order, or formatting but we do. For the schemas to be
    human readable, it helps when properties are in alphabetical order and snake case.
    """
    properties = list(
        fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)["properties"]
    )
    assert properties == sorted(properties)

    for property in properties:
        assert ALLOWED_PROPERTY_CHARS.issuperset(property)
        assert property
        assert property[0] not in digits + "_"
        assert property[-1] != "_"
        assert "__" not in property


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_schema_properties_have_jurisdiction(schema_name):
    """
    JSON may not care about order, but we do. For the schemas to be
    human readable, it helps when properties are in alphabetical order.

    We ignore inheritance, because we just care about how each individual schema "looks"
    """
    properties = fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)["properties"]
    for property_name, property_spec in properties.items():
        jurisdictions = property_spec["jurisdictions"]
        assert (
            len(jurisdictions) > 0
        ), f"{property_name} should have a list of applicable jurisdictions"
        for jurisdiction in jurisdictions:
            assert (
                jurisdiction in _VALID_COUNTRY_CODES
            ), f"{property_name}: {jurisdiction} should be a valid jurisdiction"


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_schema_property_overlap(schema_name):
    """
    The extension properties should be distinct from the regular ones.
    """
    extension_properties = list(
        fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)["properties"]
    )
    regular_properties = schema_properties(schema_name, with_inheritance=True)

    overlaps = set(extension_properties).intersection(regular_properties)
    assert not overlaps, f"{schema_name} has overlap(s): {overlaps}"


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_properties_and_documentation_align(schema_name):
    """
    Every property should be documented, and every piece of documentation should
    have a corresponding property in the extensions.
    """
    # properties = set()
    # schemas = load_jsons(EXTENSION_FILES, EXTENSION_SCHEMAS_DIR)
    # for schema in schemas:
    #     properties.update(schema["properties"])

    schema = fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)
    properties = schema.get("properties", {})

    for name in properties:
        assert (
            name in EXTENSION_DOC_NAMES
        ), f"[{schema_name}]:every extension property should have documentation"


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_extension_enums_documented(schema_name):
    """
    Each enum value in extension schemas should have a corresponding level 3 header (###) in the
    documentation markdown file.

    eg. ### enum_value
    """

    def error_msg(schema_name, value, enum):
        return (
            f"Could not find a level-3 header (###) entry for "
            f"{schema_name}:{value} in {enum}.md"
        )

    # Load the schema and get its properties
    schema = fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)
    properties = schema.get("properties", {})

    # Check each property for enums
    for prop_name, prop_spec in properties.items():
        if "enum" in prop_spec:
            # Get the documentation file for this property
            doc_file = os.path.join(EXTENSION_DOCS_DIR, f"{prop_name}.md")

            if not os.path.exists(doc_file):
                raise FileNotFoundError(
                    f"Could not find documentation for: {schema_name} :: {prop_name}"
                )

            # Read the documentation file
            with open(doc_file) as f:
                doc_content = f.read()

            # Check each enum value has a level 3 header
            for enum_value in prop_spec["enum"]:
                assert f"### {enum_value}" in doc_content, error_msg(
                    schema_name, enum_value, prop_name
                )


@pytest.mark.parametrize("schema_name", EXTENSION_FILES)
def test_schema_enums_are_alphabetical(schema_name):
    """
    Test that all enum values in the extension schema are in alphabetical order.
    This ensures consistency and makes it easier to find values in the documentation.
    Only checks enums defined in the extension schema, not inherited from parent schemas.
    """
    schema = fire_load(schema_name, schemas_dir=EXTENSION_SCHEMAS_DIR)
    properties = schema.get("properties", {})

    for property_name, property_spec in properties.items():
        if "enum" in property_spec:
            enum_values = property_spec["enum"]
            sorted_values = sorted(enum_values)
            assert enum_values == sorted_values, (
                f"Enum values for {schema_name}:{property_name} are not in alphabetical order.\n"
                f"Current order: {enum_values}\n"
                f"Expected order: {sorted_values}"
            )


@pytest.mark.parametrize("doc_name", EXTENSION_DOC_NAMES)
def test_extensions_dont_duplicate_properties(doc_name):
    """
    Test that we don't create an extension property that already exists in the mean schemas
    """
    assert doc_name not in DOC_NAMES
