
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def run(self):
        return self.x+self.y
class B(A):
    def __init__(self,x,y,z):
        A.__init__(self,x,y)
        self.z = z
    def run(self):
        return A.run(self)+self.z

b = B(6,6,6)
print(b.run())