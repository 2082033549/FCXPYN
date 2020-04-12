#  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
# import getpass
# _username=input('username:')
# _password=getpass.getpass('password:')
# #输入密码并实现隐藏密码的函数，调用之后密码将不会以明文形式显示
# str1=''
# for i in range(1,6):
#     xm=input('姓名:')
#     yhm=input('username:')
#     mm=getpass.getpass('password:')
#     str1+=xm
#     str1+="    "
#     str1+=yhm
#     str1+="    "
#     str1+=mm
#     str1+='\n'
# with open('test.txt', 'w') as f:
#     f.write(str1)
import getpass
list1= ["李一","李二","李三","李四","李五"]
with open(r"G:\text111\text_1.txt","a")as f1:
    for i in range(5):
        zh=input("请输入账号:")
        zh+=" "
        mm=getpass.getpass('请输入密码:')
        f1.write(list1[i])
        f1.write(zh)
        f1.write(mm)
        f1.write("\n")
