# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})
class dictclass:
    def __init__(self,zd):
        self.zd=zd
    def del_dict(self,key):#删除某key
        del self.zd[key]
    def get_dict(self,key):#判断某键
        if key in self.zd.keys():
            return self.zd[key]
        else:
            return "not found"
    def get_key(self):#返键列表
        return list(self.zd.keys())
    def update_dict(self,zd1):#合并字典
        for i in zd1.keys():
            self.zd[i]=zd1[i]
        return list(self.zd.values())#返回组合列表


a={"颜色":"red","价格":20}
b={"姓名":"王一","性别":"男"}
zd_1=dictclass(a)
zd_1.del_dict("颜色")
print(zd_1.get_dict("性别"))
print(zd_1.get_dict("价格"))
print("keys:",zd_1.get_key())
print(zd_1.update_dict(b))

