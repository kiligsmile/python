# 1.判断空白字符
space_str = " "
print(space_str.isspace())
space_str = "a"
print(space_str.isspace())
space_str = "\t\n"
print(space_str.isspace())

# 1>都不能判断小数
# num_str="1.1"
# 2>unicode字符串
num_str = "\u00b2"
# 3>中文数字
num_str = "一千零一"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
