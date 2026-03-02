"""
    self:是一个参数，表示对象自身，里面存放的是对象自身的地址，如果希望类中的方法可以被对象使用
    那么第一个参数必须是self,其作用对象与类的方法进行绑定，这样才能让每个对象都能调用属于自己的实例方法

"""
class Dog:
    def speak(self):
        print(f"{self}在说话")
        self.speak()
dog1 = Dog()
dog1.speak()
