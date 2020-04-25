# 1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#         人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#         人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#     3   对战规则: 
#      A  随机决定,谁先开始攻击; 
#      B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
import time
import random

class fight():
    d=dog()
    p=people()
    def __init__(self):
        i=random.randint(0,2)
        for i in range(i,100):
            if not self.p.shibai():
                print("dog胜利")
                break
            elif not self.d.shibai():
                print("people胜利")
                break
            elif i%2==1:
                p,p1=self.d.attack()
                o,o1=self.p.behit(p1)
                print("{}攻击了{}".format(p,o1))
                print("{}攻击下降2,生命下降{}".format(o1,p1))
                print(self.p.list1[o])
                if not self.p.list1[o]["血量"]>0:
                    print("{}被杀死".format(self.p.list1[o]["name"]))
            elif i%2==0:
                m,m1=self.p.attack()
                x,x1=self.d.behit(m1)
                print("{}攻击了{}".format(m,x1))
                print("{}攻击下降3,生命下降{}".format(x1,m1))
                print(self.d.list1[x])
                if not self.d.list1[x]["血量"]>0:
                    print("{}被杀死".format(self.d.list1[x]["name"]))                
f=fight()