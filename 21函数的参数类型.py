#无参数函数
def test():
    print("hahah")

test()

#必填参数的函数
def test2(s1,s2):
    print(s1+s2)
    return s1+s2

test2(1,2)  #少传、多传 都会报错


#关键字传参
print(test2(s2=100,s1=200))


#默认值参数  如果函数参数设有默认值 调用时可以不传参
def test3(s1=20,s2=10):
    print(s1,s2)

test3(s1=80) #如果默认参数传参了就用传递的参数



#1,*:传递任意长度的参数   自动打包成tuple
def test4(*args):
    print(type(args),args)  #<class 'tuple'> (1, 2, 3)

test4(1,2,3)  #传递多个参数 类型为tuple元组



#**: 传递任意长度参数 自动打包成dict
def dtest(**kwargs):
    print(type(kwargs),kwargs)

dtest(s1=100,s2=300,s3=6000) 


def test5(*args,**kwargs):  #可以传递任意类型参数
    print(type(kwargs),kwargs)
    print(type(args),args)


