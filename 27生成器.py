def test():
    print("我是test")
    return 111

print(test())


def gen_test():
    print("我是gen_test")
    yield "hahaha"
    print("我是yield后面的代码")
    yield "hahaha"
    print("我是呵呵呵")

# gen=gen_test()
# print(next(gen))
# print(next(gen))
# print(next(gen))  #StopIteration 生成器执行完毕

#生成器和函数的区别
#return: 函数一次性执行完，并且执行到return 会终止代码运行，在函数体中return只有一个
#yield ：调用生成器并不会立刻执行，需要使用next 函数手动调用生成器
#yield 是分段执行 调用一次next执行一次yield，并且生成器会暂定卡住等待继续执行

gen=(x for x in range(10))
print(type(),gen)
print(next(gen))
