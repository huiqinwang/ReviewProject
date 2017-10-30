#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-13 下午2:42
# @Author  : huiqin
# @File    : SQLContext.py
# @Description : Class is for
from pyspark import SparkConf,SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext,Row

conf = SparkConf().setAppName("spark_sql_test")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
hiveContext = HiveContext(sc)

datas = ['1 a 28','2 b 29','3 c 30']
source = sc.parallelize(datas)
splits = source.map(lambda line:line.split(" "))
rows = splits.map(lambda words:Row(id = words[0],name=words[1],age=words[2]))
people = hiveContext
people.printScheme()
people.registerTempTable("people")

results = hiveContext.sql("select * from people where age > 28 and age < 30")
results.registerTempTable("people2")
results2 = hiveContext.sql("select name from people2")
results2.printSchema()

results3 = results2.map(lambda row:row.name.upper()).collect()
for result in results3:
    print("name:",result)
sc.stop()
