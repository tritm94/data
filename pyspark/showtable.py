from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import *

# Programmatic way to define a schema
spark = (SparkSession
             .builder
             .appName("FinalCSV")
             .getOrCreate())

parquet_table = 'SendyLogistics'
sendyLogisticsDf = spark.read.parquet("/home/blue/spark-warehouse/sendylogistics")

sendyLogisticsDf.show(5);