import threading
import requests
from datetime import datetime

url=["https://www.baidu.com","https://www.qq.com","https://cn.bing.com"]

def request(u):
    return requests.get(u)  #requests 请求

start= datetime.now()  #打印当前时间

for u in url:
    request(u)

end=datetime.now()  #遍历请求完了打印当前时间

ones=end-start
print(end-start)



thrds=[]  #线程列表
start= datetime.now()  
for u in url:
   t= threading.Thread(target=request,args=(u,))  #批量创建线程
   t.start()
   thrds.append(t)

for t2 in thrds: #批量结束线程
    t2.join()# 结束线程
    print(t2)

end=datetime.now()

tows=end-start
print(f"单线程：{ones} , 多线程：{tows}")


