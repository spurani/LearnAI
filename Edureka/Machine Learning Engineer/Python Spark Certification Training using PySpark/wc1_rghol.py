import sys
from pyspark import SparkContext, SparkConf

if __name__ == '__main__':
    # create SparkContext with SparkConf
    conf = SparkConf().setAppName("edureka_1068176 - WordCount")
    sc = SparkContext(conf=conf)
    
    # read in text file and split each document into words
    words = sc.textFile('/user/edureka_1068176/sample.txt').flatMap(lambda line: line.split(' '))
    
    # count occurences of each word
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
    
    wordCounts.saveAsTextFile('/user/edureka_1068176/output1/')
