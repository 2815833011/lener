# 定义类 A，在 Python 中，类默认继承 object
class A(object):
    """
        Aba
    """
    # 类属性，用于实现单例模式，存储类的唯一实例
    _instance = None

    # 初始化函数，在实例化类时自动调用，用于对实例对象进行初始化
    # 参数 name 和 age 分别用于设置实例的姓名和年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age


    # 构造函数，控制实例产生的过程，先于 __init__ 调用
    # __new__ 产生实例对象，然后再调用 __init__ 做实例对象的初始化
    # 参数需要与 __init__ 保持一致
    def __new__(cls, name, age):
        # 创建一个新的实例对象
        a = super().__new__(cls)
        print(a)
        # 实现单例模式，如果 _instance 为空，则创建一个新的实例对象并赋值给 _instance
        if not cls._instance:
            cls._instance = super().__new__(cls)
        # 返回类的唯一实例
        return cls._instance
    

    # 解构函数，在实例对象被销毁时自动调用
    # 例如 Python 程序运行完成或者手动使用 del 语句删除实例对象时会触发
    def __del__(self):
        pass


    # __setattr__，在设置实例变量时自动调用
    # 参数 name 是变量名，value 是变量的值
    def __setattr__(self, name, value):
        # 检查变量值的长度是否在 1 到 3 之间
        if len(str(value)) > 0 and len(str(value)) < 4:
            # 调用父类的 __setattr__ 方法设置变量
            super().__setattr__(name, value)
        else:
            # 如果长度不满足条件，抛出异常
            raise Exception("数据类型长度不满足")
        

    # __delattr__，在删除实例变量时自动调用
    # 参数 name 是要删除的变量名
    def __delattr__(self, name):
        print(f"删除了变量{name}")
        # 调用父类的 __delattr__ 方法删除变量
        super().__delattr__(name)


    # __eq__，在判断 self == xxx 时自动调用
    # 参数 value 是比较的值
    def __eq__(self, value):
        if value == 123:
            return True
        return False
    

    # __ne__，在判断 self != xxx 时自动调用
    # 参数 value 是比较的值
    def __ne__(self, value):
        if value == 123:
            return True
        return False
    

    # __str__，在打印类对象时调用，返回一个可读性较好的字符串表示
    def __str__(self):
        return "我们是A对象__str__"
    

    # __repr__，在打印类对象时调用，通常用于调试，返回一个更准确的字符串表示
    # 当 __str__ 和 __repr__ 同时存在时，print() 函数优先调用 __str__
    def __repr__(self):
        return "我是__repr__"
    

    # __call__，当实例对象像函数一样被调用时自动调用
    def __call__(self, *args, **kwds):
        return "我被调用了"
    

    # __iter__，将普通对象设置为可迭代对象，返回一个迭代器
    def __iter__(self):
        return iter([1, 2, 3, 4])
    

    # __ge__，在判断 self >= xxx 时自动调用
    # 参数 value 是比较的值
    def __ge__(self, value):
        return True
    

    # __gt__，在判断 self > xxx 时自动调用
    # 参数 value 是比较的值
    def __gt__(self, value):
        return True
    

    # __le__，在判断 self <= xxx 时自动调用
    # 参数 value 是比较的值
    def __le__(self, value):
        return False
    

    # __lt__，在判断 self < xxx 时自动调用
    # 参数 value 是比较的值
    def __lt__(self, value):
        return False
    

    # __add__，在计算 self + xxx 时调用
    # 参数 _value 是相加的值
    def __add__(self, _value):
        pass


    # __sub__，在计算 self - xxx 时调用
    # 参数 _value 是相减的值
    def __sub__(self, _value):
        pass


    # __len__，在调用 len(self) 时调用
    def __len__(self):
        pass


# 打印类的文档字符串
print(A.__doc__)

# 打印类的属性字典
print(A.__dict__)

# 只有直接运行当前文件这个条件才成立，被其他文件导入则不成立，一般用来调试代码
if __name__ == "__main__":
    print("当前文件代码开始执行")
    # 实例化 A 类
    a = A("张三", 18)

    # 打印实例的 age 和 name 属性
    print(a.age, a.name)

    # 再次实例化 A 类，由于使用了单例模式，a 和 b 指向同一个实例
    a = A("张三", 18)
    b = A("张三", 19)

    # 打印实例 a 的内存地址
    print(id(a))

    # 打印实例 b 的内存地址
    print(id(b))

    # 删除实例 a 的 age 属性
    del a.age

    # 查看实例 a 的属性字典
    print(a.__dict__)

    # 判断实例 a 是否等于 123
    print(a == 123)

    # 测试 __str__ 方法
    print(str(a))

    # 测试 __repr__ 方法
    print(repr(a))

    # 测试 __call__ 方法
    print(a())

    # 测试 __iter__ 方法
    for i in a:
        print(i)

    # 测试 __ge__ 方法
    print(a >= 10)

    # 测试 __gt__ 方法
    print(a > 10)
    
    # 测试 __le__ 方法
    print(a <= 10)

    # 测试 __lt__ 方法
    print(a < 10)

    # 测试 __add__ 方法
    try:
        result = a + 10
        print(result)
    except TypeError:
        print("__add__ 方法未实现具体逻辑")

    # 测试 __sub__ 方法
    try:
        result = a - 10
        print(result)
    except TypeError:
        print("__sub__ 方法未实现具体逻辑")
        
    # 测试 __len__ 方法
    try:
        length = len(a)
        print(length)
    except TypeError:
        print("__len__ 方法未实现具体逻辑")