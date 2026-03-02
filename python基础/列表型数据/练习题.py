#[[0, 0, 0, 0, 0, ], [0, 1, 2, 3, 4, ], [0, 2, 4, 6, 8, ], [0, 3, 6, 9, 12, ]]
# 方法一
list1 = [[0, 0, 0, 0, 0, ], [0, 1, 2, 3, 4, ], [0, 2, 4, 6, 8, ], [0, 3, 6, 9, 12, ]]
# 方法二
ls1 = []
for i in range(4):
    temp1 = []

    for j in range(5):
        temp1.append(i*j)
    ls1.append(temp1)
print(ls1)
# 推导式
ls1 = [ [ i*j for i in range(5)] for j in range(4)]
print(ls1)

#把列表[0,1,2,3,4,5,6,7,8,9]中的每个元素都加100,生成一个新列表
ls1 = [0,1,2,3,4,5,6,7,8,9]
ls = []
for i in ls1:
    i += 100
    ls.append(i)
print(ls)


#列表推导式
ls  = [ i + 100 for i in ls1]
print(ls)


# EAl:list1 = ["A", "B", "C"], list2 = ["X", "Y", "Z"]
# 使用列表推导式生成['AX','AY','AZ','BX','BY','BZ','CX','CY','CZ']
list1 = ["A", "B", "C"]
list2 = ["X", "Y", "Z"]

ls3 = []
for i in list1:
 for j in list2:
     ls3.append(i+j)
print(ls3)


ls1 = [ i+j for i in list1 for j in list2]
print(ls1)


