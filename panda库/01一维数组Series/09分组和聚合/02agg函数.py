"""
    Series.agg(func=None,axis=0,*args,**kwargs)
    func():实际函数
"""
import pandas as pd

s = pd.Series([1,2,3,4,5])
#计算平均值
print(s.agg('mean'))
#计算最大值最小值
print(s.agg(['max','min']))

#使用字典为聚合函数命名
print(s.agg({'Maximum':'max','Minimum':'min'}))

#使用自定义函数进行聚合

print(s.agg(lambda x,power:(x**power).sum(),power=2))
