# 定义一个print_line函数能够打印*组成的一条分割线
def print_line():
    print("*"*50)
print_line()

# 定义一个函数能够打印由任意字符组成的分隔线
def print_line(char):
    print(char*50)
print_line("-")

# 定义一个函数能够打印由任意字符组成的分隔线
def print_line(char,times):
    print(char*times)
print_line("kilig",40)