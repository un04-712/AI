"""
    类的封装：将数据和方法封装到一个类中，并且通过设置访问权限
    可以将类的属性和方法隐藏在类的内部，可以防止类的属性和方法
    被外部直接访问和修改，提高代码的安全性和可维护性
        _(单下划线)：表示该属性或方法是内部使用，这是人为规定的。外部可以访问
        __(双下划线)：真正设置私有权限的方法，属性或者方法一旦被设置私有外部将无法访问
        __ __(双下划线前后缀):表示python中特殊的属性和方法，有特殊的意义和用途，不推荐自己定义
"""
#设置私有权限
class Person:
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.num = '138xxxxxxxx'
    def __say(self):
        print(f'我的密码是：{self.password}')
    def say1(self):
        print(f'我的密码是：{self.password}')
p1 =Person('zmh',1232)
print(p1.name)

print(Person.__dict__)

