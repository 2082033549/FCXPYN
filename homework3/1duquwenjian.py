# 1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
def duquxinxi():
    list1=[]
    while True:
        str1=input("请输入文本信息")
        if str1==' ':
            return str1
        list1.append(str1)
def xieru(list2):
    try:
        f=open("G:/input.txt","a+")
        for i in list2:
            f.write(i)
            f.write('\n')
        f.close()
    except IOError:
        print("发生错误")