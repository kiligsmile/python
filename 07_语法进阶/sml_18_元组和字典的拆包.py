def demo(*args,**kwargs):
    print(args)
    print(kwargs)
# 元组变量/字典变量
gl_nums=(1,2,3)
gl_dict = {"name":"拉拉","age":18}
demo(*gl_nums,**gl_dict)
print(" ")

def demo(*args,**kwargs):
    print(args)
    print(kwargs)
gl_nums=(1,2,3)
gl_dict = {"name":"拉拉","age":18}
demo(1,2,3,name="拉拉",age="18")
print(" ")

# 其实吧直接这样子也可以的
def demo(args,kwargs):
    print(args)
    print(kwargs)
gl_nums=(1,2,3)
gl_dict = {"name":"拉拉","age":18}
demo(gl_nums,gl_dict)
