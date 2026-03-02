"""
    自定义迭代器应用场景：
        1、生成自定义的数列
        2、按需生成数据
        3、分页查询
"""
class MyIter:
    def __init__(self,end):
        self.end = end
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        num = self.num
        if num < self.end:
            self.num +=1
            return num
        else:
            raise StopIteration

ret = MyIter(5)

for i in ret:
    print(i)




