"""
        用于替换dataframe中的内容
    DataFrame.replace(to_replace=None, value =_ NoDefault.no_default, inplace=False, limit=None,
regex=False, method =_ NoDefault.no_default)

    to_replace:可以是标量 列表 字典 正则 如果是字典，键就是要替换的值，值就是替换后的值
    value:替换后的值，标量，列表，数组，与to_place长度相同
    inplace:是否在原数组上修改
    limit:限制替换的数量
    regex:是否使用正则
    method:
        'ffill'  'bfill'
"""

import pandas as pd
import numpy as np
data={
    '编号':[np.nan,np.nan,323],
    '姓名':['小明','小刚',np.nan],
    '年龄':[89,np.nan,64],
    '成绩':[78,64,89]
}
df = pd.DataFrame(data)
print(df)

# 单一值替换
print(df.replace(np.nan,-1))

# 列表替换所有的匹配的值
print(df.replace([89,64, 78, 323],'a' ) )

# 字典替换所有匹配的值
print(df.replace({89 :- 89,64 :- 64}))

# 使用正则表达式替换
import pandas as pd

df = pd.DataFrame({
'col1': ['apple', 'banana', 'cherry', 'agerape' , 'apricote' ],
'col2': ['apple pie', 'banana split', 'cherry tart', 'grape juice', 'apricote jam']
})
print(df)

# 将a开头的和e结尾的字符串替换成fruit
print(df.replace(to_replace=r'^a .* e$', value='fruit', regex=True))