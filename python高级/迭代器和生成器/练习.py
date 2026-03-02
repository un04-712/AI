class Fi:
    def __init__(self,count):
        self.count = count
        self.ct = 0
        self.a = 0
        self.b = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.ct+=1

        if self.ct<self.count:
            if self.ct == 1:
                self.a = 0
                return 0
            if self.ct == 2:
                self.b = 1
                return 1
            else:
                self.a=self.a+self.b
                self.b = self.a
            return self.a
        else:
            raise StopIteration

fib = Fi(6)
for i in fib:
    print(i)





