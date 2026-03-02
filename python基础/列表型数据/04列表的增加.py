"""
    列表的增加API:
                append()    向列表的尾部添加元素      单个元素
                insert()    向列表的指定位置添加元素    单个元素
                extend()    将另一个列表的所有元素添加到本列表的后面        多个元素

"""

#向列表的尾部添加元素

ls1 = [1,2,3,4]
ls1.append(4)
print(ls1)
print('*'*50)
#向列表的指定位置添加元素
ls1 = [1,2,3,4]
ls1.insert(2,5)
print(ls1)
print('*'*50)
#将另一个列表的所有元素添加到本列表的后面
ls1 = [1,2,3,4]
ls2 = ls1
ls2.append(4)
ls1.extend([5,6,7,8,9])
print(ls1)
ls1[3:] = []
print(ls2)

a = [1]
print(a*2)


