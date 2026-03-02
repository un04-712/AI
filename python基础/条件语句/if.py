'''
    if基本格式
        if 要判断的条件；
            条件成立时要做的事
    age = int(input('请输入你的年龄：'))
        if age>=18:
            print('你可以去网吧了')
'''
import random

'''
if……else语句基本格式
    if 条件：
    满足条件做的事1
    满足条件做的事2
    else：
    不满足条件做的事
    不满足条件做的事
    ticket = 1
if ticket:
    print('不允许进入')
else:
    print('请先买票')
    height = int(input('请输入你的升高(cm):'))
if height >=150:
    print('请进')
else:
    print('禁止进入')
'''

'''
if……elif……else基本格式
    if 条件1:
    事件1
    elif 条件2：
    事件2
    elif 条件3：
    事件3
说明：
条件1满足时，执行事件1，然后整个if结束
条件1不满足时，判断条件2，如果条件2满足，则执行事件2，整个if结束
条件1不满足，条件2也不满足时，如果条件3满足，则执行条件3，然后整个if结束
可以和else一起使用

'''

'''
score = 50
if 90<= score <=100:
    print('等级A')
elif 80<= score <90:
    print('等级B')
elif 60<= score <80:
    print('等级C')
elif score >100 or score< 0:
    print('输入错误，请重新输入')
else:
    print('等级D')
'''
'''
    if嵌套的格式
    if 条件1：
        满足条件1做的事1
        满足条件1做的事2
        if 条件2：
        满足条件2做的事1
        满足条件2做的事2
        else:
        不满足条件2做的事1
    else:
    不满足条件1做的事 
说明：
外层的if判断也可以是if-else
内层的if判断也可以是if-else
'''
'''
knifeLength = 9
ticket = 1
if knifeLength<10:
    print('通过安检')
    if ticket == 1:
        print('可以乘坐')
    else:
        print('请先购票')
else:
    print('不能进入')
'''
'''
if 实现三目运算符
条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
'''
'''
a = 1
b = 2
print(a if a>3 else b)
'''
random.randint(1,100)
print(random.randint(1,100))






