# Hadoop and Spark envrionment

### The way to fire up your hadoop local hadoop and spark working envrionment in minutes.
```
docker-compose up
```

### To interactive with spark-shell
```
docker exec -it spark-master bash

spark-shell
```

### To read data from spark
```
val data = spark.read.textFile("hdfs://hadoop:8020/data/file.csv")
```

### If you lauch the job from spark worker node
```
spark-shell --master spark://master:7077
```

### To check your spark job status
```
localhost:4040
```
