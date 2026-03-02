"""
    类的多继承：一个类有多个父类
    多继承格式：
            class name(继承1，继承2…………)
    注意：多继承有可能导致继承冲突，比如父类和多个子类有相同的属性和方法，此时
    如果需要使用该属性和方法：
    继承优先级: 子类>从左到右第一个父类>第二个父类>第三个父类…………
    对于复杂的关系使用子类mro()的方法来获取继承顺序
"""
class A:
    a = 100
    def say(self):
        print('我是A')
    def run(self):
        print('我会跑步')
class B:
    a = 200
    def say(self):
        print('我是B')
    def swim(self):
        print('我会游泳')
class C(A,B):
    pass
c = C()
print(c.a)
c.say()
c.swim()