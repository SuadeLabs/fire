import unittest
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
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
