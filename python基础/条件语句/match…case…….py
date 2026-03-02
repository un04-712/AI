"""
match……case……基本格式
match 表达式：
    case a:
    print("事件1")
    case b:
    print("事件2”)
    case c:
    print("事件3")
    case _:
    print('事件4')
"""
#demo1
x = 20
match x :
    case 1:
        print('x的值为1')
    case 10:
        print('x的值为10')
    case _:
        print('x的值不在条件中')

#demo2
x = 20
match x:
    case 10 | 20 | 30:
        print('x的值为10、20、30中的一个')
    case 60:
        print('x的值为60')
    case _:
        print('x的值不在条件中')

#demo3
x = 10
y = 5
match x:
    case i if x<30:
        print('x的值:',i)
    case 50:
        print('x的值为：',50)
    case _:
        print('x不满足条件')


#中国合法工工作年龄为18~60岁，如果年龄小于18岁的情况视为童工，如果年龄在18~60岁之间为合法工龄；大于60岁为退休年龄。
x = 80
match x:
    case a if a<18:
        print('童工')
    case b if 18<=b<=60:
        print('合法工龄')
    case c if c>60:
        print('退休年龄')

