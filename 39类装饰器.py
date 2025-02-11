
#类装饰器其实相当于重写__call__
class Logger:
    def __init__(self,func):
        self.func=func
    
    def __call__(self, *args, **kwds):
        print("开始记录日志")
        res=self.func(*args,**kwds)
        print("这里打印返回值")
        return res
    
@Logger
def demo():
    print("adfaeasdf")
# demo=Logger(demo)

demo()