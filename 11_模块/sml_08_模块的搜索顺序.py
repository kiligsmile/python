"""注意如果当前目录下存在一个random.py的文件，程序就无法正常执行，
这个时候，python解释器会加载当前目录下的random.py
而不会加载系统的random模块"""
import random
# python中每一个模块都有一个内置属性__file__ 可以查看模块的完整路径
# print(random.__file__)
rand = random.randint(0,10)
print(rand)