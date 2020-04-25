# 1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#         人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#         人和狗的攻击力,都会因为被咬, 或者被打而降低(人被咬一次,打击力降低2;  狗被打一次,攻击力降低3);
#     3   对战规则: 
#      A  随机决定,谁先开始攻击; 
#      B  一方攻击完毕后, 另外一方再开始攻击;  攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
import random

class people():
    r1={"名字": "李一", "攻击力": 10, "血量": 100}
    r2={"名字": "李二", "攻击力": 10, "血量": 100}
    list1=[r1,r2]
    def gj(self):#人类攻击
        for i in range(50):#50回合
            z=random.randrange(0,2)
            if not self.list1[z]["血量"]>0: #如果血量不为0，即存活
                return self.list1[z]["名字"],self.list1[z]["攻击力"]#随机选择一个人
    def bgj(self,y):#参数为被击打的血量
        for i in range(50):
            z=random.randrange(0,2)
            if not y==0 and not self.list1[z]["攻击力"]==0:
                self.list1[z]["攻击力"]-=2
                self.list1[z]["血量"]-=y
                return z,self.list1[z]["名字"]
            elif not self.list1[z]["血量"]<=0:
                if not self.list1[z]["血量"]<=0:
                    self.list1[z]["血量"]-=y
                else:
                    self.list1[z]["血量"]=0
                return z,self.list1[z]["名字"]

    def shibai(self):
        for i in self.list1:
            if not i["血量"]==0:
                return 1
        else:
            return 0       