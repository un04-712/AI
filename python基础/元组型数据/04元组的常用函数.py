"""
    len         获取队列长度
    max         返回元组中元素最大值
    min         返回元组中元素最小值
    in 和 not in判断元素是否在元组内
    del         删除元组
"""
tuple1 = (1,2,3,4)
print(len(tuple1))

tuple1 = (1,2,3,4)
print(max(tuple1))

tuple1 = (1,2,3,4)
print(min(tuple1))


tp1 = (1,54,6,3,5,9,45)

# in
if 3 in tp1:
    print('3在元组中')

if 100 not in tp1:
    print('100不在元组中')