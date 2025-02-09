#可迭代对象
a="哈哈哈"
a=[1,2,3,23]
a={1,2,3,23}
a=(1,2,3,23)
a={"u":"p"}
a=(x for x in range(10))
a=range(10)
print(dir(a))
#必须包含 __iter__ ,__next__ 才是可迭代对象

#创建迭代器
a="哈哈哈"
a=(1,2,23)
a={1,2,23}
a=[1,2,23]
a={"u":"p"}
a=range(10)
it=iter(a) #加入iter方法他就转换成一个可迭代类型 
print(dir(it))
print(next(it))

#访问元素的一种方式，迭代器只能往前不能往后退

