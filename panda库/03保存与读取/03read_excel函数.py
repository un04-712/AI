"""
    pandas.read_excel 是pandas库中用于读取Excel文件（ .xls 或 .xlsx ）的函数。
    它可以将Excel文件中的数据读取为DataFrame对象，便于进行数据分析和处理。
        pandas.read_excel(io, sheet_name=0, header=0, index_col=None,usecols=None,
        squeeze=False, dtype=None, skiprows=None,nrows=None, na_values=None,
        keep_default_na=True,parse_dates=False, date_parser=None, skipfooter=0,convert_float=True, **kwds)
    io : 文件路径或文件对象。这是唯一必需的参数，用于指定要读取的Excel文件。
    sheet_name=0 : 要读取的表名或表的索引号。默认为0，表示读取第一个工作表。可以指定工作表名或索引号，如果指定多个，将返回一个字典，键为工作表名，值为对应的DataFrame。
    header=0 : 用作列名的行号，默认为0，即第一行作为列名。如果没有标题行，可以设置为None。
    index_col=None : 用作行索引的列号或列名。默认为None，表示不使用任何列作为索引。可以是一个整数、字符串或列名的列表。
    usecols=None : 要读取的列。默认为None，表示读取所有列。可以是一个整数列表、字符串列表或Excel列的位置（如 [0, 1, 2] ）或字母标记（如 ['A','B', 'C'] ）。
    squeeze=False : 如果读取的数据只有一列，当设置为True时，返回一个Series而不是DataFrame。
    dtype=None : 指定某列的数据类型。默认为None，表示自动推断。可以是一个字典，键为列名，值为NumPy数据类型。
    skiprows=None : 要跳过的行号或行号列表。默认为None，表示不跳过任何行。可以是整数或整数列表。
    nrows=None : 读取的行数，从文件头开始。默认为None，表示读取所有行。
    na_values=None : 将指定的值替换为NaN。默认为None，表示不替换。可以是一个值或值的列表。
    keep_default_na=True : 如果为True（默认），则除了通过 na_values 指定的值外，还将默认的NaN值视为NaN
    parse_dates=False : 是否尝试将列解析为日期。默认为False。可以是一个布尔值、列名列表或列号的列表。
    date_parser=None : 用于解析日期的函数。默认为None，表示使用pandas默认的日期解析器。
    skipfooter=0 : 要跳过的文件底部的行数。默认为0，表示不跳过任何底部的行。
    convert_float=True : 是否将所有浮点数转换为64位浮点数。默认为True，以避免数据类型推断问题。
    **kwds : 允许用户传递其他关键字参数，这些参数可能会被引擎特定的读取器所识别。

"""
import pandas as pd

data = pd.read_excel('./人员信息.xlsx')
print(data)


"""
     https://pandas.pydata.org/pandas-docs/
"""
