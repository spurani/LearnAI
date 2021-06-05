from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import datetime
import re
from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import regexp_extract

if __name__ == "__main__":
    sc = SparkContext(appName="LogParser-py-Streaming")
    ssc = StreamingContext(sc, 10)
    now = datetime.datetime.now()

    # define the regular expression - <date-time> <log-type> <message>
    regex = re.compile("^([\d/]+ [\d:]+) ([a-zA-Z]+) (.*)")

    filepath = "/user/edureka_321047/use_cases/streaming/events/" + now.strftime("%Y-%m-%d/")

    print("filepath:", filepath)
    lines = ssc.textFileStream(filepath)

    def getSparkSessionInstance(sparkConf):
        if ("sparkSessionSingletonInstance" not in globals()):
            globals()["sparkSessionSingletonInstance"] = SparkSession \
                .builder \
                .config(conf=sparkConf) \
                .getOrCreate()
        return globals()["sparkSessionSingletonInstance"]

    def process(t, rdd):
        if rdd.isEmpty():
            print("==== EMPTY ====")
            return

        print("=== RDD Found ===")
        rowRdd = rdd.map(lambda x: Row(line=x))
        spark = getSparkSessionInstance(rdd.context.getConf())
        df = spark.createDataFrame(rowRdd)
        print(df.show())
        df2 = df.select(regexp_extract('line', "^([\d/]+ [\d:]+) ([a-zA-Z]+) (.*)", 1).alias("etime"),regexp_extract('line', "^([\d/]+ [\d:]+) ([a-zA-Z]+) (.*)", 2).alias("etype"),regexp_extract('line', "^([\d/]+ [\d:]+) ([a-zA-Z]+) (.*)", 3).alias("emsg"))

        df2 = df2.filter("emsg != ''")
        print(df2.show())        
    
    lines.pprint()  
    lines.foreachRDD(process)

    ssc.start()
    ssc.awaitTermination()
