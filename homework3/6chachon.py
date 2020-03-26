# 6  在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
#  请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
#     比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
import string
with("G:\text\cs1.txt","r") as f1:
    str1=f1.read()
with("G:\text\cs2.txt","r") as f2:
    str2=f2.read()
word1={}
word2={}
list1={}
list2={}
def chachon(s,w,list3):
    for i in s:
        if not ("a"<=i and i<="z"):
            s=s.replace(i," ")# 替换成 new(新字符串)后生成的新字符串,将不在里面的全部换成空格，以便后续删除
    strs=s.split(" ")#分割空格
    list3=list(strs)#转换成列表
    for i in list3:
        if i in w:
            w[i] += 1     
        else:
            w[i] = 1
    if "" in w:
        del w[""]#删除字典空格
chachon(str1,word1,list1)
def main():
    chachon(str1,word1,list1)
    chachon(str2,word2,list2)
if __name__ == "__main__":
    main()
d1=sorted(word1.items(), key=lambda d:d[1], reverse=1)
d2=sorted(word2.items(), key=lambda d:d[1], reverse=1)
d1=d1[:10]
d2=d2[:10]
print(d1)
print(d2)
b=0
for i in d1:
    if i in d2:
        b+=1
print("相似度{}0%".format(b))
        