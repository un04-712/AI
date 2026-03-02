"""
    len     计算集合元素的个数
    set     生成一个集合，这里的参数为可迭代对象
    为什么需要set函数：
                    1、创建集合
                    2、强制转换
    copy     返回集合的浅拷贝
    intersection    求两个集合的交集    &   公共部分
    difference      求两个集合的补集    -   在全集之中属于A之外的元素组成的集合
    union           求两个集合的并集    |    两个集合中所有元素的集合
    issubset        求两个集合是不是子集关系
    issuperset      求两个集合是不是父集关系
"""
set1 = set(range(1,10))
print(set1)

my_set1 = { }
print(type(my_set1))
my_set2 = set()
my_set2.difference()
print(type(my_set2))


my_set1 = {1,2,3 }
my_set2 = {1,2,3,4}

print(f'两个集合的交集为{my_set1.intersection(my_set2)}')
print(f'两个集合的交集为{my_set1 & my_set2}')
print(f'两个集合的并集为{my_set1.union(my_set2)}')
print(f'两个集合的并集为{my_set1| my_set2}')
print(f'两个集合的补集为{my_set2.difference(my_set1)}')
print(f'两个集合的补集为{my_set2-my_set1}')
print(f'两个集合的子集为{my_set1.issubset(my_set2)}')
print(f'两个集合的父集为{my_set1.issuperset(my_set2)}')


#集合不能被运算符操作

#集合不能被嵌套
#不可哈希(可变元素) 不可变元素才能被哈希  哈希值是唯一的并且不可逆















