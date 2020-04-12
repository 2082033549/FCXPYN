# 6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
import os
from datetime import datetime
path= r"F:\PyCharm 2019.3.3\plugins"
fandd=os.listdir(path)
for i in fandd:
    file=os.path.join( r"F:\PyCharm 2019.3.3\plugins",i)
    if os.path.isfile(file):#文件存在
        print("{},{},{}".format(i,datetime.fromtimestamp(os.path.getmtime(file)),"文件"))
    else:
        print("{},{},{}".format(i,datetime.fromtimestamp(os.path.getmtime(file)),"文件夹"))