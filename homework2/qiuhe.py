#2 写一个函数，接收n个数字，求这些参数数字的和
def sum_func(*args):
    sm = 0
    for i in args:
        sm += i
    return sm
 
print(sum_func(10,18,78,45,75,96))