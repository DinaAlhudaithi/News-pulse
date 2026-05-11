from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, lower, window

spark = SparkSession.builder.appName("News Pulse Big Data Challenge").getOrCreate()

df = spark.read.csv("mock_news.csv", header=True, inferSchema=True)

print("=== News Data ===")
df.show(truncate=False)

print("=== Headlines Count by Source ===")
df.groupBy("source").count().show()

words_df = df.select(
    col("source"),
    col("timestamp"),
    explode(split(lower(col("headline")), " ")).alias("keyword")
)

filtered_words = words_df.filter(
    ~col("keyword").isin("the", "to", "in", "after", "new", "and", "of")
)

print("=== Trending Keywords ===")
filtered_words.groupBy("keyword").count().orderBy(col("count").desc()).show()

print("=== Windowed Count by Source ===")
df.groupBy(
    window(col("timestamp"), "5 minutes"),
    col("source")
).count().show(truncate=False)

spark.stop()
