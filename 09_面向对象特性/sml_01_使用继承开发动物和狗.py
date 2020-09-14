class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")



class Dog(Animal):
    def bark(self):
        print("汪汪叫")

# 创建一个对象--狗对象
lulu=Dog()
lulu.eat()
lulu.drink()
lulu.run()
lulu.sleep()
lulu.bark()
