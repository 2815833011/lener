
C=int(input("现在多少度"))
F=C*9/5+32
print(f"现在是华氏{F}")


def test():
    num=int(input("请输入一个数字："))    
    if num%2==0:
        if num%4==0:
            print("通过")
        else:
            test()
    else :
        test()

test()