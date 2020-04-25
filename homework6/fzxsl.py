# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。
class Student:
    def __init__(self,name,age,sex,score):
        self.name=name
        self.age=age
        self.sex=sex
        self.score=score
    def zf(self):#单个学生总分
        return int(sum(self.score))
    def pjf(self):#平均分
        return int(sum(self.score)/3)
    def xsxx(self):#学生信息
        print("姓名:",self.name,"年龄:",self.age,"性别:",self.sex,"分数:",self.score[0],self.score[1],self.score[2])
a=Student("李一",18,"男",[70,80,90])
print("总分",a.zf())
print("平均分",a.pjf())
a.xsxx()