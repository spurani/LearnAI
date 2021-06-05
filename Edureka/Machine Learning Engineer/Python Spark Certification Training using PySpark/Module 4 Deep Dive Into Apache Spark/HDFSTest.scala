import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
// Create spark context with Spark configuration

object HDFSTest {
    def main(args: Array[String]) {
       val conf = SparkConf().setAppName("Scala Spark Word Count").set("spark.hadoop.yarn.resourcemanager.address","192.168.0.104:8032")
    val sc = SparkContext(conf=conf)

    val textFile = sc.textFile("/user/edureka_1118556/Practice/PySpark.txt")
    val counts = textFile.flatMap(line => line.split(" "))
                  .map(word => (word, 1))
                  .reduceByKey(_ + _)
    counts.saveAsTextFile("/user/edureka_1118556/Practice/OutputScala")
    }
}
