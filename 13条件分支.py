#match case语句
num=int(input("请输入一个数字："))

match num:
    case 100:
        print("数字正确")
    case 0:
        print("错误")
    case _:
        print("默认值")