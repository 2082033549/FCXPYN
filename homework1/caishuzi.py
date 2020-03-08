#9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
a=int(input("请输入一个数字:"))
b=int(input("请输入猜的次数:"))
c=int(input("请输入想猜的数字:"))
d=0
if c==a:
    print("成功！")
if c!=a:
    d=d+1
    if d<b:
       e=int(input("失败了,请再输入想猜的数字:"))
       if e==a:
          print("成功!") 
       if e!=a:
            d=d+1
            f=int(input("失败了,请再输入想猜的数字:"))
            if c==a:
              print("成功!") 
            if f!=a:
                d=d+1
                if d<b:
                    g=int(input("失败了,请再输入想猜的数字:"))
                else:
                    print("猜测失败")
    else:
        print("猜测失败")
    
