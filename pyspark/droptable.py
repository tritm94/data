from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import *

# Programmatic way to define a schema
spark = (SparkSession
             .builder
             .appName("FinalCSV")
             .getOrCreate())

spark.sql("DROP TABLE IF EXISTS SendyLogistics")