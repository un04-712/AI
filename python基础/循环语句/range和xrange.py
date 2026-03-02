# coding=utf-8
#在python3 range函数返回的是一个可迭代的对象，并不是列表类型，所以不会打印列表  input

#在python2 range函数返回的是一个列表
#在python2 xrange函数返回的是一个迭代器   在python3  raw_input
#内存开销量
"""
当我们要生生成很大的数字序列的时候，用xrange会比range性能优很多，因为不需要一上来就开辟一块很大的内存空间
"""
print(range(10))
print(range(0,10))

