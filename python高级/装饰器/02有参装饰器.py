import time# 函数加验证功能
def auth(source):
    def outer(func):
        def wrapper(*args, ** kwargs):
            name=input('请输入账号>>>').strip()
            pwd=input('请输入密码>>>').strip()
            if source =='file':
                print('基于文件的登录验证')
                if name == 'lisi' and pwd == '123456':
                    func()
                    print(f"欢迎{name}注册成功")
                else:
                    print("输入错误,请重新输入")
            elif source =='mysql':
                print('基于mysql的登录验证')
            elif source =='access':
                print('基于access的登录验证')
        return wrapper
    return outer
@auth('file') # outer = auth('source') => @outer => home = outer(home)
def home ():
    time.sleep(2)
    print ('welcome to home')
home ()


#有参装饰器模板
def auth(x):
    def outer(func):
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapper
    return outer