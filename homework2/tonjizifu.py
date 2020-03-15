#4 函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果
s = ' sdfd 5 wewf'
def lei(l):
    num = 0
    isah = 0
    kong = 0
    other = 0
    for i in l :
        if i.isdigit():         
            num +=1
        elif i.isalpha():
            isah +=1
        elif i.isspace():
             kong +=1
        else:
             other +=1
    return num,isah,kong,other   

print(lei(s))