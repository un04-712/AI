"""
    max:返回数组中的最大值或者沿相应方向的最大值
    min:返回数组中的最小值或者沿相应方向的最小值
    max(a,axis=None,out=None,keepdims=<no value>,initial=<no value>,where=<no value>)
    min(a,axis=None,out=None,keepdims=<no value>,initial=<no value>,where=<no value>)

"""
import numpy as np
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
#
print(np.max(b),np.min(b))

#沿着行方向求出最大值
print((np.max(b,axis=1)))

#沿着列方向求出最大值
print((np.max(b,axis=1,initial=8)))

#where参数的用法

