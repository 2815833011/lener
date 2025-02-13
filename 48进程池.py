import multiprocessing
from multiprocessing import Pool

def square(number):
    print(number*number,f"{number},{number}")
    return number*number

if __name__=="__main__":
    nums=[188,992,6678,2293,6652,7788,9911,220,23,222]
    with Pool() as pool:
            pool.map(square,nums) #跑任务


    pool.join() #等待所有任务完成
    

        # pool.close() #关闭进程，不让添加新任务了