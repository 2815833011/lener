#使用文件夹管理py文件
#python3.3以前 文件夹想要有一个特殊文件 __init__.py 标识文件夹是包

# import package  #导入自定义包

# print(package.name)
# package.test_name()

# from package.test import a   #导入自定义包非 init文件的 变量 函数 类
# from package.test import test_m 
# from package.test import TestClass

# print(a)
# test_m()
# TestClass()


#不包含包的导入：两个文件夹在同一个文件夹下
#from xxx import name ,test_m

#导入文件夹下所有 不推荐使用
# from package.test import *

#给导入的参数起别名
# from package.test import TestClass as TC
# TC()


# 不同文件夹下的导入  跨文件夹导入
import os
import sys

sys.path.append(os.getcwd()) #将当前项目路径添加到环境变量中
from package1 import test1


