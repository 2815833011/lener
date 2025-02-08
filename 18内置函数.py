# print("哈哈哈哈")
# input("请输入名称：")
# print(id("哈哈哈"))
# print(type("hhh"))
#len: 获取字符串、元组、列表、；字典、集合 的长度，元组个数
a="哈哈哈哈"
a=("哈哈哈哈")
a=["哈哈哈哈"]
a={"哈哈哈哈"}
a={"哈哈哈哈":"111"}
print(len(a))
print(len(a))
print(len(a))
print(len(a))

#max：最大值
a=[1,100,2,3]
print(max(a))

#min：最小值
print(min(a))

#sum：求和
print(sum(a))

#eval :根据字符中的数据类型自动转换

#ABS: 获取绝对值
print(abs(-6))

# zip:  合并列表
a=[1,2,3]
b=["星","期","五"]
obj=zip(a,b)
print(type(obj),obj)