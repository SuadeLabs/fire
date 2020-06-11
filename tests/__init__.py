import json
import os


HOME = os.path.join(os.path.dirname(__file__), "..")
SCHEMAS_DIR = os.path.join(HOME, 'v1-dev')
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


def fire_load(schema_name):
    with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
        schema = json.load(json_schema)
    return schema
