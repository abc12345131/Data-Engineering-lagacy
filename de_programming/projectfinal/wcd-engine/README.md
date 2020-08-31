To submit file on your local machine
```
bin/spark-submit --class Driver.MainApp --conf spark.ui.port=5000 --master local file:///Users/edwinguo/edwin/watergun/target/scala-2.11/watergun_2.11-1.0.jar -p wcd-demo -i Csv -o parquet -s </dir/spark-2.4.3-bin-hadoop2.7/python/test_support/sql/ages.csv> -d <output-path> -m append -c name --input-options header=true
```
