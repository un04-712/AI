"""
    super函数:严格根据mro继承顺序去搜索父类指定的函数，并且直接绑定好
"""


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


class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("C")


c = C()
