
def outer3(func):
    def wrapper(*args, ** kwargs):
        print('开始执行outer3.wrapper')
        res = func(*args, **kwargs)
        print('outer3.wrapper执行完毕')
        return res
    return wrapper

def g_outer2(x):
    def outer2(func) :
        def wrapper(*args, ** kwargs):
            print('开始执行outer2.wrapper')
            res = func(*args, **kwargs)
            print('outer2.wrapper执行完毕')
            return res
        return wrapper
    return outer2

def outer1(func):
    def wrapper(*args, ** kwargs):
        print('开始执行outer1.wrapper')
        res = func(*args, ** kwargs)
        print('outer1.wrapper执行完毕')
        return res
    return wrapper
# 装饰器的叠加的加载顺序:先outer1->outer2(10)->outer3
@outer3# home = outer3(home)  home=>outer3.wrapper 1 usage
#@g_outer2(10) # @g_outer2(10) => @outer2 => home = outer2(home)home=>outer2.wrapper
@outer1 # home = outer1(home)   home=>outer1.wrapper

def home (z):
    print('执行home功能',z)
home (0)

# print('开始执行outer3.wrapper')
# print('开始执行outer2.wrapper')
# print('开始执行outer1.wrapper')
#home (0)
# print('outer1.wrapper执行完毕')
# print('outer2.wrapper执行完毕')
# print('outer3.wrapper执行完毕')




