# 1 数据库查询练习：
#    针对我们给大家的2张表（学生表和班级表），做以下查询；（查询脚本放在一个文件中，创建一个SQL文件夹，放到这个里面，最有提交到代码仓库）
# ① 查询所有男生的姓名，年龄，所在班级名称；
# ② 查询所有查询编号小于4或没被删除的学生；
# ③ 查询姓黄并且“名”是一个字的学生；
# ④ 查询编号是1或3或8的学生
# ⑤ 查询编号为3至8的学生
# ⑥ 查询未删除男生信息，按年龄降序
# ⑦  查询女生的总数
# ⑧  查询学生的平均年龄
# ⑨ 分别统计性别为男/女的人年龄平均值
# ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
#         | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# 	| 中性   | 金星                                                       |
# 	| 保密   | 凤姐
def cx1():
    query1 = session.query(Students.name, Students.age, Students.cls_id).filter(Students.gender == '男').all()
    for data in query1:
        print(*data)
print('所有男生的姓名，年龄，所在班级名称是为:')
cx1()

def cx2():
    query1=session.query(Students).filter(or_(Students.id<4, Students.is_delete==0)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('所有查询编号小于4或没被删除的学生为:')
cx2()

def cx3():
    query1=session.query(Students).filter(Students.name.like('黄_')).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('姓黄并且“名”是一个字的学生为:')
cx3()

def cx4():
    query1=session.query(Students).filter(or_(Students.id==1,Students.id==3,Students.id==8)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('编号是1或3或8的学生为:')
cx4()

def cx5():
    query1=session.query(Students).filter(and_(Students.id>=3, Students.id<=8)).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('编号为3至8的学生为:')
cx5()

def cx6():
    query1=session.query(Students).filter(Students.is_delete==0).order_by(Students.age.desc()).all()
    for data in query1:
        print(data.id, data.name, data.age, data.height, data.gender, data.cls_id, data.is_delete)
print('未删除男生信息，按年龄降序为:')
cx6()

def cx7():
    query1=session.query(func.count(Students.id)).filter(Students.gender == '女').scalar()
    print(query1)
print('女生的总数为:')
cx7()

def cx8():
    query1 = session.query(func.avg(Students.age)).scalar()
    print(query1)
print('学生的平均年龄为')
cx8()

def work9():
    query1=session.query(func.avg(Students.age)).filter(Students.gender=='男').scalar()
    print(query1)
    query2 = session.query(func.avg(Students.age)).filter(Students.gender == '女').scalar()
    print(query2)
print('分别统计性别为男/女的人年龄平均值为:')
work9()

session.close()