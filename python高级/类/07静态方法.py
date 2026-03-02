#静态方法：有自己的参数，与类里面的数据不共享，类和对象都可以调用，无法访问类属性
#静态方法的修饰符:@staticmethod


class mail:
    username = 123231321
    def __init__(self):
        self.a = 1
    @staticmethod
    def is_valid_email(email):
        print (mail.username)
# 检查邮箱地址是否包含@和.
        if '@' in email and '.' in email.split('@')[-1]:
            return True
        return False

mail1 = mail()
print(mail.is_valid_email("123123124@qq.com"))
print(mail1.is_valid_email("123123124@qq.com"))