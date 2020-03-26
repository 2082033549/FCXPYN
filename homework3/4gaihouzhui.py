# 4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.
import os
from os.path import splitext
def gaihouzhui(d,o,ns):
    png=filter(lambda fn:fn.endswith(o),os.listdir(d))
    basefiles=[os.path.splitext(fn)[0] for filename in png]
    for fn in basefiles:
        name1=os.path.join(d,fn+o)
        name2=os.path.join(d,fn+ns)
        os.rename(name1,name2)
        print(1)

gaihouzhui('img','.png','.jpg')