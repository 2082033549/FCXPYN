# 5  通过Python来模拟实现一个txt文件的拷贝过程;
import os

def copy(path,path1):                     
    f1= open(path,'r')
    f2= open(path1,'w')
    for i in f1:
        f2.write(i)                      
    f1.close()
    f2.close()

copy("G:/test/text.txt","F:/test/text1.txt")
