class Father:  #父类
    name="大马"
    money="2000个小目标"
    
    def make_money (self):
        print("超能力")


class Son(Father):  #子类
     name="小马"
     
     def make_money(self):  #重写父类函数
         super().name
         super().make_money()
         print("印钞机")


#子类可以继承父类的变量和函数
son=Son()
print(son.name)
son.make_money()
#子类可以重写父类的变量和函数