"""
    实现登录和注册 注册的账号和密码用字典保存起来
"""
user_account = {}
print(f"{'用户注册管理系统':*^20}")
print(f"{'1注册':*^20}")
print(f"{'2登录':*^20}")
print(f"{'3退出':*^20}")
user_input = int(input("请选择你输入的选择(1-3):"))
if user_input==1:
    print(f"{'注册功能':*^20}")
    user_username = input("请输入你的账户:")
    user_password = input("请输入你的密码:")
    user_account[user_username] = user_password
    print(f"{'注册成功','欢迎{user_username'}")
