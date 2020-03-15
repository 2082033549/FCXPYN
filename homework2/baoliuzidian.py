#5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
def a4(arg):
    ret = {}
    for key,value in arg.items():
        if len(value) > 2:
            ret[key] = value[0:2]
        else:
            ret[key] = value
    return  ret
dic = {"k1": "qwef", "k2": [11, 22, 33, 44],"k3":"616891"}
r = a4(dic)
print(r)