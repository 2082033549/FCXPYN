# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:
class Student:
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_course(self):
        return int(max(self.score))
a=Student("李一",18,[10,20,30])
print("姓名",a.get_name())
print("年龄",a.get_age())
print("最高分",a.get_course())
b=Student("李二",18,[40,50,99])
print("姓名",b.get_name())
print("年龄",b.get_age())
print("最高分",b.get_course())