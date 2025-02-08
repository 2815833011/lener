
sum11=1000
def sum(s1,s2):
    sum=s1+s2   
    print(sum)
    print(sum11)


sum(1,2)

#local>enclosing >globals >build-in

name ="张三"
def test():
    # global name  #声明全局变量
    name ="李四"

test()
print(name)

globals()["tset"]="1111"   #内置的全局字典
print(globals())

# nonlocal: 内部函数修改外部函数的变量
def outter():
    c=1000
    def inner():
        nonlocal c
        c=10
        print(c)
    return inner
    

outter()