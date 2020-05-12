l1 = [1,2,3,4,5,6,7]
def jishu_list(l,li = []):
    n = 1
    for i in l:
        if n%2 == 1:
            li.append(i)
            n += 1
    return li
print(jishu_list(l1))