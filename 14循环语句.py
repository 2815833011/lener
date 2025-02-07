#for:遍历list/tuple/str/dict/set  循环取出每个元素 并且执行for循环语句
# debug:调试模式 允许达断点 程序执行到断点可以自定暂停运行
# content="今天星期五"
# content=("1","2","哈哈哈")
# content=["1","2","哈哈哈"]
content={"1","2","哈哈哈"}  #无序不重复的集合 他的元素会自动去重
for c in content :  #便利字符串中的每一个元素
    print(c)

#遍历字典
a={"username":"张三","password":"李四"}
for i in a:
    print(a.get(i))

for k,v in a.items():  #遍历字典用 items 键值对  分别取出key和value
    print(k,v)

for k in a.keys():     #只便利key
    print(k)
for v in a.values():     #只便利value
    print(v)