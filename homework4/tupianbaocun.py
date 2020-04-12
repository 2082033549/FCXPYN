#   9 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）
import pip._vendor.requests
import os
from pip._vendor import requests
url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E4%BB%8E%E7%BD%91%E7%BB%9C%E4%B8%8A%E4%B8%8B%E8%BD%BD%E4%B8%80%E5%BC%A0%E5%9B%BE%E7%89%87%2C%E4%BF%9D%E5%AD%98%E5%88%B0%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%9A%84%E6%8C%87%E5%AE%9A%E7%9B%AE%E5%BD%95%3B(requests%E5%92%8Cos%E6%A8%A1%E5%9D%97)&step_word=&hs=0&pn=11&spn=0&di=550&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=2623115107%2C3239182610&os=2079193415%2C1656469513&simid=4290380260%2C716436797&adpicid=0&lpn=0&ln=259&fr=&fmq=1586671290208_R&fm=&ic=undefined&s=undefined&hd=undefined&latest=undefined&copyright=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimage.bubuko.com%2Finfo%2F201804%2F20180407164956034872.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3F3twghwg2_z%26e3Bxhyg_z%26e3Bv54AzdH3Fkwthj-uuk26pj2kje1e6k6u1_z%26e3Bip4&gsm=e&rpstart=0&rpnum=0&islist=&querylist=&force=undefined"#图片网址
d='D:\\B\\'
path=d+url.split('/')[-1]
try:
    if not os.path.exists(d):
        os.mkdir(d)
    if not os.path.exists(path):
        r=requests.get(url)
        r.raise_for_status()
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("图片保存成功")
    else:      
        print("图片已存在")
except:
    print("图片获取失败")