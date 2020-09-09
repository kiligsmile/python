smile_dict = {"name":"舒媚拉"}
# 1.取值
print(smile_dict["name"])
# 2.增加
smile_dict["age"]=18
# 3.修改
# 如果key存在，会修改已经存在的键值对；若不存在，会新增键值对
smile_dict["name"]="拉拉"
# 4.删除
smile_dict.pop("name")

print(smile_dict)