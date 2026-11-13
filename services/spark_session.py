import os
from pyspark.sql import SparkSession
#Use this lightweight configuration:
#This configuration limits Spark's local parallelism. It does not guarantee that the entire application will fit in 1 GB RAM.
def create_spark_session():
    """
    Create a memory-conscious local Spark session
    for the Indian Stock Analyzer application.
    """

    os.environ.setdefault(
        "SPARK_LOCAL_IP", "127.0.0.1"
    )

    spark = (
        SparkSession.builder
        .appName("IndianStockAnalyzer")
        .master("local[1]")
        .config("spark.ui.enabled", "false")
        #.config("spark.driver.memory", "384m")
        .config("spark.driver.memory", "512m")
        .config("spark.driver.maxResultSize", "128m")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.default.parallelism", "1")
        .config("spark.sql.execution.arrow.pyspark.enabled", "false")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    return spark
