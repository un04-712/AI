"""
    read(size):size是可选参数
    在文本模式下，一次最多读取文件指针后面size个大小的字符
    在二进制模式下，一次最多读取文件指针后面size个大小的字节
    默认size = -1 表示一次性读取文件指针后面所有内容并将字符串返回


    readline() 从文件读取单行数据，返回的是字符串
    readlines() 从文件读取所有行数据，返回的是一个列表
"""

# # res=open('./测试文件夹/1.txt','rt',encoding='utf-8')#以文本模式进行打开
# res=open('./测试文件夹/1.txt','r',encoding='utf-8')#以文本模式进行打开 默认为文本模式
# read_str = res.read(3)
# print(read_str)
#
# print('*'*100)
#
# res=open('./测试文件夹/1.txt','rb')#以二进制模式进行打开
# read_str = res.read(3)
# print(read_str)
# print('*'*100)
#
# # 读取单行数据
# res= open('./测试文件夹/1.txt','r',encoding='utf-8')#以文本模式进行打开 默认为文本模式
# read_str = res.readline ()
# print(read_str)
# print('*'*100)
#
# # 读取多行数据
# res=open('./测试文件夹/1.txt','r',encoding='utf-8')#以文本模式进行打开 默认为文本模式
# read_str = res.readlines()
# print(read_str)
# print('*'*100)

"""分块读出所有数据  （解决大文件读取问题）"""
f =  open('./测试文件夹/1.txt','rt',encoding='utf-8')
print(f.readlines())
# 从文件中读取所有行  将每一行的数据存到列表中
# 方法一 只针对文本文件
# while True:
#     res =  f.readline()
#     if res == '':
#         break
#     print(bytes(res,'utf-8'))
#
# print(":",f.readline())
# print(":",f.readline())

# 方法二  只针对文本文件
for line in f:
    print('shjds',type(line))

# 方法三： 通用
while True:
    res =  f.read(1024)
    if res == '':
        break
    print(res)


#write: 将str的内容覆盖到当前文件指针位置的后面,并将文件指针移动到新的写入位置。返回写入的字符数量。
#注意:写入其他类型的对象时,要先将他们转换为字符串或字节对象,写入完成返回写入的字符个数

#writelines

# 写入单个字符串
res= open('./测试文件夹/1.txt','a',encoding='utf-8')
num = res.write('abc')
print(num)

print('*'*100)

# 写入多个字符串
res=open('./测试文件夹/1.txt','a',encoding='utf-8')
res. writelines([ 'def' ,
                  '你好'
                  ,'666'])


#b模式下的读操作
with open('./测试文件夹/1.txt','rb')as fd:
    data = fd.read()#对于中文来说，utf-8 三个字节表示一个中文
    print(data)
    print(type(data))
    print(data.decode('utf-8'))

#b模式下的写操作
with open('./测试文件夹/1.txt','wb')as fd:
    #data = fd.write(b'fw')
    data1 = fd.write('三千道天下间'.encode('utf-8'))