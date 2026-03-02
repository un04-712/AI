"""
    序列(Sequence)是一个抽象概念
    它指的是可以按照索引位置访问元素的有序数据结构
    标准序列类型包括列表(list),元组(tuple),字符串(str),
    其中列表被称为可变序列，元组和字符串叫做不可变序列。

    count() 统计子字符串出现的次数
    join()  将序列中的元素连接成一个新的字符串
    replace() 替换指定的字符串，并且可以知道替换次数
    capitalize() 将字符串首字母大写
    len()   返回字符串的长度值

"""
#1、统计子字符串出现的次数
str1 = 'hello world'
print(str1.count('ll'))
print(str1.count('o'))

#2、将序列中的元素连接成一个新的字符串
str1 = '_'
list1 = ['hello','world','hello,world']
print(str1.join(list1))

#3、换指定的字符串，并且可以知道替换次数
str1 = 'hello world hello world'
print(str1.replace('hello','Hello'))
print(str1.replace('hello','Hello',1))

#4、将字符串首字母大写

str1 = 'hello world'
print(str1.capitalize())    #单个首字母大写
print(str1.title())         #每个单词首字母大写

#5、 len()函数 返回字符串的长度值  计算的是字符不是字节
str1 = '你好python'
print(len(str1))

print("Never give up".split())


