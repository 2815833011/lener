#字典 （键值对，key：value）
#key :key 不能重复，是唯一，int、str
a={"username":"zhangsan","password":"liss"}
b=dict(((1,2),(1,2)))
print(b)

#取值
print(a["username"])
print(a.get("password")) #用get取值 如果字典中不存在key 不会报错会返回一个空值

#新增
a["age"]=18
a.update(height=190)
a.update({"weight":220})
print(a)

#修改  区别如果字典key存在就修改不存在新增
a["age"]=20
a.update(height=160)
a.update({"weight":80})
print(a)

#删除
v=a.pop("weight")
del a["age"]
print(v)

#常用函数
print(a.keys())  #打印字典列表中所有的key值
print(a.values())#打印字典列表中所有的value值
print(a.items()) #打印字典列表中所有的键值对
a_copy= a.copy()  #复制字典列表
print(a_copy)
a.clear()
print(a,"a现有元素")

