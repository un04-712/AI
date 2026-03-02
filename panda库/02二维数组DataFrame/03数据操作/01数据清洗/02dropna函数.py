"""
    DataFrame. dropna(axis=0, how=any, thresh=None, subset=None, inplace=False, ignore_index=False)
    axis:0 表示按行删除 1 表示按列删除
    how:
        any: 如果行列中的任意一个值是NaN, 就删除该行或该列
        all:如果行或列中的所有值都是nan,才删除该行或该列
    thresh:指定每行或每列至少需要有多少个非缺失值才能保留,如果设置此参数,how参数将被忽略
    subset:指定在哪些列中搜索缺失值。如果未指定,则在所有列中搜索
    inplace:是否修改dataframe而不是创建新的dataframe
    ignore_Index:是否重置索引


"""
import  numpy as np
import pandas as pd
data={
    '编号':[np.nan,np.nan,np.nan],
    '姓名':['小明','小刚','小红'],
    '年龄':[20,np.nan,19],
    '成绩':[78,64,89]
}
df = pd.DataFrame(data)
print(df)

# 按行去丢弃nan值
print (df.dropna(how='all'))

# 按列去丢去缺失值
print(df.dropna(axis = 1))