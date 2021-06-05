import sys

from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

    # Create spark context with Spark configuration
    conf = SparkConf().setAppName("Word Count - Python").set("spark.hadoop.yarn.resourcemanager.address","192.168.0.104:8032")
    sc = SparkContext(conf=conf)

    # Read in text file and split each document into words
    words = sc.textFile("/user/edureka_1118556/Practice/PySpark.txt").flatMap(lambda line: line.split(" "))

    #Count the occurence of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

    wordCounts.saveAsTextFile("/user/edureka_1118556/Practice/Output")