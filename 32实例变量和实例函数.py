class GF:
    #类变量
    threeD="不知道"
    #类函数
    @classmethod
    def eat(cls):
        print("她一顿饭吃一吨")
    
    #实例函数
    def dance(self,wudao):
        print(self)
        print(self.name)
        print(f"她会{wudao}")  
        self.sing("天天向上")

    def sing(self,ge): 
        print(self.name)
        print(f"她会{ge}")


gf=GF()
gf.name="婷婷"
gf.eat()
print(gf.threeD)
gf.dance("极乐净土")
# #实例化对象
# gf=GF()
# gf2=GF()
# print(gf)
# print(gf2)


# #实例变量
# gf.name="婷婷"
# gf.age=18
# print(gf.name,gf.age)
# gf.age=80
# print(gf.name,gf.age)
# gf.dance("广场舞")



# gf2.name="花花"
# gf2.age=22
# print(gf2.name,gf2.age)
# gf2.dance("极乐净土")

#self 是类对象本身
# gf1=GF()
# gf1.name="婷婷"
# gf1.age=19
# gf1.dance("两年半")
# gf1.sing("及你太美")


# 实例方法：必须通过实例调用。

# 类方法和静态方法：可以通过类名或实例调用。