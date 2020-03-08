#6 前面2个元素为0，1，输出100以内的斐波那契数列；
f1=0
f2=1
print(f1)
print(f2)
for i in range(1,101):
    if i==f2+f1:
        print(i)
        f1,f2=f2,i