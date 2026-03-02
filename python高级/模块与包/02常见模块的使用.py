"""

os模块

"""
# import os
# folder_name = 'new_folder'
# if not os.path.exists(folder_name):
#    os.mkdir(folder_name)
# else:
    #print('文件已经存在')


"""
sys 模块
"""


import sys
print(sys.version)
# print(sys.exit(0))    如果为0表示正常退出，非0 不正常退出

"""
    math模块
"""
import math

print(math.pi)
a = math.pi
print(math.sin(a))

help (math)
"""
    time 模块
"""

import time
# for i in range(10):
#time.sleep(1)
#print(i)
print(time. time ())#自1970年1月1号8点8分8秒(UNIX元年)以来经过的秒数,返回值是一个
                    #浮点数,共中整数部分时秒,小数部分是微妙


start = time.time ()
for i in range(5):
    time.sleep(1)
    print(i)
end = time.time ()
print(end - start)

# random
import random
my_list = [1,2,3,4,5]

# 将列表中的元素随机打乱
random. shuffle(my_list)
print(my_list)