"""
构造函数和析构函数能手动调用
        构造函数:   __init__
            在创建对象时自动调用，目的就是用来初始化属性，可以在需要时定义通过__init__来创建构造函数
        析构函数:
            在对象引用清零时自动调用目的就是用来进行释放资源
            通过__del__来创建构造函数不推荐使用，python有自己的垃圾回收机制会与其冲突

"""
class nTime:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def Gettime(self):
        return self.hour,self.minute,self.second
    def Settime(self,hour,min,sec):
        self.hour = hour
        self.minute = min
        self.second = sec
    def __del__(self):
        pass
#通过构造函数初始化属性
ComputerTime = nTime(14, 48, 55)
print(ComputerTime.Gettime())