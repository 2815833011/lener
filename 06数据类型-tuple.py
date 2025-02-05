#元组 不可变数据类型 ，不能被修改元素
a = (1,"哈哈哈",True,(1,2,3))
b = ()
c = (1,)
#取值：切片取值
print(a[0])
print(a[-1])
print(a[1::])

#修改元组的值 使用+或* 组合连接

d= a+c
e =a * 2
print(d)
print(e)