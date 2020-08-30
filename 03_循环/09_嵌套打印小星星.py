row=1
while row <=5:
    # 增加一个小的循环，专门负责当前行中，每一"列"的星星显示
    # 1.定义一个列计数器变量
    col=1
    # 2.开始循环
    while col <=row:
        # print("%d"%col)
        print("*",end="")
        col +=1
    #print("第%d行"%row)
    #这行代码的目的，就是在一行星星输出完成之后，添加换行！
    print("")
    row +=1
