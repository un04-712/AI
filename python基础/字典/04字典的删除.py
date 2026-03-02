"""
    pop()       删除指定的键名，并将其对应的值删除，返回删除键所对应的值
    clear()     清空字典
    popitem()   随机弹出一个键值对，在python3.7及以后变为弹出最后一个键值对
    del         删除字典 删除指定的键名，并将其对应的值删除
"""
boy1 = {'name':'Tom','age':'18','city':'New York'}
boy1.pop('city')
print(boy1)


boy1 = {'name':'Tom','age':'18','city':'New York'}
boy1.popitem()
print(boy1)


boy1 = {'name':'Tom','age':'18','city':'New York'}
boy1.clear()
print(boy1)

del boy1


d={'name':'lisi','age':10,'sex':'男'}
print(d.pop('sex'),d)


