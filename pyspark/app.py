import os
from pyspark.sql import SparkSession
from app import main

os.environ['PYSPARK_PYTHON'] = "/home/blue/pyspark_pex_env.pex"
spark = SparkSession.builder.config(
    "spark.files",  # 'spark.yarn.dist.files' in YARN.
    "pyspark_pex_env.pex").getOrCreate()
main(spark)