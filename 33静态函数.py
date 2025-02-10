class Person:
    
    @staticmethod
    def eat(food,food2):
        print(food,food2)
        return True

res=Person.eat("菠菜","西兰花")
print(res)