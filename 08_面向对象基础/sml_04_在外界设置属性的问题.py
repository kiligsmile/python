class Cat:
    def eat(self):
        # 使用self在方法内部输出每一只猫的名字
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼"%self.name)
        # print("小猫爱吃鱼")
    def drink(self):
        print("%s要喝水"%self.name)
        # print("小猫要喝水")
# 创建猫对象
tom = Cat()
# 给对象增加属性 可以使用 .属性名  利用赋值语句就可以了
# tom.name = "Tom"
tom.eat()
tom.drink()
# 在日常开发中，不推荐在类的外部给对象增加属性
# 因为如果在运行时没有找到属性，程序会报错
# 对象应该包含有哪些属性，应该封装在类的内部
tom.name()="Tom"