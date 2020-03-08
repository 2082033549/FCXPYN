#1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
for i in range(0,51):
    if i%2==0:
        print("偶数有:",i)
    if i%2==1:
        print("奇数有:",i)
    if i%2==0:
        if i%3==0:
            if i!=0:
                print("能同时被2和3整除的有:",i)
    if i>1:
        for k in range(2,i):
            if(i%k)==0:
                break
            else:
                print("质数有",i)
