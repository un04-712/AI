"""
        不可变集合 用frozenset函数需要填入一个参数
        该参数是一个序列,可迭代对象


"""
a = frozenset([1,2,3])
print(type(a))
for i in a:
   print(i)