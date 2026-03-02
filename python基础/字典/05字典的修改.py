"""
    直接修改
    update修改        合并两个字典，重复的键会覆盖

"""

boy = {'name': 'joy', 'age': '18', 'city': 'New York'}
boy['city'] = 'China'
print(boy)


boy = {'name':'Tom','age':'18','city':'New York'}
boy1 = {'name':'zmh','age':'20','city':'China'}
boy.update(boy1)
print(boy)

x = {1:2}
x[2] = 3
print(x)
