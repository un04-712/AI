"""
        显示Series中的概要信息        包括数据类型 非空值的数量 内存使用情况
    Series.info(verbose=None, buf=None, max_cols=None, memory_usage=None, show_counts=None)

    verbose:控制输出信息的详细程度 一般给True
    buf:一个打开的文件对象或类似的文件对象。如果提供则输出将被写入这个缓冲区而不是标准输出
    max_cols:要显示最大的列数
    memory_usage:控制是否显示内存使用情况,一般为True
    show_counts:是否显示非空值的数量,一般为True
"""
import pandas as pd
import numpy as np
