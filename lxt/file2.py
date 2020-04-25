#一个文件内容的如下,请读取文件的内容, 并输出;
with open('D:\PPython\exe_11\ceshi_1.txt', 'r',encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
#一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出;
str_1='\n'
print(str_1.join(sorted(open('D:\PPython\exe_11\ceshi_1.txt', 'r',encoding='utf-8'), key=lambda s: s.split()[2],reverse=1)))