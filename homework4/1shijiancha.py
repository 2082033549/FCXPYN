# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#     提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
import time
from collections import deque
list1=list(range(10))
fisttime=time.time()
list1.insert(0,20)
list1.append(11)
finalltime=time.time()
consumetime=finalltime-fisttime#运行时间
print("第一个耗费时间是%d" % consumetime)
list2= deque([1,2,3,4,5,6,7,8,9,10])
statetime=time.time()
list2.append('x')
list2.appendleft('y')
endtime=time.time()
dtime=statetime-endtime
print("第二个耗费时间是%d" % dtime)
chazhi=consumetime-dtime
print("差值是%d" % chazhi)

