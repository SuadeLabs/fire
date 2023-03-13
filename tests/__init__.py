import decimal
import json
import os


HOME = os.path.join(os.path.dirname(__file__), "..")
SCHEMAS_DIR = os.path.join(HOME, "v1-dev")
DOCS_DIR = os.path.join(HOME, "documentation", "properties")
EXAMPLES_DIR = os.path.join(HOME, "examples")

_, _, filenames = next(os.walk(SCHEMAS_DIR), (None, None, []))
SCHEMA_FILES = [f for f in filenames if f.endswith(".json")]
SCHEMA_NAMES = [f.split(".json")[0] for f in SCHEMA_FILES]

_, _, filenames = next(os.walk(DOCS_DIR), (None, None, []))
DOC_FILES = [f for f in filenames if f.endswith(".md")]
DOC_NAMES = [f.split(".md")[0] for f in DOC_FILES]

_, _, filenames = next(os.walk(EXAMPLES_DIR), (None, None, []))
EXAMPLE_FILES = [f for f in filenames if f.endswith(".json")]


def schema_properties(schema_name):
    """
    Returns the properties for a schema
    """
    schema = fire_load(schema_name)
    if schema_name == "common.json":
        properties = schema.keys()
    else:
        properties = schema["properties"].keys()

    return properties


def schema_enum_registry(schema_name):
    """
    Returns a dictionary of "property name" : [enum values]
    """
    enums = {}

    if "json" != schema_name[-4:]:
        schema_name = schema_name + ".json"

    schema = fire_load(schema_name)

    if schema_name == "common.json":
        properties = schema
    else:
        properties = schema["properties"]

    for prop, obj in properties.items():
        if "$ref" in obj:
            prop = obj["$ref"].split("/")[-1]
            obj = fire_load("common.json")[prop]
        if "enum" in obj:
            enums[prop] = obj["enum"]

    return enums


def all_properties():
    properties = set()
    for schema_name in SCHEMA_FILES:
        {properties.add(prop) for prop in schema_properties(schema_name)}

    return properties


def property_doc_name(property_name: str):
    for doc in DOC_FILES:
        if property_name + ".md" == doc:
            return doc


def fire_load(schema_name):
    with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
        schema = json.load(json_schema)
    return schema


def fire_stats():
    schemas = 0
    properties = 0
    uniq_properties = set()
    combos = []
    for schema_name in SCHEMA_FILES:
        all_props = schema_properties(schema_name)
        enums = schema_enum_registry(schema_name)

        for prop in all_props:
            if prop in enums:
                combos.append(len(prop))
            else:
                combos.append(3)  # we assume ~3 variations for continuous vars

            properties += 1
            uniq_properties.add(prop)

        schemas += 1

    N = 1
    for p in combos:
        N = N * p

    return {
        "schemas": schemas,
        "properties": properties,
        "unique_properties": len(uniq_properties),
        "data_combinations": format(decimal.Decimal(N), ".6e"),
    }
