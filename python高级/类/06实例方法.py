# 实例方法：第一个参数传入self参数，没有实例化前，无法调用，实例化后，也只能使用对象来调用而不是类来调用

class Person:
    def __init__(self,name):
        #实例属性
        self.name = name
    def changename(self,name):
        self.name = name
    def say(self):
        print(f'我的名字叫{self.name}')
person = Person('zhangsan')
person.say()
person.changename('lisi')
person.say()