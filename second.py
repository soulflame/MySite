import os, sys
#
# if __name__ == "__main__":
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MySite.settings')
#     django.setup()
#
# from app01 import models
# class Meta:
#     db_table = ""
import redis
import random
from concurrent.futures import ThreadPoolExecutor


pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    password='8877',
    db=0,
    max_connections=20,

)

con = redis.Redis(connection_pool=pool)

# con.sadd('employee',8001,8002,8003)
# con.srem('employee',8002)
# res = con.smembers('employee')
# for item in res:
#     print(item.decode('utf-8'))

# con.hmset("9527", {"name": "Daryl", "gender": "male", "age": "30"})
# con.hset("9527","city","纽约")
# res = con.hgetall("9527")
# for item in res:
#     print(item.decode('utf-8'),res[item].decode('utf-8'))

# pipline = con.pipeline()
# pipline.watch('9527')
# pipline.multi()
# pipline.hset('9527','name','Jack')
# pipline.hset('9527','age',23)
# pipline.execute()
#
# if 'pipline' in dir():
#     pipline.reset()

# con.zadd('vote', {'马云': 0, '丁磊': 0, '张朝阳': 0, '马化腾': 0, '李彦宏': 0})
# name_list = ['马云','丁磊','张朝阳','马化腾','李彦宏']
# for i in range(0,300):
#     num = random.randint(0,4)
#     name = name_list[num]
#     con.zincrby('vote',1,name)
# res = con.zrevrange('vote',0,-1,'withscores')
# for item in res:
#     print(item[0].decode('utf-8'),int(item[1]))


s =set()
while 1:
    if len(s)==1000:
        break
    num = random.randint(10000,100000)
    s.add(num)

con.delete('kill_total','kill_num','kill_flag','kill_user')
con.set("kill_total",50)
con.set("kill_num",0)
con.set("kill_flag",1)
con.expire("kill_flag",600)

executor = ThreadPoolExecutor(200)
def buy():
    connection = redis.Redis(
        connection_pool=pool
    )
    pipline = connection.pipeline()
    if connection.exists('kill_flag') == 1:
        pipline.watch("kill_num","kill_user")
        total = int(pipline.get('kill_total').decode('utf-8'))
        num = int(pipline.get('kill_num').decode('utf-8'))
        if num<total:
            pipline.multi()
            pipline.incr("kill_num")
            user_id = s.pop()
            pipline.rpush("kill_user",user_id)
            pipline.execute()
    if "pipline" in dir():
        pipline.reset()
    del connection

for i in range(0,1000):
    executor.submit(buy)
print("秒杀结束")






