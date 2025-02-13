import traceback #第三方的包获取完整异常


a=[1,2,3]

#使用场景：调用第三方包，不是自己的代码的时候

try:  #这里代码报错
    print(a[10])
except Exception as e:  #报错代码异常

    traceback.print_exc() #打印在终端
    e=traceback.format_exc()

    print(e)  #处理异常 打印异常
    print(2) 
else:  #没有报错就执行这里的代码
    print(3)
finally:  #有没有报错都会执行
    print(4)

#异常处理，当代码报错时，不想要代码退出执行 try/except/else/finnay

#自定义异常
class MyException(Exception):
    pass

#主动抛出异常
try:
    raise MyException("hhhhh")
except :
    traceback.print_exc()