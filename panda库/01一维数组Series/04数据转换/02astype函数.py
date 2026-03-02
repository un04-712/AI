"""
    将series数据类型转换成拎一个数据类型
    Series.astype(dtype,copy=True,error='raise)

    dtype:需要转换成的数据类型
    copy: false :尽可能不复制底层数据
    errors:如果设置为raise，则会在转换失败是抛出异常
            ignore则不会抛出异常

"""
import pandas as pd

series = pd.Series([1,2,3,4,])

print(series.dtype)

print(series.astype('float32'))