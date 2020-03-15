#1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def test(num):
    a=int(len(num))
    print("长度为%d" % a)
test_num = eval(input("请输入字符串，列表或元组,字符串请加上引号："))
test(test_num)