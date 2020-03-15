#7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
import random
list1 = [random.randint(0,100) for i in range(20)]
for i in list1:
    if i>=90:
        print("A")
    if(i>=80 and i<90):
        print("B")
    if(i>=70 and i<80):
        print("C")
    if(i<70):
        print("D")