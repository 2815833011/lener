# 定义一个名为 GF 的类，用于表示女朋友对象
class GF:
    # 类变量：所有实例共享的变量
    threeD = "不知道"

    # 类方法：使用 @classmethod 装饰器，第一个参数为 cls，表示类本身
    @classmethod
    def eat(cls):
        print("她一顿饭吃一吨")

    # 实例方法：第一个参数为 self，表示实例本身
    def dance(self, wudao):
        # 打印实例对象本身
        print(self)
        # 打印实例的 name 属性
        print(self.name)
        # 打印她会跳的舞蹈名称
        print(f"她会{wudao}")
        # 调用实例的 sing 方法，传入歌曲名称
        self.sing("天天向上")

    # 实例方法：第一个参数为 self，表示实例本身
    def sing(self, ge):
        # 打印实例的 name 属性
        print(self.name)
        # 打印她会唱的歌曲名称
        print(f"她会{ge}")


# 主程序部分
if __name__ == "__main__":
    # 实例化一个 GF 类的对象 gf
    gf = GF()
    # 为实例对象 gf 添加 name 属性并赋值为 "婷婷"
    gf.name = "婷婷"

    # 正确调用类方法 eat，类方法可以通过类名或实例调用
    print("正确调用类方法：")
    GF.eat()
    gf.eat()

    # 访问类变量 threeD
    print(gf.threeD)

    # 正确调用实例方法 dance，传入舞蹈名称 "极乐净土"
    print("正确调用实例方法：")
    gf.dance("极乐净土")

    # 错误调用实例方法示例
    try:
        print("\n错误调用实例方法：尝试通过类名调用实例方法")
        # 错误：实例方法必须通过实例调用，不能直接通过类名调用
        GF.dance("极乐净土")
    except TypeError as e:
        print(f"错误信息：{e}")

    try:
        print("\n错误调用实例方法：未传入足够参数（缺少 self 对应的实例）")
        # 错误：调用实例方法时没有传入实例对象作为第一个参数
        gf.dance()
    except TypeError as e:
        print(f"错误信息：{e}")

    # 错误调用类方法示例
    try:
        print("\n错误调用类方法：传入错误的参数类型（非类本身相关操作）")
        # 错误：类方法第一个参数 cls 代表类本身，不能传入其他不相关的参数
        GF.eat("额外参数")
    except TypeError as e:
        print(f"错误信息：{e}")

    # 更多实例化和操作示例
    # 实例化另一个 GF 类的对象 gf2
    gf2 = GF()
    # 为实例对象 gf2 添加 name 属性并赋值为 "花花"
    gf2.name = "花花"
    # 为实例对象 gf2 添加 age 属性并赋值为 22
    gf2.age = 22
    # 打印实例对象 gf2 的 name 和 age 属性
    print("\n更多实例操作：")
    print(gf2.name, gf2.age)
    # 调用实例方法 dance，传入舞蹈名称 "极乐净土"
    gf2.dance("极乐净土")

    # 关于 self 的说明
    # self 是类实例对象本身，在实例方法中用于访问实例的属性和方法
    gf1 = GF()
    gf1.name = "婷婷"
    gf1.age = 19
    # 调用实例方法 dance，传入舞蹈名称 "两年半"
    gf1.dance("两年半")
    # 调用实例方法 sing，传入歌曲名称 "及你太美"
    gf1.sing("及你太美")

    # 方法调用规则说明
    # 实例方法：必须通过实例调用。
    # 类方法和静态方法：可以通过类名或实例调用。