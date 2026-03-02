#导入re模块
import re

"""
    查找字符串中所有匹配正则表达式内容
    re.findall(pattern,string,flags)
    pattern:正则表达式
    string:匹配的字符串
    flags:标志位
            re.DOTALL 让点可以匹配到所有内容
            re.I      忽略大小写
            re.M      多行模式
    return:返回匹配到的结果列表   如果没有匹配到则列表为空
"""
# s1 = 'abc\ndef\nghi'

#匹配abc def ghi
# print(re.findall(r'[a-z]+', s1))
#
# #匹配所有内容
# print(re.findall(r'.+', s1,re.DOTALL))


"""
    re.search():    只会匹配符合规则的第一个值，不要求开头必须匹配，只要字符串中符合条件即可 返回Match对象
"""
s1 = """    
tel:028-6323432
tel:029-1245324
tel:030-5123134
"""

res = re.search(r"tel:[0-9]{3}-[0-9]{7}",s1)
print(res)

"""
    re.finditer():返回一个可迭代的匹配对象.
     
    ()  group组概念  
    (?:)  正则表达式()
"""

res = re.finditer(r"tel:[0-9]{3}-[0-9]{7}",s1)

for i in res:
    print(res)

s = """
Host: movie.douban.com
Pragma: no-cache
Referer: https://cn.bing.com/"""

#通过正则表达式将字符串转为字典
s_dict = {}
res =  re.finditer(r"([a-zA-Z]+): (.*)", s)
print(res)
for i in res:
    s_dict[i.group(1)] = i.group(2)
print(s_dict)

"""
    re.match():   尝试使用正则表达式从字符串的起始位置开始匹配，只有开头就符合才会返回匹配结果，否则返回none
    应用场景:验证是否符合特定的开头格式
    
    re.fullmatch():严格要求整个字符串都要匹配
"""

text = "hello 123 hello world"

res = re.match("world",text)
print(res)

"""
    re.sub():将我们的匹配内容替换为其他内容
    re.subn():将我们的匹配内容替换为其他内容 同时返回替换次数
    
    repl: 要替换的字符/函数
"""

s1 = """    
tel:028-6323432
tel:029-1245324
tel:030-5123134
"""
#将后五位替换为xxxxx

print(re.sub(r'[0-9]{7}', 'xxxxx', s1))


def des(m): # m为获取到匹配的字符串 match对象，每匹配到一次就会进一次函数
    return m.group(1)+'-'+m.group(2)[:2]+"xxxxx"

print(re.sub(r'tel:([0-9]{3})-([0-9]{7})', des, s1))



"""
    re.split():将正则表达式 匹配到的内容变成分隔符进行拆分字符串
"""

s = "xyg ,*&* time *^* dog cat"
print(re.split(r'\W+', s))


"""
    re.compile:预编译正则表达式，将正则表达式内容转化为正则表达式对象
"""
re_obj = re.compile(r'\W+')

print(re_obj.split(s))
print(re_obj.findall(s))

"""
    账号 ： 只允许数字长度至少为8-12位
    密码： 至少包含大小写字母，数字，长度至少为8-16位
"""

username = "42132142131"
password = "3a2BB"

res_user = re.findall(r"^[0-9]{8,12}$", username)
res_pass = re.findall(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).{8,16}$", password)
print(res_user)
print(res_pass)
if res_user != [] and res_pass != []:
    print("账号正确")
else :
    print("格式出错")