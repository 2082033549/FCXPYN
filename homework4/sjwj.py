# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
import random
f = open('ip.txt','w+')
for i in range(1200):
    f.write('172.25.254.' + str(random.randint(1,255))+'\n')
f.seek(0.0)
s = {}
for i in f.readlines():
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
sort_li = list(s.items())
sort = sorted(sort_li,key=lambda x:x[1])[-10:]
for i in sort[::-1]:
    print(i[0],end='')

f.close()
