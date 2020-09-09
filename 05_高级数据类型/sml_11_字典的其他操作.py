smile_dict ={"name":"lala",
             "age":18}
# 1.统计键值对数量
print(len(smile_dict))
# 2.合并字典
# 注意：如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp_dict = {"height":1.60,
             "age":17}
smile_dict.update(temp_dict)
# 3.清空字典
smile_dict.clear()
print(smile_dict)
