"""
    用于检测Dataframe中的缺失值,它会返回一个相同形状的布尔型dataframe,其中每个元素原始dataframe中相同
位置的元素是否右缺失值

"""
import  numpy as np
import pandas as pd
data={
    '编号':[1,2,3],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,np.nan,19],
    '成绩':[78,64,np.nan]
}
df = pd.DataFrame(data)
print(df.isnull())
print(df[df.isnull()])