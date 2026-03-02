"""
    查找：查看某元素是否存在于该列表里，
    count():返回列表中某个元素的数量
    in 或者 not in   判断元素是否在列表中
    index
"""
from operator import index

#count  返回列表中某个元素的数量
list1 = [1,23,4,34,5,2,3,5,2,5,6,2]
print(list1.count(3))

# in
if 3 in list1:
    print('3在列表中')

if 100 not in list1:
    print('100不在列表中')

#index()
list1 = [1,23,4,34,5,2,3,5,2,5,6,2]
print(list1.index(3,5,7))