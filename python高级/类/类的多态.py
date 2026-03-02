# 多态体现
str1 = 'abcdef'
Ls1 = [1,2,3]
tp1 = (1,2,3)
dic = {1:1,2:2,3:3}
print(len(str1))
print(len(Ls1))
print(len(tp1))
print(len(dic))

# 鸭子模型:我想要一只鸭子,但我没有鸭子,但是我有一只鸡,这只鸡
# 走路像鸭子,叫声也像鸭子,这只鸡拥有鸭子的功能,那么我就认为这只鸡就是鸭子

class Cat:
    def say(self):
        print('miao~~~~~')
class Dog:
    def say(self):
        print('wang~~~~~')
class Sheep:
    def say(self):
            print('mie~~~~~')
dog = Dog()
cat = Cat()
sheep = Sheep()
def call(x):
    x.say()
call(dog)
call(cat)
call(sheep)
