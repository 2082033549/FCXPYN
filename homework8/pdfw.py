#2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   #请查资料，Python的 requests库，如何判断一个网址可以访问；
#提示 ：使用requests模块
import threading,re,requests
from multiprocessing.pool import ThreadPool

with open(r"D:\PPython\text1\data11.txt")as f1:
    u1 = f1.readlines()

def ght(url):
    try:        
        r = requests.get(url,timeout = 5)    
        r.raise_for_status()
        print("%s访问成功" %url)
    except:
        print("%s产生异常" %url)

if __name__ == '__main__':
    t = ThreadPool(10)
    for i in range(len(u1)):
        gur = re.compile(r'[a-zA-Z]+://[^\s]*[.com|.cn]')
        ret = re.findall(gur, u1[i])
        for i in range(len(ret)):
            t.apply_async(ght,(ret[i],))
    t.close()
    t.join()