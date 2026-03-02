#监测文件有没有新增内容，如果有显示新增内容

with open('./测试文件夹/1.txt','rt')as fd:
    fd.seek(0,2)
    fd.write(b'fw')