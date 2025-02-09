#类变量和类函数
class Person:
    #类变量
    name="gege"

    # 类函数
    @classmethod
    def eat(cls,*args,**kwargs):
        print(cls)
        print(cls.name)
        cls.run()
        print("我是类函数eat")
        return args
    
    @classmethod
    def run(cls):
        print("我是函数run")

print(Person.name)
Person.name="小黑子"
print(Person.name)
Person.fav="篮球"
print(Person.fav)
Person.eat()

# 调用类变量
print(f"Person名字是{Person}")
args=Person.eat("哈哈哈哈哈")
print(args)