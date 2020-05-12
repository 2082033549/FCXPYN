# 1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#    提示，文件有1000行，注意控制每次读取的行数；
import os
import re

def main():
    p1=r'D:\PPython\text1\webspiderUrl.txt'
    p2=r'D:\PPython\text1\w2.txt'
    with open(p1,'r',encoding='utf-8') as f1:
        with open(p2,'w',encoding='utf-8') as f2:
            while True:
                a1=f1.readline()
                src=r'http://[^\';]*' 
                i=re.compile(src)  
                list1=re.findall(i,a1)  
                for a in list1:
                    f2.write(a)
                    f2.write('\n')
if __name__=='__main__':
    main()