#   7 使用python代码统计一个文件夹中所有文件的总大小
# import os
# ret = os.sep.join(__file__.split('/')[:-2])
# name = os.path.basename(ret)
# sum = 0
# def func(dirpath):
#     lst = os.listdir(dirpath)  # 大文件夹下文件列表,包括文件夹
#     for el in lst:
#         new_dir = dirpath+'\\'+el
#         if os.path.isfile(new_dir):
#             getsize = os.path.getsize(new_dir)
#             global sum
#             sum += getsize
#         else:
#             func(new_dir)
#     return sum

# num = func(ret)
# print('文件夹%s的大小为%s字节' % (name,num))
import os
path=r"F:\PyCharm 2019.3.3\plugins"
sum=0
fandd=os.listdir(path)
for i in fandd:
    file=os.path.join( r"F:\PyCharm 2019.3.3\plugins",i)#合成路径
    sum+=os.path.getsize(file)
print("总大小为:%d" % sum)

