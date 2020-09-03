from django.test import TestCase
from pypinyin import lazy_pinyin
# Create your tests here.

import pymysql

db = pymysql.connect(
         host='localhost',
         port=3306,
         user='root',
         passwd='8877',
         db ='text',
         charset='utf8'
         )

cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)
cursor.execute("select * from employee")
data1 = cursor.fetchall()
print(data1)
# 关闭数据库连接
db.close()






