import multiprocessing

def kitchen(name,food):
    print(f"厨房{name}正在做{food}")


if __name__ == '__main__':  #window 系统下多进程必须加这个不然会报错
    process=[] #进程列表
    kitchen_work=[["a","煲汤"],["b","煲汤"],["c","螺蛳粉"]]
    for p in kitchen_work:
        p=multiprocessing.Process(target=kitchen,args=(p[0],p[1]))  #批量创建进程
        process.append(p)
        p.start()

    for p in process:
        print(p)
        p.join()

    print("吃饭罗！")