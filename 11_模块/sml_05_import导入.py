"""
import模块名 是一次性把模块中所有工具全部导入，
并且通过模块名/别名访问
使用from...import可以直接使用模块提供的工具
不需要通过模块名.
"""
from sml_01_测试模块1 import Dog
from sml_01_测试模块2 import say_hello
say_hello()
wangcai=Dog()
print(wangcai)