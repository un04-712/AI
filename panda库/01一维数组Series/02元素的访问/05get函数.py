"""
    通过标签来获取series中的元素
    pd.Series.get(key,default=None)

    key:你想要获取元素的标签
    default:可选参数，如果key不在标签中，返回这个默认值，如果没有指定，默认为None
"""
import pandas as pd

a = pd.Series(['apple', 'banana', 'cherry'], index=[2, 2, 3])
#获取标签为2的值
print(a.get(2))

#标签不存在，返回提示词
print(a.get(5, 'Notfound'))
