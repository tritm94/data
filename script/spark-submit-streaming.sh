$SPARK_HOME/bin/spark-submit \
    --class /home/blue/project/data/pyspark/streamingEx.py \
    --master spark://LAPTOP-HBKNP45N.:7077 \
    $SPARK_HOME/jars/spark-streaming_2.13-3.3.2.jar localhost 9999