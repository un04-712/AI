"""
    in 和 not in 用来判断某键是否在列表中
    get 第一个参数为要查找的键，第二个参数为键不存在是指定返回的提示语，如果存在返回键对应的值
    setdefault r如果存在则返回对应的值，不存在则会创建一个新的键值对，第一个参数为键，第二个参数为值
"""

boy = {'name':'Tom','age':'18','city':'New York'}
dict1 = {1:2,2:3,3:4}
print(sum(dict1))
# if 'Tom' in boy:
#     print('age键存在')
# else:
#     print('Tom键不存在')
#
# a = boy.get('height', 'not height')
# if a == 'not height':
#     boy.setdefault('height','1.82')
#     print(boy)

