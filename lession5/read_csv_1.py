from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import *
# Programmatic way to define a schema
spark = (SparkSession
             .builder
             .appName("lessionSpark")
             .getOrCreate())
# Use the DataFrameReader interface to read a CSV file
sf_fire_file = "/home/blue/project/python/mci/mci-dw-dl/lession5-spark/departuredelat.csv"

df = (
    spark.read.format('csv') \
    .option("inferSchema", "true") \
    .option("header", "true") \
    .load(sf_fire_file) \
)

df.createOrReplaceGlobalTempView("us_delay_flights_tbl");

spark.sql("""SELECT distance, origin, destination 
FROM us_delay_flights_tbl WHERE distance > 1000
ORDER BY distance DESC""").show(10)

(df.select("distance","origin","destination")
 .where("distance > 1000")
 .orderBy("distance",ascending=False).show(10))