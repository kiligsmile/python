students=[
    {"name":"阿土","age":"17"},
    {"name":"小美","age":"16"}
]
# 在学员列表中搜索指定的姓名
find_name = "阿土"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] ==find_name:
        print("找到了%s"%find_name)
print("循环结束")

students=[
    {"name":"阿土","age":"17"},
    {"name":"小美","age":"16"}
]
# 在学员列表中搜索指定的姓名
find_name = "阿土"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] ==find_name:
        print("找到了%s"%find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
print("循环结束")

students=[
    {"name":"阿土","age":"17"},
    {"name":"小美","age":"16"}
]
# 在学员列表中搜索指定的姓名,若不存在，希望给予相应提示
find_name = "小黑"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] ==find_name:
        print("找到了%s"%find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
else:
    print("抱歉没有找到%s"%find_name)
print("循环结束")

students=[
    {"name":"阿土","age":"17"},
    {"name":"小美","age":"16"}
]
# 在学员列表中搜索指定的姓名,若不存在，希望给予相应提示
find_name = "小黑"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] ==find_name:
        print("找到了%s"%find_name)
        # 如果已经找到，应该直接退出循环，而不再遍历后续的元素
        break
    else:

         print("抱歉没有找到%s"%find_name)
print("循环结束")
