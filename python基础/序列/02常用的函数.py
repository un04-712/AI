"""
    max         返回序列中元素最大值
    min         返回序列中元素最小值
    sum         对序列中的元素进行求和
    sorted      对序列进行排序
    reversed    对序列进行反转
    all         用于判断序列中的元素是否都为真
    any         用于判断序列中的某个元素是否都为真
    enumerate   将序列下标与元素进行组对，下标参数可以通过start参数进行修改返回的是enumerate类型
    zip         将多个序列中对应的元素进行组合，放到一个元组里（注意：多个要操作的序列程度不同时，以最短的为主，多出来的元素会被丢掉）
    map         对可迭代对象中的每个元素应用一个指定的函数，然后返回一个包含所有函数的调用结果的迭代器，需要强转才可以进行输出
    filter      会根据提供的函数对指定的可迭代对象的每个元素进行运算，并将运算结果为真的元素以迭代器的形式返回

"""
from audioop import reverse

# a = (1,2,3,4,5,6)
# print(sum(a))
#
# s = 'sgavg'
# print(sorted(s))

s1 = [1,2,3,4,0,6]
print(enumerate(s1))
print(all(s1))
print(any(s1))

# def my_function(x):
#     return x * 2
#
# lst = [1, 2, 3, 4, 5]
# result = list(map(my_function, lst))
# print(result)  # 输出: [2, 4, 6, 8, 10]
#
# user_input = tuple(input('请输入六个不同的整数:'))
# res = map(user_input)
# print(res)
