import json
import os
import unittest


HOME = os.path.realpath(".")
SCHEMAS_DIR = os.path.join(HOME, 'v1-dev')
_, _, filenames = next(os.walk(SCHEMAS_DIR), (None, None, []))
FIRE_SCHEMAS = [f for f in filenames if f.endswith(".json")]

DOCS_DIR = os.path.join(HOME, "documentation", "properties")
_, _, filenames = next(os.walk(DOCS_DIR), (None, None, []))
DOCS = [f for f in filenames if f.endswith(".md")]


class TestSchemas(unittest.TestCase):

    def test_jsons_are_valid(self):
        for schema_name in FIRE_SCHEMAS:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                self.assertTrue(json.load(json_schema))

    def test_property_has_docs(self):
        properties = set()
        for schema_name in FIRE_SCHEMAS:
            print(schema_name)
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                schema = json.load(json_schema)
                if schema_name == "common.json":
                    props = schema.keys()
                else:
                    props = schema["properties"].keys()

                {properties.add(p) for p in props}

        self.assertTrue(DOCS)
        self.assertTrue(properties)

        for p in properties:
            self.assertIn(p, DOCS)
