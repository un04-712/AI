# 实例属性：属于对象本身的属性，存在于__init__函数中，在对象创建时候会赋值给对象。

#对象能访问类属性和实例属性，但无法修改类属性
#实例属性的访问:对象.实例属性名  self.实例属性名
#如果要修改类属性 类.类属性 = 要修改的值

class Person:
     #类属性
    a = 1
    def __init__ (self,name,age,gender) :
        # 实例属性
        self.name = name
        self.age = age
        self.gender = gender
    def changA (self,A):
        a = A

Person1 = Person('zhangsan',10,'man')
Person2 = Person('zmh',10,'man')

print(Person1.name)
print(Person1.a)
Person1.a = 3
Person1.name = 'alice'
# Person.a = 4
print(Person1.a)
print(Person.a)
print(Person2.a)