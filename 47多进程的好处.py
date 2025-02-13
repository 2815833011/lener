import multiprocessing
import requests
from datetime import datetime


url=["https://www.baidu.com","https://www.qq.com","https://cn.bing.com"]

def request(u):
    return requests.get(u)  #requests 请求


if __name__ == '__main__':  #window 系统下多进程必须加这个不然会报错
    process=[] #进程列表

    star=datetime.now()
    for p in url:
        p=multiprocessing.Process(target=request,args=(p,))  #批量创建进程
        process.append(p)
        p.start()
    end=datetime.now()
    for p in process:
        print(p)
        p.join()

    print(end-star)