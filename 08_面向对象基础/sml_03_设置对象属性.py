class cat:
    def eat(self):
        # 使用self在方法内部输出每一只猫的名字
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼"%self.name)
        # print("小猫爱吃鱼")
    def drink(self):
        print("%s要喝水"%self.name)
        # print("小猫要喝水")
# 创建猫对象
tom = cat()
# 给对象增加属性 可以使用 .属性名  利用赋值语句就可以了
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)
# 再创建一个猫对象
lazy_cat = cat()
lazy_cat.name="大懒猫"
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

lazy_cat2=lazy_cat
print(lazy_cat2)