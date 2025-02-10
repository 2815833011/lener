class A :
    name="a"
    def test(self):
        print("a的test")

class B:
    name="b"
    def test(self):
        print("b的test")

class C(A,B):
    def test(self):
        print(C.mro())  #[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>] 多继承顺序
        super(A,self).test()
        print(super(A,self).name)

c=C()
c.test()


#多继承中想调用目标类中的参数 必须得传出继承顺序的上一位才能调用