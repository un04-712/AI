"""
    使用return结束函数，会返回值给调用方
    不带表达式的return相当于返回none


"""
#减法
def fun(x,y):
    return x-y

def fun1(a,b):
    if b==0:
        return '除数不能为0'
    return a/b
print(fun1(3,0))

# 返回多个值
def cal(x,y):
    z1 = x+y
    z2 = x-y
    z3 = x*y
    z4 = x/y
    return z1,z2,z3,z4
z1,z2,z3,z4 = cal(2,6)
z = cal(2,6)
print(z1,z2,z3,z4)
print(z)




