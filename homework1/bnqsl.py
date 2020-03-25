#6 前面2个元素为0，1，输出100以内的斐波那契数列；
a=0
b=1
print(a)
for i in range(1,100):
    if i==b+a:
        print(i)
        a,b=b,i