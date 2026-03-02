#生成一个迭代器，可以产生一亿个值的迭代器
l = [1,2,3]
l.__iter__()
l = range(10000000)
l.__iter__()

#生成器：不依赖于range和其他数据类型就可以直接定义出来的迭代器方法
"""
    生成器：是一种特殊的迭代器，可以在需要时，动态生成值，避免一次性生成所有值所占用大量内存。
    生成器使用yield语句来产生值。
    可以通过迭代器方法逐个获取生成器的值，生成器可以在循环中被逐个迭代，从而实现高效处理
    大量数据或者无限序列。在python中，生成器可以通过函数定义和生成器表达式来创建
"""
def func():
    print('第一次执行')
    yield 1
    print('第二次执行')
    yield 2
    print('第三次执行')
    yield 3
    print('第四次执行')
    yield 4
    print('第五次执行')

# res = func()
# iter(res)
# print(res)
# print(next(res))   #res.__next__() = next(res) len(l) = l.__len__()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

#生成一个生成器对象，生成一亿个0~1的随机浮点数
import random
def generate_random_floats(limit):
    while limit > 0 :
        yield random. uniform( 0, 1)
        limit -= 1
gen = generate_random_floats(100000000)

for i, value in enumerate(gen):
    if i<100:
        print(value)
    else :
        break
def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
fib = fibonacci()

for _ in range(10):
    print(next(fib))

help(enumerate)
