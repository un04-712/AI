"""
    opp(面向过程)
    面向过程是一种以‘过程’(或函数)为中心的编程思想
    它强调通过一系列顺序执行的步骤来完成任务。
    在面向过程编程中，程序通常由一组函数或过程来完成，这些函数对数据进行操作，数据和操作他们的代码是分开的


    oop(面向对象)
    面向对象是一种以'对象'为中心的编程思想
    对象是由数据和操作这些数据的方法组成的实体。
    在opp中，程序被视为一组互相交互的对象，这些对象通过方法来操作内部数据，从而实现功能
"""
#编程:面向数据和功能
#面向对象 : 一切流程化,执行细节
#面向过程 : 一切框架化,顶层设计  高级容器: 数据类型，方法及方法定义
from platform import libc_ver

"""
    类的创建：
            class 类名;
                pass

"""
class GameObject:
    #类属性
    hp = 100
    level = 1
    attack = 100
    # 类方法
    def changelv(self,lv):
        print(f'等级升为:{lv}')
        level = lv
    def changehp(self, hp):
        print(f'等级升为:{hp}')
        hp = hp


#创建对象，也叫做类的实例化
"""
    对象与类之前的关系：
                1、对象拥有类所定义的全部属性和行为
                2、对象的属性和行为可以单独进行增加、修改、删除
                3、对象不能单独创建，必须依托于类的实例化，一个类可以实例化多个对象
                4、对象之间的属性和行为不共享
"""
hero1 = GameObject()
hero2 = GameObject()
hero3 = GameObject()
hero1.changelv(100)
hero1.changehp(1000)
hero1.hp = 2000
hero2.hp = 1000
print(hero1.hp)
print(hero2.hp)
print(hero1.level)
print(hero1.attack)

#对象属性的增加，如果对象属性存在会被修改，不存在会为对象创建一个新的属性
hero1.skill = {'slill':60}
print(hero1.skill)

#对象属性的删除   del 类.属性名

del hero1.skill
print(hero1.skill)

# 方法修改
def changelv(self, lv):
    print(f"等级升至力{100}")
    level = 100

from types import MethodType

hero1.changeLv = MethodType(changelv,hero1)
hero1.changeLv(59)