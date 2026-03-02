"""
    用于对DataFrame中的数据进行转换操作，并返回与原始series具有相同索引的新series
    transform(self, func, axis, *args, **kwargs)

    func:应用与series的函，这个函数可以是内置函数，或者自定义函数
    axis: 0 index 1 columns
    *args,**kwargs:参数传递给func函数
"""
import  pandas as pd
import  numpy as np
df = pd.DataFrame(
    {
        'A':[1,2,3,4,5],
        'B':[10,20,30,40,50],
        'C':[100,200,300,400,500]
    }
)

print(df.transform(lambda x:x**2))