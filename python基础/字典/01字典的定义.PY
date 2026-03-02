"""
    字典的定义： 字典名字 = {键1:值1,健2:值2,……键n:值n,键n+1:值n+1}
    注意： 1、在字典中，键是唯一的，且键和值是一一对应的
    如果定义了相同的键，那么新定义的值就会被覆盖掉
         2、键必须不可变，一般为数字、字符串、元组，但不能用列表
    值可以为任何数据类型
"""
# 字典的创建
#方式1
boy = {'name':'Tom','age':'18','city':'New York'}
print(boy)


#方式2 fromkeys，一次性创建多个字典，所有的键和字典都使用指定的值，值默认是None

people = dict.fromkeys(['name','age','height','weight'],'bob')
print(people)

ls =list({'shandong':200, 'hebei':300, 'beijing':400})
print(ls)

