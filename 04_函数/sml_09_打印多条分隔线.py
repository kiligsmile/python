# 定义一个函数能够打印5行的分隔线，分隔线要求符合需求3
def print_lines(char,times):
    row=0
    while row<5:
        print_line(char,times)
        row +=1
print_lines("-",20)