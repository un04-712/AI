"""
    with语句 是一种上下文管理器，用于简化资源打开和关闭的过程，确保资源在不需要时得到适当的释放

"""
with open('./测试文件夹/1.txt','a',encoding='utf-8') as fd:
    fd.writelines(['def','你好'])