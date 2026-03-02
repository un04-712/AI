# 类方法:属于类本身的方法,用来访问和修改类属性,不能访问实例属性
# 类方法的修饰符:@classmethod

"""
                            类方法                  静态方法                         实例方法
绑定对象                      cls                   无绑定对象                         self
是否能直接访问类属性            cls                   不可以                             self
是否能访问实例属性             不可以                   不可以                            self
使用场景               操作类属性,创建类的实例  工具方法,与类相关但不依赖类或实例属性           操作实例属性
"""
class Person:
    name = 'zhangsan'
    def chang_name(cls,name):
        cls.name = name
        print(cls)


print(Person)
person = Person()
print(person.name)
person.chang_name('lisi')
print(person.name)








