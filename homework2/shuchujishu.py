#3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
from random import randint
list1=[randint(0,100) for _ in range(1,11)]
print("奇数有:")
for i in list1:
    if i%2==1:
        print(i)