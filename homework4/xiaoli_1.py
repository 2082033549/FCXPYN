# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
# from datetime import datetime
# import time
# dt= datetime.date(2019, 5, 9) # 用指定日期时间创建datetime
# a=dt.isocalender()
# print(a)
# import datetime
# a=datetime.date(2017, 12, 31).isocalendar()
# print(a)
import datetime
def riqi(year,month,date):
    print(year,month,date,year,datetime.date(year,month,date).isocalendar()[1],datetime.date(year,month,date).isocalendar()[2])
def xiaoli(year,month,date):
    print(year,month,date,datetime.date(year,month,date).isocalendar()[1]-7,datetime.date(year,month,date).isocalendar()[2])
a=int(input("年份:"))
b=int(input("月份:"))
c=int(input("日期:"))
riqi(a,b,c)
xiaoli(a,b,c)