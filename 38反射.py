class A:
    name="niubi"

    @classmethod
    def class_m(cls):
        print("类函数")

    
    def __init__(self):
        self.age=18

    
    def test(self):
        print("哈哈哈")
    
print(A.name)  #调用类变量
A.class_m()     #调用类函数
a=A()   #实例化对象A
print(a.age) #调用实例对象a 的实例函数


#通过反射获取 类变量 类函数
a_name=getattr(A,"name")
a_class_m=getattr(A,"class_m")
print(a_name)
a_class_m()

#通过反射获取 实例变量 实例函数
sel=getattr(a,"age")
sel_test=getattr(a,"test")
print(sel)
sel_test()

# hasattr（） 判断类中是否包含这个 变量 或者函数

print(hasattr(A,"name")) #会返回一个bool值
print(hasattr(a,"age"))


#设置setattr() 设置 类变量 实例变量
setattr(A,"height",18)
setattr(a,"weight",18)
print(A.height,a.weight)

#删除
delattr(A,"height")
delattr(a,"weight")
print(hasattr(A,"height")) #会返回一个bool值
print(hasattr(a,"weight"))

# 反射函数
def test():
    a=100
    print(a)
    def bbb():
        pass
    print(locals())

a1=globals().get("test")
res=a1()
print(res.get("a"))
print(res.get("bbb"))

