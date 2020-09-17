# 开发时，import代码应该统一写在代码的顶端，更容易及时发现冲突
from sml_01_测试模块1 import say_hello
from sml_01_测试模块2 import say_hello
say_hello()

# 一旦发现冲突，可以使用as关键字给其中一个工具起一个别名
# from sml_01_测试模块2 import say_hello as module2_say_hello
# from sml_01_测试模块1 import say_hello
# module2_say_hello()