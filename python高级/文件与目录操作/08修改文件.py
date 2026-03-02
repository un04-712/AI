"""
    user.txt :我喜欢吃苹果

    通过程序将user.txt中的内容修改为我不喜欢吃苹果

"""
with open('./测试文件夹/2.txt','r+',encoding='utf-8')as fd:
    data = fd.read()
    res = data.replace('喜欢','不喜欢')
with open('./测试文件夹/2.txt','w',encoding='utf-8')as fd:
    fd.write(res)
 