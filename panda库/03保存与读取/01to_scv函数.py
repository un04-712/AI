"""
    DataFrame.to_csv(path_or_buf=None, sep=',',
    na_rep='',float_format=None, columns=None,
    header=True, index=True, mode='w', encoding=None,
    quoting=None, quotechar='"', **kwargs)

    path_or_buf:文件名
    sep : 分隔符 ,通常使用逗号或制表符
    na_rep:缺失值的表示方式,默认
    float_format:浮点数的格式化方法，例如&.2f来表示保留两位小数
    header:是否写入列名
    index:是否写入行名
    mode:通常是先w后a
    encoding:字符编码格式'utf-8'
    quoting:控制字段的引用方式
    quotechar:用于包围字段的字符默认为“”
    **kwargs:

"""

import pandas as pd
# 创建一个简单的DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [28, 34, 29],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
# 将DataFrame保存为Excel文件
df.to_csv('员工信息.csv', index=False,encoding='utf-8')
