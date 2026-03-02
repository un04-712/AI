"""
    seek(offset,whence)
    offset:偏移量，可正可负，单位为字节

    whence:
        0 表示从文件开头
        1 当前文件指针位置
        2 表示从文件末尾
        文本模式下只能使用 0

    读取文件指针：
    tell()  返回当前文件指针位置，单位为字节
"""
with open('./测试文件夹/1.txt','rb') as fd:
    fd.seek(2,0)
    # fd.seek(2, 1)
    print(fd.tell())
    fd.seek(0,2)
    print(fd.tell())