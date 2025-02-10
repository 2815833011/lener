class A(object): #python中类会默认继承object
    """
        Aba
    """
    _instance=None

    def __init__(self,name,age):  #初始化函数，实例化类的时候需要做对应的传参
        self.name=name 
        self.aeg=age

#构造函数：控制实例产生的过程:__new__产生实例对象 >再调用__init__做实例对象的初始化 
# new函数自动把参数传给init所以参数要保持一致
    def __new__(cls,name,age): 
       a= super().__new__(cls)
       print(a)

       if  not cls._instance:
           cls._instance=super().__new__(cls)
       
       return cls._instance

#__setattr__设置实例变量时会自动调用
    def __setattr__(self, name, value):
        if len(str(value))>0 and len(str(value))<4:
            super().__setattr__(name,value)
        else :
            raise Exception("数据类型长度不满足")
    
    #__delattr__删除实例变量时会自动调用
    def __delattr__(self, name):
        print(f"删除了变量{name}")
        super().__delattr__(name)
        
    #判断self==XXX会自动调用
    def __eq__(self, value):
        if value ==123:
            return True
        return False
    
    #判断 #判断self!=XXX会自动调用
    def __ne__(self, value):
        if value ==123:
            return True
        return False

#魔术函数：一般是由object继承得来的
print(A.__doc__)
print(A.__dict__)


#只有直接运行当前文件这个条件才成立，被其他文件导入则不成立 ，一般用来调试代码
if __name__ =="__main__":
    print("当前文件36")
    # print(A().__class__)  #获取类名

    a=A("张三",18)
    print(a.aeg,a.name)

    a=A("张三",18)
    b=A("张三",19)
    print(id(a))
    print(id(b))
    del a.aeg
    print(a.__dict__)  #查看对象属性

    print(a==123)