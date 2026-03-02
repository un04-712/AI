#通过文件编程，将user.txt拷贝一份user

# 这种只能针对文本文件
# with open('./测试文件夹/user.txt','rt',encoding='utf-8') as f1,\
#      open('./测试文件夹/user(副本).txt','wt',encoding='utf-8') as f2:
#      res=f1.read() # 将原始文件内容读取出来
#      f2.write(res) # 将原始文件内容写入新文件

# 通用文件拷贝                   C:\Users\pg\Desktop\2501寒假班\18文件和目录操作\r测试文件夹\1.png
old_path=input('请输入原始文件路径>>>').strip()
new_path= input('请输入新文件路径>>>').strip()
with open(fr'{old_path}','rb') as f1,\
     open(fr'{new_path}','wb') as f2:
    res=f1.read() # 将原始文件内容读取出来 #方案一
    for line in f1: # 方案二
            f2.write(line)
            #print(line)

# 方案三
#     while True:
#         res = f1.read(1024)
#         if not res:
#             break
#         f2.write(res)
#         print(res)


import shutil
old_path=input('请输入原始文件路径>>>').strip()
new_path= input('请输入新文件路径>>>').strip()
print(old_path)
#拷贝文件
# shutil.copy(old_path,new_path)
#拷贝目录
# shutil.copytree(old_path,new_path)