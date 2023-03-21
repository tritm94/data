from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import *

SRC_SENDY_LOGISTICS = "/home/blue/project/data/dist/sendy_logistics.csv"
# name of the table
PARQUET_TABLE = 'SendyLogisticTable'

# Programmatic way to define a schema
spark = (SparkSession
             .builder
             .appName("FinalCSV")
             .getOrCreate())


# 1. Đọc dữ liệu CSV vào DataFrame
sendyLogisticsSchema = StructType([
    StructField('OrderNo', StringType(), True), \
    StructField('UserId', StringType(), True), \
    StructField('VehicleType', StringType(), True), \
    StructField('PlatformType', IntegerType(), True), \
    StructField('PersonalOrBusiness', StringType(), True), \
    StructField('PlacementDayofMonth', IntegerType(), True), \
    StructField('PlacementWeekday', IntegerType(), True), \
    StructField('PlacementTime', StringType(), True), \
    StructField('ConfirmationDayofMonth', IntegerType(), True), \
    StructField('ConfirmationWeekday', IntegerType(), True), \
    StructField('ConfirmationTime', StringType(), True), \
    StructField('ArrivalatPickupDayofMonth', IntegerType(), True), \
    StructField('ArrivalatPickupWeekday', IntegerType(), True), \
    StructField('ArrivalatPickupTime', StringType(), True), \
    StructField('PickupDayofMonth', IntegerType(), True), \
    StructField('PickupWeekday', IntegerType(), True), \
    StructField('PickupTime', StringType(), True), \
    StructField('ArrivalatDestinationDayofMonth', IntegerType(), True), \
    StructField('ArrivalatDestinationWeekday', IntegerType(), True), \
    StructField('ArrivalatDestinationTime', StringType(), True), \
    StructField('Distance', IntegerType(), True), \
    StructField('Temperature', IntegerType(), True), \
    StructField('Precipitationinmillimeters', FloatType(), True), \
    StructField('PickupLat', FloatType(), True), \
    StructField('PickupLong', FloatType(), True), \
    StructField('DestinationLat', FloatType(), True), \
    StructField('DestinationLong', FloatType(), True), \
    StructField('RiderId', StringType(), True), \
    StructField('TimefromPickuptoArrival', IntegerType(), True)
])


sendyLogisticsDf = spark.read.csv(SRC_SENDY_LOGISTICS, header=True, schema=sendyLogisticsSchema)

sendyLogisticsDf.write.format("parquet").saveAsTable(PARQUET_TABLE)  # .save(parquet_path)

# 2. Xóa các cột không cần thiết

sendyLogisticsDf = (sendyLogisticsDf.drop(
    *('PickupLat','PickupLong', 'DestinationLat', 'DestinationLong')
))

sendyLogisticsDf.show(5, False)

sendyLogisticsDf = sendyLogisticsDf.na.fill(value="")
sendyLogisticsDf = sendyLogisticsDf.na.fill(value=0)

# 3. Chuyển đổi kiểu dữ liệu của cột

sendyLogisticsDf = (sendyLogisticsDf
    .withColumn("PlacementTimeConvert", to_timestamp(col("PlacementTime"), "dd/MM/yyyy HH:mm:ss"))
    .drop("PlacementTime")
    .withColumn(
        "ArrivalatDestinationTimeConvert",
        to_timestamp(
            col("ArrivalatDestinationTime"),
            "dd/MM/yyyy HH:mm:ss"
        )
    ).drop("ArrivalatDestinationTime")
)

sendyLogisticsDf = sendyLogisticsDf.na.fill(value="",
    subset=["PlacementTimeConvert", "ArrivalatDestinationTimeConvert"]
)

sendyLogisticsDf.show(5, False)

# 4.Thêm dữ liệu vào DataFrame

columnsImport = ['OrderNo', 'UserId', 'VehicleType', 'Platform Type']
valsImport = [
    ('Order_No_9999','User_Id_9999', 'Bike', 1),
    ('Order_No_10000','User_Id_10000', 'Car', 3)
]

sendyLogisticsDf = spark.createDataFrame(valsImport, columnsImport)

sendyLogisticsDf.show(5, False)

# 5.Lưu trữ kết quả vào tập tin Parquet

sendyLogisticsDf.write.parquet('/home/blue/project/data/dist/output/SendyLogistic.parquet')