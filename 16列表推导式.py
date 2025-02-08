#列表推导式可以使用for+if的语句来快速生成满足条件的列表
a=[i for i in range(10)]
print(type(a),a)

a=[i for i in range(10) if i%2!=0]
print(type(a),a)

a=(x for x in range(10))
print(type(a),a)
