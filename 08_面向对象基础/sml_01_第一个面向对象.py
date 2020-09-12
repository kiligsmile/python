class cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")
# 创建猫对象
tom = cat()
tom.eat()
tom.drink()
print(tom)
addr = id(tom)
print("%x"%addr)