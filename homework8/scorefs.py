# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
import threading, random, time
from multiprocessing.pool import ThreadPool
a = 1
mutex = threading.Lock()

class Scorethread( threading.Thread ):

    def run( self ):
        global a
        for i in range(20):
            mutex.acquire()
            score = random.randint( 0, 101 )
            print( '%s is running: 学号为%s的学生的分数为: %s.' %( self.name, a, score ) )
            a += 1
            mutex.release()
            time.sleep( 1 )

def test():
    for i in range(5):
        t = Scorethread()
        t.start()

if __name__ == "__main__":
    test()

def run(b):
    score = random.randint( 0, 100 )
    print( '学生{}的分数为: {}.'.format(b,score))
    b+=10
    time.sleep(1)

if __name__ == '__main__':
    t = ThreadPool(10)
    for i in range(100):
        t.apply_async(run,(i+1,))
    t.close()
    t.join()