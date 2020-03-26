# 2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
# #第一行： xxxx
# #第二行： xxxx
def duqushujv():
    list1=[]
    try:
        f=open("G:/input.txt","a+")
        while True:
            str1 = f.readline()
            if str1 is None:
                f.close()
                return list1
            str2 = str1.rstrip()#删除 string 字符串末尾的指定字符（默认为空格）
            list1.append(str1)
    except IOError:
        print("发生错误")
def xianshishujv(list2):
    print(list2)
    for i,str2 in enumerate(L,1):#将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
        print("第{}行: {}".format(i,str2))
 
xianshishujv(duqushujv())