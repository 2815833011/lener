#集合：set.无序不重复通常用于数据去重

a={1,2,3}
b={3,4,5}

#交集
print(a&b,"交集")
#反交集
print(a^b,"反交集")
#并集
print(a|b,"并集")
#差集
print(a-b,"差集")

#内置函数
a.add(4)  #增加元素
print(a)

a.pop()   #删除元素 默认删除集合第一个元素并返回删除的元素
print(a)

a.discard(3)  #指定删除某一个元素
print(a)
