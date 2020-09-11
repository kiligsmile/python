gl_num = 10
# 再定义一个全局变量
gl_title = "拉拉会发光"
# 再定义一个全局变量
gl_name = "拉拉"
def demo():
    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的线
    num = 99
    print("%d"%num)
    print("%s"%gl_title)
    print("%s"%gl_name)
demo()
