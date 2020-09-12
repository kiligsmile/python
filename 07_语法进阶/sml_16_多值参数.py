# 有时候需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数
# python中有两种多值参数：
# 参数名前增加一个*可以接收元组
# 参数名前增加两个**可以接收字典
def demo(num,*nums,**person):
    print(num)
    print(nums)
    print(person)
# demo(1)
# demo(1,2,3,4,5)
demo(1,2,3,4,5,name="拉拉",age=18)