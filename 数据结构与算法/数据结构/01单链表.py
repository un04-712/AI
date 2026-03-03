"""
    单链表是一种线性的数据结构，由一系列节点组成，这些节点按照特定的顺序排列，通过指针相互连接在一起

    节点结构: data(存储的数据)  next(存储下一个节点的位置)

    优点:
        动态数据集合:
        元素顺序:
        内存效率:
        避免数组扩容:

"""

# 创建节点类型
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # 指向下一个节点
# 创建单链表类型
class SinglyLinkedList:
    def __init__(self):
        self.head = None # 头节点
        self.length = 0  # 链表长度

    def is_empty(self):
        return self.length == 0

    def insert(self,index,value):
        """
            index: 表示要插入位置的索引
            value: 要插入的值
        """
        # 判断index是否为合法的范围   0 <= index<=length
        if not  0<=index<=self.length:
            print(f"位置{index}不对，插个毛")
            return False
        new_node =  Node(value)  # 创建节点
        if index==0:  # 插在头部
             # 链表为空
             if self.is_empty():
                 self.head = new_node
              # 链表不为空
             else:
                 new_node.next = self.head
                 self.head = new_node
        else:    # 插在中间或尾部
            current_node =self.head
            for _ in range(index-1):
                current_node = current_node.next
            # 新节点存储当前的下一个节点地址
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1
        return True


    def delete(self,index):
        if not self.is_empty(): #数据不为空
            if not 0 <= index <= self.length:
                print(f"位置{index}不对，插个毛")
                return False
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            current_node.next = current_node.next.next
        self.length -=1

    def find(self,value):
        """
            查找 ： 按值查位置
        """
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == value:
                print(f"找到了! {value}在位置{index}")
                return index
            current_node = current_node.next
            index += 1
        print(f"{value}不在这儿!")
        return -1


    # 遍历数据
    def display(self):
        # 判断是否有数据
        if not self.is_empty() :
            current_node = self.head
            print('链表里有,', end='')
            while current_node is not None:
                print(current_node.data,end='->')
                current_node = current_node.next

        print('None')
# 测试一把
if __name__ == '__main__':
    sl = SinglyLinkedList()
    sl.insert(0,666)   # 往头部插
    sl.insert(1, 111)  # 往尾部插
    sl.insert(2, 222)
    sl.insert(3, 333)
    sl.insert(2, 2222) # 往中间插
    sl.insert(0, 100)  # 往头部插
    sl.insert(6, 6666)    # 往尾部插
    sl.insert(7,999)

    sl.display()
    sl.delete(0)
    sl.display()
