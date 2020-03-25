#9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；
import random
w=int(input("请输入猜的次数:"))
q=random.randint(10,100)
print(q)
for i in range(0,w):
    e=int(input("想猜的数字是(10-100):"))
    if e==q:
        print("游戏成功！")
        break
else:
    print("游戏失败")