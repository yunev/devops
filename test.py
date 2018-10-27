df = spark.read.csv("file.csv")
df2 = df.select('a')
