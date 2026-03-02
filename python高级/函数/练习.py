




def gender(user_select=None):
    if user_select == None:
        return '所选性别为男'
    else:
        return user_select
print(gender())
print(gender('女'))





def num(*args):
    for i in args:
        print(i)
print(num(1,5,6,['d',(1,4)]))





def num(**kwargs):
    for key,value in kwargs.items():
        print(f'key:{key},value:{value}')

num(key = 'name',vlaue = '电脑')






def num(*args,**kwargs):
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(f"key:{key},value；{value}")
num(1,3,a=3,b=4)
num(1,3,5,3,a=3)
num(a=1,b=2)
