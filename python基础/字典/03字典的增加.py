"""
    直接增加
    update增加        合并两个字典，重复的键会覆盖

"""
#直接增加
#格式 字典名字[新的键名] = value
# boy = {'name':'Tom','age':'18','city':'New York'}
# boy['height'] = 1.82
# print(boy)


#update增加
boy1 = {'name':'Tom','age':'18','city':'New York'}
boy2 = {'1':'Tom','age':'19','3':'New York'}
boy1.update(boy2)
print(boy1)
print(boy2)



