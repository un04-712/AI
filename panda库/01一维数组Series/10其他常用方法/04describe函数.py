"""
    用于生成描述性统计信息，返回一个计数,均值,标准差,最小值,25%分位数,中位数,75%中位数,最大值,的Series

    Series.describe()

    percentiles:数值列表或数值元组，默认为[25,5,75]，表示要包含的数据类型

    include:用于指定包括在结果中的数据类型

    exclude:用于指定要排除在结果中的数据类型

"""

import pandas as pd
import numpy as np

s = pd.Series([1,2,3,1,2,4,np.nan,2,4,5])

print(s.describe())