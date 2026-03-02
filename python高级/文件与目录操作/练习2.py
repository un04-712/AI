"""
    1.	已知文本文件中存放了若干数字,请编写程序读取所有数字,排序以后进行输出。
文本文件内容为：12 213 423 45 12
"""
# with open(r'./测试文件夹/3.txt','r') as fi:
#     res = fi.read()
#     print(res)
# list1 = []
# for i in res.split():
#     list1.append(int(i))
# list1.sort()
#
# for n in list1:
#     print(n,end=' ')

"""
    2.	读取文本内容，将所有字母变成小写重新写入到文件。
文本文件内容为：GGagKKfsggggGGSg
"""
# with open(r'./测试文件夹/4.txt','r+') as fd:
#     str1 = fd.read().lower()
#     print(str1)
#     fd.write(str1)

"""
    3.编写一个 Python 程序，实现将一个文件的内容复制到另一个文件的功能。程序需要满足以下要求：
- 通过命令行交互方式获取用户输入的源文件路径和目标文件路径
-  同时支持文本文件和图片文件的复制
"""
# old_path=input('请输入原始文件路径>>>').strip()
# new_path= input('请输入新文件路径>>>').strip()
# with open(fr'{old_path}','rb') as f1,\
#      open(fr'{new_path}','wb') as f2:
#     for line in f1:
#          f2.write(line)
#          print(line)



print(f"{'登录界面':*^20}")
print(f"{'1注册':^20}")
print(f"{'2登录':^20}")
user_input = input("请选择你的功能:")
if user_input == '1':
    name = input("请输入你要注册的账号:")
    word = input("请输入你要注册的密码:")
    with open('./测试文件夹/3.txt','a',encoding='utf-8') as fd:
        fd.write(f"{name}:{word}\n")
    print("用户注册成功")
if user_input =='2':
    count = input("请输入你要登录的账号:")
    password = input("请输入你要登录的密码:")
    with open('./测试文件夹/3.txt', 'r', encoding='utf-8') as fi:
        user_count = fi.readlines()
        for i in user_count:
            if  i.split(':')[0].strip()==count  and  i.split(':')[-1].strip()== password:
                print('用户登录成功')

