#10 给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：crtl+K+C(注释)
# word={}
# s1=input("输入文本:")
# s1=s1.lower()#大写转小写
# for i in s1:
#     if not("a"<=i and i<="z"):
#         s1=s1.replace(i," ")
# s2=s1.split(" ")
# list1=list(s2)
# for i in list1:
#     if i in word:
#         word[i]+=1
#     else:
#         word[i]=1
# del word[""]
# print(word)
import collections
word={}
a=input("输入文本:")
a.split()
print(collections.Counter(a))

