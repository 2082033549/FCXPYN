# 3给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/；  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；要求大家使用Requests库获取这个网页html文本内容，并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
  #Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
import requests
import re
from urllib.parse import quote
from urllib import request

def ght(url):
    header= {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
    response=requests.get(url,headers=header)
    html = response.text
    return html

def gur(html):
    src=r"sc-ad [^\"]*\.mp3"
    mp3 = re.compile(src)
    lst1= re.findall(mp3, html)
    lst1=list(set(lst1))
    for i in range(len(lst1)):
        lst1[i]="http://www.listeningexpress.com/studioclassroom/ad/"+quote(lst1[i])
    for i in lst1:
        print(i)
    return lst1

def xzmp3(lst1):
    path=r"D:\PPython\text1\Mp3.txt"
    a=0
    for url in lst1:
        request.urlretrieve(url, path+"\%s.mp3" %a)
        a=a+1
        print("下载: "+url,"\n")

if __name__=="__main__":
    html=ght("http://www.listeningexpress.com/studioclassroom/ad/")
    lst1=gur(html)
    xzmp3(lst1)
    print("下载成功")