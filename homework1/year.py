#4 判断用户输入的年份是否为闰年
x=int(input("输入年份:"))
if x%4==0 and x%100!=0:
    print("是闰年")
elif x%400==0:
    print("是闰年")
else:
    print("不是闰年")