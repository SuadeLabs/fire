import unittest
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import pkg_resources
import fire
import os
import json
from fire.fire.spark import FireModel

from . import (
    SCHEMA_FILES,
    SCHEMAS_DIR
)


class FireSparkTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.\
            builder.\
            appName("FIRE_SPARK").\
            master("local").\
            getOrCreate()

    def tearDown(self) -> None:
        self.spark.stop()

    def test_schema(self):
        for entity in SCHEMA_FILES:

            json_file = os.path.join(SCHEMAS_DIR, entity)
            with open(json_file) as f:
                json_model = json.loads(f.read())
                tpe = json_model.get('type', None)
                if tpe != "object":
                    break

            model = FireModel(SCHEMAS_DIR).load(entity.split('.')[0])
            self.assertTrue(len(model.schema.fields) > 0)
            for field in model.schema.fields:
                print(field)
            self.assertTrue(len(model.constraints) > 0)
            for constraint in model.constraints:
                print(constraint)

    def test_schema_apply(self):
        files = "tests/data/collateral.json"
        model = FireModel(SCHEMAS_DIR).load("collateral")
        df = self.spark.read.format("json").schema(model.schema).load(files)
        df.show()
        self.assertEqual(1000, df.count())

    def test_constraints_apply(self):
        files = "tests/data/collateral.json"
        model = FireModel(SCHEMAS_DIR).load("collateral")
        constraints = model.constraints
        fire_col = F.array([F.expr(c) for c in constraints])
        self.spark.read.format("json").schema(model.schema).load(files) \
            .select(F.explode(fire_col).alias("fire")) \
            .groupBy("fire") \
            .count() \
            .show()


if __name__ == '__main__':
    unittest.main()
