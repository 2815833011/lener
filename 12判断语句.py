#判断
#if/else
#if/elif/...else

right= 100
num=int(input("请输入数字：")) 
if num==right:
    print("猜对了")
elif num> right:
    print("猜大了")
else:
    print("猜小了")

#缩进：代码块的归属条件/语句
if num ==100:
    print("猜对了")
else:
    print("猜错了")

#if嵌套
username= input("请输入账号：")
password= input("请输入密码：")
right_username="admin"
right_password="123456"

if username== right_username:
    if password==right_password:
        print("登录成功！")
    else:
        print("密码错误")
else:
    print("账号错误")


if username==right_username and password== right_password:
    print("登录成功")
else:
    print("登录失败")


num=-1
# flag=None
# if num>0:
#     flag =True
# else:
#     flag=False

flag=True if num>0 else False  #用三元表达式简写 判断语句
print(flag)