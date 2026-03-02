"""
    add :用来向可变集合中添加单个元素
    update:一次添加多个元素，比如一个字符串、元组，列表   注意(是逐个添加单个元素)
"""
set1 = {1,2,3,5}
set1.add('hello,world')
print(set1)


set1 = {1,2,3,5}
set1.update((2,3,4,'34','true'))
set1.update('hello,world')
print(set1)
set1.update('true')
print(set1)


