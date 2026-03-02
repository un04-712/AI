"""
    账号的注册 和 登录
    注册； 将账号和密码存入到 user.txt
    登录： 从user.txt匹配账号和密码

"""
HomeMenu_str=\
"""
0 注册
1 登录

"""



print (HomeMenu_str)
user = int(input('请选择功能:'))

if user == 0:
    username=input('请输入你要注册的账号:')
    pwd        =input('请输入你要注册的密码:')
    # seek(offset, whence=0)
    with open('./测试文件夹/user.txt','a')as fd:
        fd.write(f'{username}:{pwd}\n')
    print("用户注册成功")
elif user == 1:
    username = input('请输入你的账号:')
    pwd =input('请输入你的密码:')
    with open('./测试文件夹/user.txt','r')as fd:
        userList=fd.readlines()
    for userItem in userList:

        if username == userItem.split(':') [0].strip() and pwd == userItem.split(':') [-1].strip():
            print('登录成功')
            break
    else:
        print('登录失败')
else:
    pass



