# 1  编写一个装饰器，能计算其他函数的运行时间；
import time
def sj(func):
    def sj1(*args, **kwargs):
        kssj= time.time()
        func(*args, **kwargs)
        jssj= time.time()
        print('程序用时：%s秒' % int(jssj - kssj))
    return sj1

@sj
def test():
    sum = 0
    a=1
    return 1
test()