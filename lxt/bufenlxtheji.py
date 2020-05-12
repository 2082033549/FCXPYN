# -*- encoding: utf-8 -*-
import string

'''
@File : hellp.py
@Time : 2020/02/26 08:26:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#dl1='arrqwert'
#str='qwe'
#print(dl1.find(str))
#print(dl1.find(str,6))
#print(dl1.replace("arrqwert","fcxqqwe"))
#print(len(dl1))
#a=[30,60,90,15,75,99,58,36,75,14]
#print(max(a))
#print(min(a))
#print(sum(a))
#print(sum(a)/len(a))
#b=[10,20,66,75,89]
#sort(b)
#print(b)
#tup=(30,60,90,100,89)
#ist[15,51,1561,881,15]
#print(max(tup))
#print(tup[2:])
#print(tup[-3])
#tuple(list)
#dist={'name':'王一','number':'12101515742','age':'15','class':'1802'}
#print(dist['age'])
#del dist['name']
#print(dist)
#dist['school']='huadian'
#print(dist)
#x=input("请输入x的值:")
#print(tuple(x))
#a=int(input("请输入需要苹果的斤数:"))
#b=int(input("请输入每斤苹果的价格:"))
#c=a*b
#print("所需支付的金额为:",c)
#username = input('username:') 
#password = input('password:') 
#print(username,password)

#name = input("name:") 
#age = input("age:") 
#skill = input("skill:") 
#salary = input("salary:") 
#info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
#print(info)

#name = input("name:") 
#age = input("age:") 
#skill = input("skill:") 
#salary = input("salary:") 
#info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary) 

#name = input("username：") 
#age = input("age：") 
#skill = input("skill：") 
#salary = input("salary：") 
#info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary)

#name = input("name：") 
#age = input("age：") 
#skill = input("skill：") 
#salary = input("salary：") 
#info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, name, age, skill, salary) 
#print(info)

#a=[10,11,12,13,14,15,16,17,18,19,20]
#for x in a:
    #if (x%2==0):
        #print(x)

#def pg():
    #zl=int(input("请输入苹果重量:"))
    #js=int(input("请输入苹果斤数:"))
    #jg=int(zl*js)
    #print("价格一共是:",jg)

#pg()

#def alist(list):
    #print("列表里的元素为:",list)
    #list.append([1,2,3,4])
    #print("新增元素后的列表为:",list)

#list1=[12,30,8,47]
#print("list重新赋值之前的地址:",id(list1))
#alist(list1)
#print("list重新赋值之后的地址:",id(list1))

#list1=[i for i in range(1,21)]
#res = filter(lambda x: x%2!=0, list1) #返回奇数
#print(list(res))

#def printinfo( arg1, *vartuple ):
   # print("输出:")
   # print(arg1)
   # print(vartuple)
    #print(list(vartuple))

#printinfo(30,40,50)

def printinfo1( arg2, **vardict ):
    print("输出:")
    print(arg2)
    print(vardict)

printinfo1(1,a=2,b=3)
