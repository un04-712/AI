
"""
print('姓名','qzy')
print('年龄','18')
print('体重','55.55')
print('手机号','166xxxxxxxx')
print('家庭住址','xxxxx')
"""

'''
i = 1
j = 2
k = 3
print(i,j,k)
'''


'''
name = 'TOM'
age = 18
#1.直接输出
print('name',name)
print('age',age)
#2.格式化输出
print("name:%s,age:%d"%(name,age))
#3.format输出
print("name:{},age:{}".format(name,age))
#4.f-string输出123
print(f"name:{name},age:{age}")
'''

'''
username = input('请输入用户名：')
password = input('请输入密码：')
print('username:%s,password:%s'%(username,password))
print('username:{},password:{}'.format(username,password))
print(f('username:{username}','password:{password})')

num1 = input('请输入一个数字:')
num2 = input('请输入一个数字:')
result= int(num1)+int(num2)
print(result)
'''


'''
apple = 7
orange = 3
apple_weight = float(input('请输入购买苹果的斤数：'))
orange_weight = float(input('请输入购买橘子的斤数：'))
result = apple*apple_weight+orange*orange_weight
print(result)
'''