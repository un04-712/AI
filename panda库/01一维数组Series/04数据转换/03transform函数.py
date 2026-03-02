"""
    用于对series中的数据进行转换操作，并返回与原始series具有相同索引的新series
    transform(self, func, axis, *args, **kwargs)

    func:应用与series的函，这个函数可以是内置函数，或者自定义函数
    axis:
    *args,**kwargs:参数传递给func函数
"""
import pandas as pd


series = pd.Series([1,2,3,4,5])
print(list(map(lambda x:x**2,series)))

print(series.transform(lambda x:x**2))