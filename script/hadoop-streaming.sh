$HADOOP_HOME/bin/hadoop jar /home/blue/project/data/dist/hadoop-streaming-2.7.3.jar \
    -input /word_count/word_count.txt \
    -output /word_count/output \
    -mapper "/usr/bin/python3 /home/blue/project/data/hadoop/streaming/mapper.py" \
    -reducer "/usr/bin/python3 /home/blue/project/data/hadoop/streaming/reducer.py"