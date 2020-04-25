#   定义一个dog类(颜色, 名称), 里面有一个狗叫的方法; 不同的狗叫声可能不一样;  然后实例化几条狗, 然后统计实例化狗的数量
class Dog1:
    color=''
    name=''
    count=0
    def __init__(self,color,name):
        self.color=color
        self.name=name
        self.__class__.count+=1#每调用一次Dog1，count就+1
    def goujiao(self):
        if(self.name=="柴犬"):
            print("aaaaa")
         
        elif(self.name=="萨摩耶"):
            print("bbbbb")
          
    @staticmethod
    def count_1():
        print("有%d条狗" % (Dog1.count))

dog1=Dog1("红色","柴犬")
dog2=Dog1("蓝色","萨摩耶")
dog1.goujiao()
Dog1.count_1()
