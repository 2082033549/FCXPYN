#8 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
import operator
listt=[{'numb':'01','name':'K','time':2,'saly':'2000'},{'numb':'02','name':'L','time':3,'saly':'3000'},{'numb':'03','name':'I','time':1,'saly':'8000'},{'numb':'04','name':'J','time':6,'saly':'1000'},{'numb':'05','name':'N','time':5,'saly':'9000'},{'numb':'06','name':'A','time':11,'saly':'2000'},{'numb':'07','name':'B','time':13,'saly':'14000'},{'numb':'08','name':'C','time':4,'saly':'7000'},{'numb':'09','name':'D','time':10,'saly':'6000'},{'numb':'10','name':'E','time':15,'saly':'3000'}]
sorted_x = sorted(listt, key=lambda x : x['saly'],reverse=True) 
print(sorted_x )







