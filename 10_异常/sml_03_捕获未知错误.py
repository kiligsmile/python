try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 使用8除以用户输入的整数并且输出
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    # 注意：此处的result是我们自己定义的变量
    print("未知错误%s"%result)