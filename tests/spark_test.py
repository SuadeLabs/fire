import unittest
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from fire.spark import FireModel
import pkg_resources
import fire
import os
import json


class FireSparkTest(unittest.TestCase):

    def setUp(self):
        self.spark = SparkSession.builder.appName("FIRE_SPARK").master("local").getOrCreate()

    def tearDown(self) -> None:
        self.spark.stop()

    def test_schema(self):
        fire_directory = pkg_resources.resource_filename(fire.__name__, 'data/')
        for entity in [f.split('.')[0] for f in os.listdir(fire_directory)]:

            json_file = os.path.join(fire_directory, "{}.json".format(entity))
            with open(json_file) as f:
                json_model = json.loads(f.read())
                tpe = json_model.get('type', None)
                if tpe != "object":
                    break

            model = FireModel().load(entity)
            self.assertTrue(len(model.schema.fields) > 0)
            for field in model.schema.fields:
                print(field)
            self.assertTrue(len(model.constraints) > 0)
            for constraint in model.constraints:
                print(constraint)

    def test_schema_apply(self):
        files = "tests/data/collateral.json"
        model = FireModel().load("collateral")
        df = self.spark.read.format("json").schema(model.schema).load(files)
        df.show()
        self.assertEqual(1000, df.count())

    def test_constraints_apply(self):
        files = "tests/data/collateral.json"
        model = FireModel().load("collateral")
        constraints = model.constraints
        self.spark.read.format("json").schema(model.schema).load(files) \
            .select(F.explode(F.array([F.expr(c) for c in constraints])).alias("fire")) \
            .groupBy("fire") \
            .count() \
            .show()


if __name__ == '__main__':
    unittest.main()
