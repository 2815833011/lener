#带参数的装饰器
def aaa(num): #第一层函数用来接收装饰器传参
    print(num)
    def outter(fun): # 第二层函数接收 函数 tset
        print(num)
        def inner(*args,**kwargs):  #第三层 直接调用 被装饰函数
            print(num)  #闭包函数中子函数可以使用父函数的参数
            print("前")
            fun(*args,**kwargs)
            print("后")
        return inner
    return outter

@aaa(10)
def test(name):
    print(f"{name}")

test("Tony") #调用这个被装饰函数实际上是启用装装饰器@aaa(10)

#调用装饰器函数逻辑
# @aaa(10)===>@outter(Test)====>inner()====>test()