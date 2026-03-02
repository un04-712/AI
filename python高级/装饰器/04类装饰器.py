"""
    除了可以自定义一个新的函数用作装饰器之外，也可以将类作为装饰器，为被装饰的函数添加新的功能，类装饰器通过实现类的的__call__方法，
    使得类的实例可以被当作函数来调用从而实现对其他函数的装饰
"""
class MyDecorator:
    def __init__(self,func):
        self.func = func
    def __call__(self,*args,**kwargs):
        print('开始执行')
        result = self.func(*args, **kwargs)
        print('执行完毕')
        return result
@MyDecorator # say_hello = MyDecorator(say_hello) 1 usage
def say_hello(name):
    print(f'hello,{name}')
say_hello('lisi')