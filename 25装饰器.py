#装饰器
#函数作为参数传递
def outter(func):
    print(func)
    func()

def test():
    print("我是test")

# outter(test)
print("-------------------------------demo2-------------------------------")

#完整的闭包函数模型
#装饰器函数：不改变原有函数代码的前提下对函数进行功能拓展，日志，鉴权
def outter2(func):

    def inner():
        print("我是inner前")
        func()
        print("我是inner后")
    return inner

#被装饰函数
def test2():
    print("我是test")


test3 = outter2(test2)
test3()

#辨认技巧 
# 函数名后面不带括号表示 将函数作为变量赋值 赋值时声明变量名称并不会调用函数内容
# 函数值后面带括号表示调用函数
print("-------------------------------demo3-------------------------------")

#@装饰器符号使用
@outter2
def test3():
    print("我是test")

test3() #@outter2 加了@拓展函数 会直接通过装饰器调用拓展函数

# test4 = outter2(test3)
# test4()
