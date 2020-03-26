# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
str1='\n'
print(str1.join(sorted(open('D:\PPython\exe_11\ceshi_1.txt', 'r'), key=lambda s: s.split()[2],reverse=1)))