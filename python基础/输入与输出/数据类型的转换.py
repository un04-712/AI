"""
float_num = 3.12
print(float_num)
complex_num = complex(float_num)
print(complex_num)


a = repr(1)
print(type(a))
a = eval('1+1')
print(type(a))
"""

#浮点形转换
num1 = 1
print(float(num1))
print(type(float(num1)))
#转换成元组
list1 = [10,20.30]
print(tuple(list1))
print(type(tuple(list1)))
#将序列转换成列表
t1 = (10,20,30)
print(list(t1))
print(type(list(t1)))
#将字符转换成ASCII整数值
a = 'A'
print(ord(a))
print(type(ord(a)))
#将一个整数转换成一个十六进制的字符串
num = 13
print(oct(num))
print(type(oct(num)))
#将一个整数转换成二进制字符串
num = 6
print(bin(num))
print(type(bin(num)))
#将一个整数转换成八进制的字符串
num =  56
print(oct(num))
print(type(oct(num)))


