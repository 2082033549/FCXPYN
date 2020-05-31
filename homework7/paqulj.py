# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库
import os
import requests
from bs4 import BeautifulSoup
import re

w1=r'D:\PPython\text1\webspiderUrl.txt'
list1=[]
with open(w1,'r',encoding='utf-8')as f1:
    while 1:
        text1=f1.readline().strip().strip()
        if not text1:
            break
        list1.append(text1)
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
list2 = []
for url in list1:

    text2=requests.get(url,headers=headers).content.decode('utf-8')

else:
    soup=BeautifulSoup(text2,'html.parser')
    target=soup.find_all('a',text2=re.compile(r'关于我们|企业介绍|企业发展|历史|概况'))
    for q in target:
        
            p=q.attrs['href']
    else:
            list2.append(p)

for e in list2:
    print(e)