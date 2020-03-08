#3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
list3 = sorted(list(set(list1)))
list4 = sorted(list(set(list2)))
list5 = []
x = 0
for i in list3:
    for j in range(x,len(list4)):
        if i == list4[j]:
            list5.append(i)
            x =j
            continue
print(list5)