class Cat:
    def __init__(self,new_name):
        self.name = new_name
        print("%s来了"%self.name)
    def __del__(self):
        print("%s我去了"%self.name)
# Tom是一个全局变量，当所有代码执行完成之后，才会把Tom这个对象回收
tom = Cat("Tom")
print(tom.name)
print("-"*50)
# del关键字可以删除一个对象
# del tom
# print("-"*50)


