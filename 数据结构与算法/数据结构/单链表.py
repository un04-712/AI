class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    def is_empty(self):
        return self.length ==0
    def insert(self,index,value):
        if not 0<=index<=self.length:
            print('索引都超了你还插个毛线')
            return False
        if index ==0:
            if self.is_empty:


