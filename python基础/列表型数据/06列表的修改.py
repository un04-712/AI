"""
        使用下标或切片的方式对列表中的单个元素或多个元素进行修改
"""
import numpy as np
#下标修改
list1 = [1,2,3,4,5,5,6]
list1[3] = [2]
print(list1)

#切片访问   可以是实现多数量修改
#注意，复制的数量必须和要修改的数量一致
list1 = [1,2,3,4,5,5,6]
#1、列表方式赋值
list1[1:4] = [3,'sd','sf']
print(list1)
#2、等号方式赋值
list1[1:4] =7,'fdFfs','daFw'
print(list1)

x='python'
x=x.split('t')
print(x)


arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
