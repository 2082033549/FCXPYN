# 4  编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    else:
        return 1
def df1(func):
    def wrapper():
        func()
    return wrapper
def df2(func):
    def wrapper():
        return func()
    return wrapper
def df3(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper
@df1
def f1():
    prime=[]
    for x in range(1,20001):
        if isPrime(x)==1:
            prime.append(x)
    print("20000以内的素数有:",prime)
@df2
def f2():
    count = 0
    for x in range(2,10001):
        if isPrime(x) == 1:
            count +=1
    return count
@df3
def f3(a):
    count = 0
    for x in range(2,a+1):
        if isPrime(x) == 1:
            count +=1
    print("%d以内的素数有%d个:" %(a,count))
f1()
print("整数2-10000之间的素数的个数有{}个".format(f2()))
f3(66)