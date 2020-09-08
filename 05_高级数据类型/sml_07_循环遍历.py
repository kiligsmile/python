info_tuple = ("smile",18,1.60)
# 使用迭代遍历元组
for my_info in info_tuple:
    # 使用格式字符串拼接my_info 这个变量不方便
    # 因为元组中通常保存的数据类型是不同的
    print("我的名字叫%s" % my_info)
