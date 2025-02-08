
# 闭包函数

def outter():
    sum=100
    
    def inner():
        print(sum)
    return inner


print(outter())  #不能直接调用外部函数 打印结果： <function outter.<locals>.inner at 0x000001E822ADE830>
a=outter()  #a =inner 将内部函数赋值给a
a()         # a= inner   a() ==> inner()  调用内部函数inner



