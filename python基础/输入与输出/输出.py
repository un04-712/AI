
#在python中，print最终调用的是sys.stdout.write()函数
#stdout 标准输出流（终端或控制台）
import sys
sys.stdout.write('Hello,World') #不会换行

#与print()相比：
print("Hello,World!")#  会自动换行

#1、直接输出
print('Hello,World!')
print(200)
a = 1
print(a)
print('a',a)
print('*'*50)
#2、格式化输出
name = 'zhangsan'
age = 18
print("name:%s,age:%d"%(name,age))
print('*'*50)
#3、format输出
height = 182.54
weight = 150.685
print("height:{},weight:{:03.2f}".format(height,weight))
print('*'*50)
"""
格式化数字 {:.2f} {:,} {:.0%}
对齐与填充
"""
#4、f-string输出,输出指定的位宽

name = 'll'
weight = 90.565476
print(f"My nane is {name} and my weight is {weight:03.3f}")
print('*'*50)

#5、print()参数
#seq:在值与值之间插入字符串，默认为空格
help(print)
name = 'wjx'
age = 10
print('name:',name,'age:',age,sep='-')
#end:最后一个值之后附加字符串，默认为换行
print('name:',name,'age:',age,end='')


