"""
    mean:计算数组中元素的平均值
    mean(a,axis=None,out=None,keepdims=<no value>,*,where=<no value>)
    a:原始数据
    keepdims:如果设置为True，计算出来的平均值会保留原始数组的维度
    注意：如果数组是一个空数组，或者指定轴上的所有元素都是空值(nan)则mean()会返回nan
    keepdims = True，则计算的平均值将具有与输入数组相同的维度数，但沿着指定轴的长度为1
"""
import  numpy as np
#计算整个数组的平均值
#一维数组的平均值
a = np.array([1,2,3,4,5])
print(np.mean(a))

#二维数组的平均值
b = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
print(np.mean(b))

#沿着相应的方向计算平均值
#按列求平均值
print('按列求平均值：',np.mean(b,axis=0))
#按行求平均值
print('按行求平均值：',np.mean(b,axis=1))

#keepdims参数
b1 = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print('按列求平均值',np.mean(b,axis=0,keepdims=True))
print('按列求平均值',np.mean(b,axis=1,keepdims=True))

#数组为空处理方式  np.mean中如果数组为空，会返回nan
c_empty = np.array([])
print('空数组：',c_empty.shape)
print('空数组的平均值：',np.mean(c_empty))

#指定轴上有nan的值
c1 = np.array([[np.nan,2,3],
              [4,5,6],
              [7,8,np.nan]])
print('c1数组的平均值：',np.mean(c1,axis=1))