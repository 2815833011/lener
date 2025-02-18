def test(s1=100):
    print(s1)
    if s1<1:
        return 1
    else:
        s1-=1  #自减
        test(s1)  #递归函数内部再次调用

test()