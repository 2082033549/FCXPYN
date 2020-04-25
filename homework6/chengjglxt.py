# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;
import os
import sys
class xscjgl:
    def __init__(self):
        self.list_1=[]
        with open(r"D:\PPython/\text1\text__11.txt","r",encoding="utf-8") as f1:
            while True:
                text1=f1.readline()
                if text1:
                    self.list_1.append(text1.split())
                else:
                    break

    def tjxx(self): # 添加学生信息
        c=input("请输入添加的学生信息(班级,学号,姓名,分数)(用空格隔开)").split()
        self.list_1.append(c)
        with open(r"D:\PPython/\text1\text__11.txt","w",encoding="utf-8") as f2:
            for a in self.list_1:
                f2.write(a[0]+" "+a[1]+" "+a[2]+" "+a[3])
                f2.write("\n")
        print("添加成功")

    def scxx(self): # 删除学生信息
        d=input("请输入要删除的学生的学号")
        for i,a in enumerate(self.list_1):
            if d==a[1]:
                self.list_1.pop(i)#移除该元素
                with open(r"D:\PPython/\text1\text__11.txt","w",encoding="utf-8") as f3:
                    for a in self.list_1:
                        f3.write(a[0]+" "+a[1]+" "+a[2]+" "+a[3])
                        f3.write("\n")
                print("删除成功")
                return 
        print("输入错误")
    
    def xgxx(self): # 修改学生信息
        d=input("请输入要修改的学生的学号")
        for i,a in enumerate(self.list_1):
            if d==a[1]:
                c=input("请输入添加的学生信息(班级,学号,姓名,分数)(用空格隔开)")
                self.list_1[i]=c.split()
                with open(r"D:\PPython/\text1\text__11.txt","w",encoding="utf-8") as f4:
                    for a in self.list_1:
                        f4.write(a[0]+" "+a[1]+" "+a[2]+" "+a[3])
                        f4.write("\n")
                print("成功！")
                return 
        print("不存在此学号")
    def cxxx(self):# 查询学生信息
        d=input("请输入学生学号")
        for i,a in enumerate(self.list_1):
            if d==a[1]:
                print(self.list_1[i][0]+" "+self.list_1[i][1]+" "+self.list_1[i][2]+" "+self.list_1[i][3])
                return 
        print("不存在此学号！")
    
        # def jiemian():
        #     print("---------------------------")
        # print("      学生管理系统 V1.0")
        # print("                           ")
        # print("      1:添加学生"            )
        # print("      2:删除学生"            )
        # print("      3:修改学生"            )
        # print("      4:查询学生"            )
        # print("      5:显示所有学生"         )
        # print("      6:保存数据"            )
        # print("      7:退出系统"            )
        # print("                           ")
        # print("---------------------------")

    @staticmethod
    def zjm():
        while 1:
            print("1添加信息\n2删除信息\n3修改信息\n4查询信息")
            b=int(input("请输入选项:"))
            if b>=0 and b <=5:
                return b
e=xscjgl()
while True:
    b=xscjgl.zjm()
    if b==1:
        e.tjxx()
        sys.exit(0)
    elif b==2:
        e.scxx()
        sys.exit(0)
    elif b==3:
        e.xgxx()
        sys.exit(0)
    elif b==4:
        e.cxxx()
        sys.exit(0)
