#list :列表，list 元组可以被修改 tuple元素不能被修改
a=[1,2,3,"哈哈哈",(1,2,3),[1,2,3]]

#取值：切片
print(a[0])
print(a[::-1])

# 新增
a.append("哥哥") #在结尾新增
a.insert(1,"没礼貌") #在指定位置插入元素 1号下标的后面插入

#修改
a[0]="耗子为止"  #可通过下标直接修改列表元素

#删除
a.remove("哈哈哈") #指定删除列表中的元素
a.clear() #清除所有列表元素
del a  #删除整个列表函数


#常用函数
a =[11,22,33]
a.sort()  #排序
print(a)
a.sort(reverse=True) #从升序或者降序 True/false
print(a)

num = a.pop(-1)  #根据索引删除列表中的元素 并返回删除元素
print(num,a)
print(a.count(333))  #count 查找列表元素的数量
a_copy=a.copy()      #复制列表
print(a)

print(len(a))  # 通过；内置函数获取列表长度
print(min(a))   # 通过；内置函数获取列表中最小值
print(max(a))   # 通过；内置函数获取列表中最大值