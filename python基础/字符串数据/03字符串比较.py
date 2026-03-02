"""
    字符串比较:
        字符串比较是逐个字符的ASCII码开始比较，如果两个字符ASCII码值相同，则会继续比较下一个字符，直到所有字符串比较完毕

"""
from itertools import count

a = '1234'
b = 'abcd'
print(a<b)
print(ord('a'))
"""
    输入一个密码锁：
        请输入密码以解锁：123456
    判断逻辑：
        输入密码=正确密码  密码正确！解锁成功！欢迎进入秘密花园！
        输入密码>正确密码 提示：密码太复杂了，感觉要开挂了！，再试试简单点的！
        输入密码<正确密码 提示：密码不正确！想进来还得再努力些哦，尝试一下更复杂的密码吧！
"""

current_password = "secure123"

user_password = input("请输入密码：")
if user_password == current_password:
            print("密码正确！解锁成功！欢迎进入秘密花园")
elif user_password > current_password:
            print("：密码太复杂了，感觉要开挂了！，再试试简单点的！")
elif user_password < current_password:
            print("密码不正确！想进来还得再努力些哦，尝试一下更复杂的密码吧！")
