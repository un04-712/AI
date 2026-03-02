"""
    创建目录：os.mkdir(path,mode=0o777)
    mode只针对Linux操作系统
"""
import os
# os.mkdir('./text1')
# os.makedirs('./text1/text2')
"""
    删除目录 可以删除1个目录,目录不存在或者权限不够会报错
"""
os.rmdir('./text1/text2')
"""
改变当前目录  os.chdir(dir)

获取当前目录  os.getcwd()
"""
#获取当前目录
os.getcwd()

#改变当前目录
os.chdir('./')

# 获取当前目录
# dir=fr"C:C:\Users\86132\Desktop\python高级\文件与目录操作\10目录操作.py”
# print(dir)
# os.chdir(fr"C:C:\Users\86132\Desktop\python高级\文件与目录操作\10目录操作.py”)
# print(os.getcwd())

# 列出目录下所有内容 返回的是一个列表
# print(os.listdir('./'))

# 重命名目录
# os.rename('ttest1', '2')

# 检查路径是否为目录
ret = os.path.isdir('2')
print(ret)

# 检查路径是否为文件
ret = os.path.isfile('2')
print(ret)

# 路径拼接 C:\Users\86132\Desktop\python高级\文件与目录操作\10目录操作.py

# os.path.join 会根据操作系统的文件系统约定来正确处理路径分割符
path = os.path.join(fr"C:\Users\86132\Desktop\python高级\文件与目录操作",'10目录操作.py')
print(path)

# 路径拆分:将路径分割成两部分,返回路径和文件名

head,tail = os.path.split('./测试文件夹/1.txt')
print(head)
print(tail)

# 获取绝对路径
path = os.path.abspath('./')
print(path)

# 检查路径是否存在
res = os.path.exists(path)
print(res)