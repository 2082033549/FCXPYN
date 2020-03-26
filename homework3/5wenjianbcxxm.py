# 5 文件编程小项目
import os
os.chdir('G:\\') 
f1=open(r'Blowing in the wind.txt','w')
f1.write('How many roads must a man walk down \nBefore they call him a man \nHow many seas must a white dove sail \nBefore she sleeps in the sand \nHow many times must the cannon balls fly \nBefore they\'re forever banned \nThe answer my friend is blowing in the wind \nThe answer is blowing in the wind\n')
f1.close()
f2=open(r'Blowing in the wind.txt','r+')
ly=f2.readlines()
ly.insert(0,'Blowin\'in the wind\n')
f2.seek(0,0)
f2.writelines(ly)
f2.close()
f3=open(r'Blowing in the wind.txt','r+')
ly=f3.readlines()
ly.insert(1,'——Bob Dylan\n')
f3.seek(0,0)
f3.writelines(ly)
f3.close()
f4=open(r'Blowing in the wind.txt','a')
f4.write('1962 by Warner Bros. Inc.')
f4.close()
f5=open(r'Blowing in the wind.txt','r')
a=f5.readlines()
for i in range(0,len(a)):
    if 1<i<len(a)-1:
        print('\t'+a[i])
    else:
        print('\t\t'+a[i])
f5.close()