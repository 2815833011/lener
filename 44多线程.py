import threading
import time

def eat():
    print("开始吃饭")

def cooker(name,s1,s2):
    print(f"正{name}")
    time.sleep(3.0)
    return s1+s2

t1=threading.Thread(target=cooker,args=("煲汤炒菜",1,2)) #创建线程 传入（函数）（函数中需要的参数）
t2=threading.Thread(target=cooker,args=("炒菜",1,2))

#启动线程
t1.start()
t2.start()


#等待线程完成 才执行后续代码
t1.join()
t2.join()
eat()
