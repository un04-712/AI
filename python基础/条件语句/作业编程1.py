
"""
num = int(input('请输入一个整数：'))
if num%6==0 and num%7==0:
    print('该数能被6和7整除')
"""




'''
num1 = int(input('请输入整数 a:'))
num2 = int(input('请输入整数 b；'))
if num1<num2:
    print("a<b")
'''
'''
x = int(input('请输入一个整数:'))
if x%2==0:
    print(x**3)
else:
    print(x**2)
'''
'''
s = int(input('请输入你的分数：'))
if s>100 or s<0:
    print('输入错误')
elif 90<s>=100:
    print('优秀')
elif 70<s>=90:
    print('良好')
elif 60<s>=70:
    print('及格')
elif s<60:
    print('补考')
'''
'''
x = int(input('请输入一个整数:'))
y = int(input('请输入一个整数:'))

if 3*x+y-4==0:
    print('True')
else:
    print('False')
'''
'''
x = int(input("整数："))12

if x>=0:
    y=2*x+1
elif x<0:
    y=2*x-1
print(y)
'''
'''
num = (input('请输入身份证号码：'))
if len(num) == 18:
    print("正确格式")
else:
    print('格式错误，请重新输入！')
    exit()
if int(num[16])%2==0:
    print("女性")
else:
    print('男性')
'''

'''
num = (input('请输入QQ号码：'))
if len(num)>6 and num.isdigit():
    print("QQ号形式合法")
'''
'''
x = int(input("整数："))
if x<0:
    y=2*(x**2)
elif x>0:
    y=abs(x)/(x+1)
elif x ==0:
    y=5
print(y)
'''

a=5;b=4;c=3;d=2
if a>b>c:
    print(d)
elif c-1>=d==1:
    print(d+1)
else:
    print(d+2)













