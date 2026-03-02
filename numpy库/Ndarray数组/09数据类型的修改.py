"""
    numpy.ndarray.astype(dtype,order="K",)

"""

"""
    asting参数说明:
        'no': 表示根本不应该进行转换数据类型。
        'equiv':允许数值上等价的类型转换,即转换前后数据的位表示相同。这意味着转换不会导致数据丢失。
        'safe':允许安全的类型转换,即转换过程中不会丢失信息。
        'same_kind':允许相同数据类型类别内的转换。例如,允许整型和整型之间、浮点
        型和浮点型之间的转换,但是不允许整型和浮点型之间的转换。
        'unsafe':允许任何类型的转换,不考虑是否会导致数据丢失或改变。这是最不安全
        的选项,因为它可能会静默地丢弃数据。
    比如:
    从 int64 到 int32 的转换:
    'no':不允许。
    'equiv':不允许。
    safe':不允许。
    'same_kind':允许。
    'unsafe':允许。
    从 float64 到 int32 的转换:
    'no':不允许,因为会丢失小数部分。
    'equiv'、'safe'、'same_kind':不允许,因为这不是数值上等价或安全的转
    'unsafe':允许,但会丢失小数部分。

"""


import numpy as np

arr1 = np.full((2,3),fill_value=7)
print(arr1)
print(arr1.dtype)

newArr1 = arr1.astype(np.int64,casting='safe')
print(newArr1)
print(newArr1.dtype)

