#导入
# import 包名
# from 包名.py import 变量/函数/类


#操作系统相关
import os
path=os.getcwd() #当前文件夹
print(path)

# os.makedirs("package")  在当前目录创建文件夹
# os.removedirs("package") 在当前目录删除文件夹

print(os.cpu_count())  #统计计算机cpu数量


# 环境变量
#自带包在%PYTHON_HOME%\Lib
#第三方包在：%PYTHON_HOME%\Lib\site-packages
#python会自动维护一份环境变量，方便快速导入包，实际上是全局变量，list
import sys

print(sys.path) #获取环境变量
# sys.exit(0)  推出执行
args=sys.argv  #获取执行参数
print(args)   
print(sys.getwindowsversion())  #获取Windows 的版本号
print(sys.platform) #获取当前运行的操作系统类型


import random

intput_num=int(input("请输入一个数字："))
number=random.randint(1,100)
if intput_num>number:
    print("大")
else:
    print("小")

input_str="小黑子"
print(random.choice(input_str))


#时间相关：
#time
import time

now=time.localtime()  #获取当前时间
print(now.tm_year)#获取年
print(now.tm_mon)#月
print(now.tm_mday)#日

print(time.time())#时间戳
time.sleep(3) #代码暂停三秒钟


#datetime
from datetime import datetime
now=datetime.now()
print(now)

#指定时间格式
now=now.strftime("%d-%m-%Y")
print(now)

#字符串转换成datetime
day_content="2023-06-13 14:21:15"
now=datetime.strptime(day_content,"%Y-%m-%d %H:%M:%S")
print(type(now),now)

#获取时间戳
print(datetime.now().timestamp())


#json 包
import json
#字典转json
a={"username":"123123123"}
json_a=json.dumps(a)
print(type(json_a),json_a)

#json 转字典
b='{"username":"324234234"}'
dict_b=json.loads(b)
print(type(dict_b),dict_b)


#正则表达式 re 搜索 匹配 替换关键字
import re
text="hello python 2222ll1111"
pattern=r"\d+" #匹配一个或者多个数字
pattern=r"\D+" #匹配非数字
pattern=r"\s+" #匹配空格
pattern=r"\S+" #匹配空格
pattern=r"\W+" #匹配单词
pattern=r"hello*" #匹配前一个字符出现的0次或者无限次
pattern=r"hello+" #匹配前一个字符出现1次或者无限次 至少有1次
pattern=r"h?o" #匹配前一个字符出现1次或者0次 要么有1次 要么有
pattern=r"h{2}" #匹配前一个字符出现m次
pattern=r"2222(.*?)1111" #匹配 前面是2222 后面是1111中间是任意字符


match=re.search(pattern,text)
if match:
    print(match.group())
else:
    print("没有找到")

res= re.findall(pattern,text)
print(res)

# 匹配手机号：13666688888
pattern="1[3-9]\d{9}$"
res=re.search(pattern,"13666688888")
if res:
    print(res.group())
else:
    
    print("没找到")

print(re.findall(pattern,"13666688888"))