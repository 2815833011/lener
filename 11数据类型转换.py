#int/str/float
a=1
b=1.0
c="18"
print(type(a),type(b),type(c))
a1=float(a)
a2=str(a)
print(type(a1),a1,type(a2),a2)
b1=int(b)
b2=str(b)
print(type(b1),b1,type(b2),b2)
c1=int(c)
c2=float(c)
print(type(c1),c1,type(c2),c2)

#tuple/set/list
a=(1,2,3)
b={1,2,3}
c=[1,2,3]
print(type(a),type(b),type(c))
a1=set(a)
a2=list(a)
print(type(a1),a1,type(a2),a2)
b1=tuple(b)
b2=list(b)
print(type(b1),b1,type(b2),b2)
c1=tuple(c)
c2=set(c)
print(type(c1),c1,type(c2),c2)

#eval 内置函数：根据字符串数据内容的数据格式进行动态转换
a="1"
b="1.0"
c="True"
d="None"
e="(1,2,3)"
f="{1,2,3}"
g="[1,2,3]"
h="{'u':'zs','p':'123'}"

print(type(a),type(b),type(c),type(d),type(e),type(f),type(g),type(h))
a1=eval(a)
b1=eval(b)
c1=eval(c)
d1=eval(d)
e1=eval(e)
f1=eval(f)
g1=eval(g)
h1=eval(h)
print(type(a1),type(b1),type(c1),type(d1),type(e1),type(f1),type(g1),type(h1))

#思考
h2=eval(h1)
k2=eval(h2)
print(type(k2),k2) #报错eval() arg 1 must be a string, bytes or code object