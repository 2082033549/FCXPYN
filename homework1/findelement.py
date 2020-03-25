#1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
for i in range(0,4):
    if i==0:
        print("奇数有:")
        for x in range(0,50):
            if x%2==1:
                print(x,end=" ")
        print()
    elif i==1:
        print("偶数有:")
        for x in range(0,50):
            if x%2==0:
                print(x,end=" ")
        print()
    elif i==2:
        print("质数有:")
        for x in range(0,50):
            if x>1:
                for k in range(2,x):
                    if(x%k)==0:
                        break
                else:
                    print(x,end=" ")
        print()
    else:
        print("能同时被2和3整除的有:")
        for x in range(0,50):
            if x%2==0 and x%3==0:
                print(x,end=" ")