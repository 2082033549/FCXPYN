# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  如果都正确,打印提示, 您登录成功(失败);

with open(r"G:\text111\text_1.txt")as f2:
        lines = f2.readlines()#读取一行数据
        xm= input("请输入姓名:")
        for i in range(6):
            if xm== lines[i][0:2]:
                zh= input("请输入账号:")
            if zh== lines[i][2:5]:#账号三位数
                mm= input("请输入密码:")
                if mm== lines[i][6:20]:
                    print("登陆成功!")
        if i == 5:
            print("登陆失败！")