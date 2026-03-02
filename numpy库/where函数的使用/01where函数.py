"""
    where:可以根据条件返回满足条件的元素索引
    numpy.where(condition)

"""
import numpy as np

#根据条件返回索引
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a > 4)
b = np.where(np.array(a > 4))
print(b)

#2、根据条件选择元素
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#如果元素大于3，返回大于3，否则返回小于等于3

result = np.where(a > 3, '大于3', '小于等于3')
print(result)
