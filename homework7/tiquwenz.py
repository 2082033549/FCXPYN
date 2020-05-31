# 4爬取这个网址上https://www.programcreek.com/python/，搜索request的范例代码；保存到txt文件中（只保留文字）；
from bs4 import BeautifulSoup
import requests
import re
import os

url='https://www.programcreek.com/python/example/3765/requests.get'

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"
}

r=requests.get(url,headers=headers).content.decode('utf-8')
s=BeautifulSoup(r,'html.parser')
rul=s.find(class_='nav__items')
rea=rul.find_all('a')
list1=[]
for i in rea:
	list1.append(i.attrs['href'])

w1=r'D:\PPython\text1\request111.txt'
with open(os.w1.join(w1,'prc-python.txt'),'w',encoding='utf-8')as f1:
	for i in list1:
		
		test1 = requests.get(i, headers=headers).content.decode('utf-8')
		st = BeautifulSoup(test1, 'html.parser')
		title = st.find(class_='page__inner-wrap').find('header').text
		f1.write('*****************************************************************\n'+title.strip()+'\n')
		content = st.find(class_='content').text.strip()
		f1.write(content+'\n')
