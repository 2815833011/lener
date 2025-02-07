content={"1","2","哈哈哈"}
for index,v in enumerate(content):  #取出列表下标
    print(index,v)

# range函数来快速遍历数组：序列产生器，快速产生数组
for i in range(10):
    print(i,"1")

for i in range(0,10,1):
    print(i,"2")

for i in range(0,10,2):
    print(i,"3")

for i in range(10):
    print(i)
else:
    print("完成")

#计算1000内所有偶数的和
sum=0
for i in range(0,1000,2):
    sum=sum+i
print(sum)

#for嵌套，九九乘法表
for i in range(1,10):
    for u in range(1,i+1):
        print(f"{u}x{i}={u*i}",end="\t")
    print("","\n")
        

#冒泡排序 两个相邻的数字两两比较
a=[100,2,-1,0,3]
# 0  4
# 1  3
# 2  2
# 3  1
num=0
for i in range(len(a)-1):  #控制论数 共四轮
    for u in range(len(a)-1-i):  #控制次数=n-1  4，3，2，1
        if a[u]>a[u+1]:
            b=a[u]
            a[u]=a[u+1]
            a[u+1]=b
        num=num+1
print(a,num)
        