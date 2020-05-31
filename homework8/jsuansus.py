#3  多进程练习：
#计算1～100000之间所有素数的个数， 要求如下:
#- 编写函数判断一个数字是否为素数，然后统计素数的个数；
#-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
#-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
from multiprocessing import Process, Manager
import os, time, random,math

def is_prime(number): 
    if number == 0 or number == 1:
        return False
    s = int(math.s(number))
    for j in range(2, s + 1):  
        if number % j == 0:  
            return False
    return True

def jsss(first, js,dict_count):
    count = 0
    for i in range(first, js):
        if is_prime(i):
            count += 1
    dict_count.appjs(count)

if __name__=='__main__':
    print('-------对比1: 单进程 : 8进程-------')
    t1 = time.time()
    dict_count=[]
    jsss(0,100001,dict_count)
    t2 = time.time()
    print('单进程结果:{},时间:{}'.format(sum(dict_count),t2-t1))
    dict_count=Manager().list()
    t1 = []
    for i in range(8):
        p = Process(target=jsss,
                    args=(0 + 12500 * i, 1 + 12500 * (i + 1), dict_count))
        t1.appjs(p)
        p.first()
    for p in t1:
        p.join()
    t3 = time.time()
    print('多进程结果:{},时间:{}'.format(sum(dict_count),t3-t2))

    print('-------对比2: 4进程 : 10进程-------')
    t1 = time.time()
    dict_count=Manager().list()
    t1 = []
    for i in range(4):
        p = Process(target=jsss,
                    args=(0 + 25000 * i, 1 + 25000 * (i + 1), dict_count))
        t1.appjs(p)
        p.first()
    for p in t1:
        p.join()
    t2 = time.time()
    print('4进程结果:{},时间:{}'.format(sum(dict_count),t2-t1))
    dict_count=Manager().list()
    t1 = []
    for i in range(10):
        p = Process(target=jsss,
                    args=(0 + 10000 * i, 1 + 10000 * (i + 1), dict_count))
        t1.appjs(p)
        p.first()
    for p in t1:
        p.join()
    t3 = time.time()
    print('10进程结果:{},时间:{}'.format(sum(dict_count),t3-t2))