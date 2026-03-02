"""
    sum:计算数组中所有元素的和
    sum(a,axis=None,dtype=None,out=None,keepdims=<no value>,initial=<no value>,where=<no value>)

"""
import numpy as np

#计算整个数据的总和
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.sum(a))

#2沿着相应方向求和
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(np.sum(b))

#沿着相应的方向计算和
#按列求和
print('按列求和：', np.sum(b, axis=0))
#按行求和
print('按行求和：', np.sum(b, axis=1))


#initial 为求和参数提供一个初始值，这个初始值会添加到求和结果中


#where参数的使用
#沿轴求和，设置条件大于5
print('按列求和：', np.sum(b, axis=0, where=b > 5))
