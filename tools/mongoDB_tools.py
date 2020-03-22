from pymongo import MongoClient
import pandas as pd
#建立MongoDB数据库连接
client = MongoClient('162.23.167.36',27101)#或MongoClient("mongodb://162.23.167.36:27101/")
#连接所需数据库,testDatabase为数据库名:
db=client.testDatabase
#连接所用集合，也就是我们通常所说的表，testTable为表名
collection=db.testTable