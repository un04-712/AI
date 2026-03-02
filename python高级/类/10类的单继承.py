"""
    在python中，类可以继承，也可以继承其他类
    被继承的类被成为父类或者基类，继承的类叫子类

    子类会继承父类所有的方法和属性，并且一个子类可以有多个父类
    一个父类可以有多个子类
继承格式:
    class Name(要继承的类)
        pass
在python3中。所有的类都有一个共同的父类，叫作object类，即使在自定义自己类时，会默认继承object类
子类会拥有object类所有的属性和方法
在python2中:
    新式类:继承了object
    经典类:没有继承object类

object类:
    __dict__    存放所有属性和方法
    __bases__   查看基类
    __init__    对象初始化
    __eq__      定义操作符 == 的行为
    __iter__    让对象支持迭代
    __next__    在迭代对象中返回下一个值
    __class__   对象所属的类
    __doc__     对象的文档
    __name__    类的名字
    __new__     创建对象时候自动调用的函数，如果当时函数没有返回的对象
                则不会执行初始化函数
"""
class A:
    a = 1
    b = 2
    c = 4
    def say(self):
        print('我是高手A')
    def aaa(self):
        print('who are you')
class B(A):
    a = 3
    b = 4
    def say(self):
        print('我是高手B')
b =B()
print(b.a)
print(b.b)
print(b.c)
print(b.say())