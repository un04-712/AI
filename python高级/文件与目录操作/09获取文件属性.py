
import os
import time
# 获取文件大小
nsize = os.path.getsize('./测试文件夹/1.txt')
print(nsize)

#获取文件的最后修改时间
#返回是一个浮点数,单位为s
last_time = os.path.getmtime('./测试文件夹/1.txt')
lotime = time. localtime(last_time)
res = time. strftime ( '%Y-%m-%d %H :%M :%S ',lotime)
print(res)

# 获取文件的创建时间
create_time = os.path.getctime('./测试文件夹/1.txt')
lotime = time. localtime(create_time)
res = time. strftime ('%Y-%m-%d %H :%M :%S',lotime)
print(res)

# 获取文件的最后访问时间
access_time = os.path.getatime('./测试文件夹/1.txt')
lotime = time. localtime(access_time)
res = time. strftime ('%Y-%m-%d %H :%M :%S',lotime)
print(res)