"""
    包：有层次的目录结构，用来更好的管理模块，庸俗来讲就是一个目录，
    里面存放python文件新的包目录，并且每一个包目录里面都需要一个__init__.py文件
    注意：__init__.py在python3.3版本之后不需要自己创建，但是为了版本的兼容性，建议还是创建

    __init__.py
            1、标识包目录：告诉python解释器该文件所在目录应该被视为一个包，而不是一个普通目录
            2、执行初始化代码：在调用该包里模块时，该文件里面的代码也会被运行
            3、通过__all__来控制哪些模块可以被导入
            4、提供包级别的命名空间
            5、批量导入模块
    from 包名 import 模块
    import 包名。模块名
    在python中，可以使用绝对路径或相对路径，需要根据项目结构和实际需求来选择合适的导入路径
    绝对路径从项目的根目录，相对路径相当于当前模块的位置
"""
import mypackage.module1
from mypackage import module2

mypackage.module1.info_print1()
module2.info_print2()
