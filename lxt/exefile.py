import os
pwd = os.path.abspath('.')
print("绝对路径是:",pwd)
print( os.path.basename('D:\PPython\pdcd.py\exe_1\aaa.txt') )   # 返回文件名
print( os.path.dirname('D:\PPython\pdcd.py\exe_1\aaa.txt') )    # 返回目录路径
print( os.path.split('D:\PPython\pdcd.py\exe_1\aaa.txt') )      # 分割文件名与路径
print( os.path.join('\pdcd.py','test','aaa.txt') )  # 将目录和文件名合成一个路径