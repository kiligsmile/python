class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count=0
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量%d"%cls.count)
    def __init__(self,name):
        self.name=name
        # 让类属性的值+1
        Tool.count +=1
# 1.创建工具对象
tool1=Tool("斧头")
tool2=Tool("榔头")
tool3=Tool("水桶")
# 调用类方法
Tool.show_tool_count()

# 注意：在类方法内部，要想访问当前类的属性，
# 或者访问当前类的其他方法，使用cls.的方式就可以。
# 而在类的外部，要想调用类方法，使用类名.类方法 就可以
