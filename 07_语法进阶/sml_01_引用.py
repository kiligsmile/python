# 用代码的方式来演示在函数调用时，实参是通过引用来调用函数的
def test(num):
    print("在函数内部%d对应的内存地址是%d"%(num,id(num)))
    # 1>定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是%d"%id(result))
    # 2>将字符串变量返回,返回的是数据的引用，而不是数据本身
    return result
    # print("result")
# 1.定义一个数字的变量
a = 10
# 数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是%d"%id(a))
# 2.调用test函数，本质上传递的是实参保存数据的引用，而不是实参保存的数据
test(a)
#  传递变量a的时候，并不会把数字10传递到函数内部，而是把变量a中保存的内存地址，传递到函数内部
# 程序不会报错，但是无法获得返回结果
r = test(a)
print("%s的内存地址是%d"%(r,id(r)))

print(" ")
def test(num):
    print("在函数内部%d对应的内存地址是%d"%(num,id(num)))
    result = "hello"
    print("函数要返回数据的内存地址是%d"%id(result))
    print("result")
a = 10
print("a变量保存数据的内存地址是%d"%id(a))
test(a)
r = test(a)
print("%s的内存地址是%d"%(r,id(r)))