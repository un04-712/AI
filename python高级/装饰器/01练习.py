
import time# 函数加验证功能
def auth(func):
    def wrapper(*args, ** kwargs):
        name=input('请输入账号>>>').strip()
        pwd=input('请输入密码>>>').strip()
        if name == 'lisi' and pwd == '123456':
            func(home)
            print(f"欢迎{name}注册成功")
        else:
            print("输入错误,请重新输入")
    return wrapper

@auth # home = auth(home) 1 usage
def home ():
    time.sleep(2)
    print ('welcome to home')
home ()
