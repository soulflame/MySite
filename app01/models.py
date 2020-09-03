from django.db import models

# Create your models here.


import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "8877", "text")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
try:

    cursor.execute(sql)  # 执行SQL语句
    results = cursor.fetchall()  # 获取所有记录列表
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()






















