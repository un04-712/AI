"""
    注意:导入模块是会先执行模块文件里面的内容
"""

from  Module1 import * #只有导入所有模块受all参数影响
from  Module1 import mul,add,b  #不受all参数影响
print(add(1,2))
print(mul(4,2))
print(b)
