"""
    可变集合的删除
    remove  删除指定的元素，如果不存在就会报错
    discard 删除指定的元素，如果不存在不会报错
    pop     删除集合在内存中第一个元素，返回删除的元素
    clear   清空集合
    del     删除对象

"""

set1 = {1,2,3,4,5}
set1.remove(3)
print(set1)

set1 = {1,2,3,4,5}
set1.discard(9)
print(set1)

set1 = {1,2,3,4,5}
print(set1.pop())
print(set1)

set1 = {1,2,3,4,5}
set1.clear()
print(set1)

set1 = {1,2,3,4,5}
del set1
print(set1)