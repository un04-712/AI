"""
    argmax和argmin分别用于找出数组中最大值最小值索引位置
    argmax(a, axis=None, out=None, *, keepdims=<no value>)
    argmin(a, axis=None, out=None, *, keepdims=<no value>)
    axis:如果为None,在展平的数组中进行搜索，如果指定了轴，会沿着轴进行搜索，并返回
"""
import numpy as np

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

max_index = np.argmax(b)
min_index = np.argmin(b)

print(max_index)
print(min_index)
