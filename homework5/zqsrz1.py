# 3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
def af(func):
    def wrapper(*args,**kwargs):
        yhm=input('用户名：')
        mm= input('密  码：')
        if yhm== "123" and mm=="456":
            ret = func(*args,**kwargs)
            return ret
        else:
            print('账户或密码错误!')
    return wrapper
@af
def text1():
    print(1)
@af
def text2():
    print(2)
text1()
text2()