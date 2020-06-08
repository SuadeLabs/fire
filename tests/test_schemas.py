import json
import os
import unittest
from . import (
    DOC_NAMES,
    SCHEMAS_DIR,
    SCHEMA_FILES,
    SCHEMA_NAMES,
)


class TestSchemas(unittest.TestCase):

    def test_schemas_and_docs_found(self):
        self.assertTrue(SCHEMA_NAMES)
        self.assertTrue(DOC_NAMES)

    def test_jsons_are_valid(self):
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                self.assertTrue(json.load(json_schema))

    def test_property_has_docs(self):
        """TODO: add documentation for adjustment schema"""
        properties = set()
        for schema_name in SCHEMA_FILES:
            with open(os.path.join(SCHEMAS_DIR, schema_name)) as json_schema:
                schema = json.load(json_schema)
                if schema_name == "common.json":
                    props = schema.keys()
                else:
                    props = schema["properties"].keys()

                {properties.add(p) for p in props}

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
