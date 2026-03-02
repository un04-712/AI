"""
    模块：以.py为后缀的python文件，可以被其他python程序导入和使用
    也可以独立执行
    模块的导入 import 关键字 配合from 和 as
    import 模块
    import 模块 as 别名
    form 模块 import 子模块
    form 模块 import 子模块 as 别名
    form 模块 import *

    模块的作用：
            不需要从零开始，不用重复"造轮子"的过程
            避免同一模块命名重复问题
            方便代码的管理和维护，提高代码的可读性

    模块内置变量：dir()查看模块内置变量

    __name__用于确定模块是否被直接运行或者被导入其他模块
    当模块直接运行时，值为__main__
    否则为
    __file__    模块的文件路径
    __all__     定义一个模块中那些变量，函数，类可以通过from module import *导入时可用
    __package__ 包含模块所在的包路径
    __dict__    包含模块的全局命名空间
    __doc__     模块的说明文档
    模块的类型：
            内置模块：python解释器自带的标准库模块
            第三方模块：pip安装模块
            自定义模块：根据自己需求来编写的py文件
"""
import random    #调用：模块名.子模块
#
# print(random.randint(1,1000))
#
# import random as rd     #调用:别名.子模块
#
# print(rd.randint(1,1000))
#
# from random import randint  #调用 子模块名
#
# print(randint(1,1000))
#
# from random import randint as rd    #调用:别名.子模块
#
# print(rd(1,1000))
#
# from random import *    #调用 子模块名
#
# print(randint(1,1000))


print(random.__name__)
print(random.__doc__)
print(random.__dict__)
print(random.__package__)
print(random.__file__)
