name_list = ["zhangsan","lisi","wangwu"]
# 1.取值
# list index out of range - 列表索引超出范围
print(name_list[2])

# 2.取索引：知道数据的内容，想要确定数据在列表中的位置
# 使用index方法需要注意，如果传递的数据不在列表中，程序会报错！
print(name_list.index("wangwu"))

# 3.修改
name_list[1]="李四"
#list assignment index out of range
# 列表指定的索引超出范围，程序会报错！

# 4.增加
# append方法可以向列表的末尾追加数据
name_list.append("smile")
# insert方法可以在列表的指定索引位置插入数据
name_list.insert(1,"kilig")

# extend方法可以把其他列表中的完整内容，追加到当前列表的末尾
tem_list = ["拉拉","大康","小拉"]
name_list.extend(tem_list)

# 5.删除
# remove方法可以从列表中删除指定的数据
name_list.remove("wangwu")
# pop方法默认可以把列表中最后一个元素删除
name_list.pop()
# pop方法可以指定要删除元素的索引
name_list.pop(3)
# clear方法可以清空列表
name_list.clear()


