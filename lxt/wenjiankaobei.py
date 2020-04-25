#将一个文件夹下的某个文件(设定这个目标文件夹下,只有文件),拷贝到另外一个文件夹下去
#提示:
#写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个#参数是目标位置，将源文件copy到目标位置。
# 还需要判断一下这个文件之前是否存在
#提示2:  读源文件的内容;
#            创建目标文件;
#           读到的内容,再写入到目标文件
def copy(path1,path2):
    with open(path1,'r',encoding='utf-8') as f:
        str1=f.read()
        print(str1)
    with open(path2,'a+',encoding='utf-8') as f1:
        f1.write(str1)
    return 1

path11 = r'D:\a\test.txt'
path22 = r'D:\b\test.txt'
copy(path11,path22)


