# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#        实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
class Dog:
    list1=[{"颜色":["red","black","blue"]},{"数量":[6,7,8]},{"价格":[2000,1500,4600]}]
    @classmethod
    def mg(cls,colour,num):#颜色和购买数量
        if colour=="red":
            cls.list1[1]["数量"][0]=cls.list1[1]["数量"][0]-num
        elif colour=="black":
            cls.list1[1]["数量"][1]=cls.list1[1]["数量"][1]-num
        elif colour=="blue":
            cls.list1[1]["数量"][2]=cls.list1[1]["数量"][2]-num        
    @staticmethod
    def scg():#打印输出
        print("各类狗的数量:")
        for i in range(3):
            print(Dog.list1[0]["颜色"][i],Dog.list1[1]["数量"][i])    
Dog.scg()#展示开始的狗的颜色以及数量

a=input("请输入狗的颜色和购买数量:").split(",")
Dog.mg(a[0],int(a[1]))
Dog.scg()
