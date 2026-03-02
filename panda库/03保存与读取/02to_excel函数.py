"""
    在操作excel表格之前，需要安装一个库： openpyxl ，因为pandas 库本身并不包含写入Excel文件的直接支持，如果没有安装的话将无法操作excel。
其安装命令为：pip install openpyxl
    Pandas中的 to_excel 用于将DataFrame保存为Excel文件。
    DataFrame.to_excel(excel_writer, sheet_name='Sheet1', na_rep='',float_format=None, columns=None,
    header=True, index=True,index_label=None, startrow=0, startcol=0,
     engine=None,merge_cells=True, inf_rep='inf', freeze_panes=None,storage_options=None)
    excel_writer ：字符串或ExcelWriter对象，指定输出文件的路径或文件对象。
    sheet_name='Sheet1' ：要写入的工作表名称。
    na_rep='' ：指定缺失值的表示方式。
    float_format=None ：浮点数的格式化方式，例如’%.2f’
    columns=None ：要写入的列的子集，默认为None，表示写入所有列。
    header=True ：是否写入列名，默认为True。
    index=True ：是否写入行索引，默认为True。
    index_label=None ：指定行索引列的列名，如果为None，并且 header 为True，则使用索引名。
    startrow=0 ：写入DataFrame的起始行位置，默认为0。
    startcol=0 ：写入DataFrame的起始列位置，默认为0。
    engine=None ：指定用于写入文件的引擎，可以是’openpyxl’（默认）或’xlsxwriter’。
    merge_cells=True ：是否合并单元格，这在有合并单元格的Header时很有用。
    inf_rep='inf' ：指定无限大的表示方式。
    freeze_panes=None ：指定冻结窗口的单元格范围，例如’A2’。
    storage_options=None ：指定存储连接的参数，例如认证凭据。

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
df.to_excel('人员信息.xlsx', index=False)