class A:
    def __init__(self):
        print("A")
class B1(A):
    def __init__(self):
        A.__init__(self)
        print("B1")
class B2(A):
    def __init__(self):
        A.__init__(self)
        print("B2")
class C(B1,B2):
    def __init__(self):
        B1.__init__(self)
        B2.__init__(self)
        print("C")
c = C()
