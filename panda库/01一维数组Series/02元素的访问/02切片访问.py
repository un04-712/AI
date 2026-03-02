"""
    切片
        位置切片  不包含终止值
        标签切片  包含终止值
    注意事项 : 当标签和位置产生冲突时,位置切片的优先级大于索引切片

"""




import pandas as pd
import numpy as np
"""
    位置切片
"""
series = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(series[1:3])

"""
    标签切片  
"""
series = pd.Series(np.arange(5),index=['a','b','c','d','e'])
print(series['a':'d'])