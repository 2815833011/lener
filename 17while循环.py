# while :是用在不知道执行多少次的情况
# for 是用在有限循环中

# num= 20
# while num<100:
#     print(num)
#     num-=1  #自检
#     num+=1 #自增

num=10
while num>0 :
    print(num)
    num -=1
else:
    print("退出")

# while True:
#     print("ok") #死循环

# break: 结束循环
# continue: 跳过本次循环

while True:
    print("ok") #死循环
    break

for i in range(10):
    if i%2==0:
        continue
    print(i)
