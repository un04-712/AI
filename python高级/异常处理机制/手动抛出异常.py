"""
    raise 异常名 (提示词)


"""
"""
import time

for i in range(100):
    print(i)
    time.sleep(1)
    #raise nameError
    raise NameError('手动抛出异常')
"""
def check_age(age):
    if age<0:
        raise Exception('年龄不能为负数')
    elif age<18:
        raise Exception('年龄小于18岁，无法注册')
    else:
        print('注册成功')

try:
    age = int(input('请输入你的年龄：'))
    check_age(age)

except Exception as e:
    print(f'发生了异常{e}')

