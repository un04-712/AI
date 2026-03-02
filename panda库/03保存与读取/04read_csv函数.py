

"""
    pandas.read_csv 是一个非常强大的函数，用于从文件、URL、文件-like对象等读取逗号分隔值（CSV）文件。
    这个函数有很多参数，允许你以多种方式自定义数据加载过程。
        pandas.read_csv(filepath_or_buffer, sep, header, usercols,na_values, parse_dates, skiprows, nrows)
    filepath_or_buffer ：指定要读取的 CSV 文件的路径或文件对象。可以是一个字符串，表示文件的绝对路径或相对路径；
    也可以是一个已经打开的文件对象（例如通过 open() 函数打开的文件）。
    sep : 字符串，用于分隔字段的字符。默认是逗号 , ，但可以是任何字符，例如';' 或 '\t' （制表符）。
    header : 整数或整数列表，用于指定行号作为列名，或者没有列名（例如header=None ）。默认为 'infer' ，表示自动检测列名。
    usecols : 列表或 callable，用于指定要读取的列。可以是列名的列表，也可以是列号的列表。
    na_values : 字符串、列表或字典，用于指定哪些其他值应该被视为 NA / NaN 。
    parse_dates : 列表或字典，用于指定将哪些列解析为日期。
    skiprows : 整数或列表，用于指定要跳过的行号或条件。
    nrows : 整数，用于指定要读取的行数。

"""
import pandas as pd

data = pd.read_csv('./员工信息.csv',nrows=1)
print(data)
