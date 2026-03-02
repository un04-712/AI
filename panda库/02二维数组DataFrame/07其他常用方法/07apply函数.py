"""
    对DataFrame中的每个元素应用与一个函数，并返回一个结果DataFrame

    DataFrame.apply(func,axis=0,raw=False,result_type,args=(),**args)

    func:函数
    raw:
    result_type:
            reduce  尽可能返回一个列表，这个列表会被转换为一个Series
            broadcast:结果会被广播到原始dataFrame,保留原始的索引相同
            expand:如果应用函数返回一个列表，则这个列表会转换成多个列，意味着每个列表元素都会变成DataFrame的一列

    args:函数位置参数
    **kwargs:函数的关键字不定长参数

"""

import pandas as pd
df = pd.DataFrame(
    {
        'A':[1,2,3],
        'B':[4,5,6],
        'C':[7,8,9],
    }
)

print(df.apply(lambda x:x.mean(),axis=0))
