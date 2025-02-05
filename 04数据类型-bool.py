a = True  # 真 条件满足
b = False  #假 条件不满足

#非空为空  可以用来判断一个容器里是否有值 有就为ture 没有就是false
print(bool(""))
print(bool("1111"))

print(bool(()))
print(bool((1)))
print(bool([]))
print(bool([1,2]))
print(bool({}))
print(bool({1,2}))