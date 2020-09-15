class A:
    def test(self):
        print("A ---test 方法")
    def demo(self):
        print("A ---demo 方法")



class B:
    def test(self):
        print("B ---test 方法")
    def demo(self):
        print("B ---demo 方法")



class C(B,A):
    pass

# 创建子类对象
c =C()
c.test()
c.demo()

# 确定C类对象调用的方法
print(C.__mro__)