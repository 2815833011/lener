#私有函数/变量

class Test:
    __name="哈哈哈哈"  #私有变量

    def __test(self):  #私有函数
        print("test")

    def aaa(self):
        print("aaa")

class Test2(Test):
    pass

# Test().__test()  AttributeError: 'Test' object has no attribute '__test'
# print(Test().__name)  AttributeError: 'Test' object has no attribute '__name'

#父类的私有函数变量不能在外部调用
print(Test2().__name)  
Test2().__test()