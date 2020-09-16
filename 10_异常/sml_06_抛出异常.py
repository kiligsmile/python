def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码：")
    # 2.判断密码长度>=8.返回用户输入的密码
    if len(pwd) >=8:
        return pwd
    # 3.如果<8主动抛出异常
    print("主动抛出异常")
# 提示用户输入密码
print(input_password())
# 为什么会出现None？
# 因为input_password并没有做任何的返回，
# 在使用print函数进行输出的时候，在控制台输出一个空对象None