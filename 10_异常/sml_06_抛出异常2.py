def input_password():
    # 1.提示用户输入密码
    pwd = input("请输入密码：")
    # 2.判断密码长度>=8.返回用户输入的密码
    if len(pwd) >=8:
        return pwd
    # 3.如果<8主动抛出异常
    print("主动抛出异常")
    # 1>创建异常对象--可以使用错误信息字符串作为参数
    ex = Exception("密码长度不够")
    # 2>主动抛出异常
    raise ex
# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
# 要想主动抛出异常，先要创建一个异常对象，
# 然后使用raise关键字把异常对象输出，
# 抛出之后在调用函数一方就可以捕获到异常了