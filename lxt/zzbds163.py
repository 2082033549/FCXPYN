# 匹配出163的邮箱地址，且@符号之前有4到20位，例如hello@163.com
import re
email_list=["a51sd65a21@163.com","aaaaaaaaaaaaaaaaaaaaa@163.com","@@@@@163.com"]
for i in email_list:
    ret = re.match("[\w]{4,20}@163.com$",i)
    if ret:
        print("你输入的邮箱%s符合要求" % i)
    else:
        print("%s不符合要求" % i)
        