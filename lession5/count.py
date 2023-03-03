from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local").setAppName("count app")
sc = SparkContext.getOrCreate(conf=conf)
words = sc.parallelize (
   ["scala", 
   "java", 
   "hadoop", 
   "spark", 
   "akka",
   "spark vs hadoop", 
   "pyspark",
   "pyspark and spark"]
)
counts = words.count()
print ("Number of elements in RDD -> %i" % (counts))