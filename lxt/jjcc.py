# 定义一个高阶函数, 实现加,减,乘,除计算器功能;
def jia(a,b):
    c=int(a+b)
    return c
def jian(a,b):
    c=int(a-b)
    return c
def cheng(a,b):
    c=int(a*b)
    return c
def chu(a,b):
    c=int(a/b)
    return c
def jsq(a,b,d,e,f,g):
    print(d(a,b))
    print(e(a,b))
    print(f(a,b))
    print(g(a,b))
jsq(5,6,jia,jian,cheng,chu)
