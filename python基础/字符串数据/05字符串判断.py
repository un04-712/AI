"""
    字符串判断：
            startswith()    判断以某字符串开头，是则返回True，否返回False
            endswith()      判断以某字符串结尾，是则返回True，否返回False
            isalnum()       判断是否都是字母或数字，是则返回True，否返回False
            isspace()       判断是否只包含空格，是则返回True，否返回False
            isdigit()       判断是否都是数字，是则返回True，否返回False
            isalpha()       判断是否都是字母，是则返回True，否返回False

"""
str1 = "zhangSan123"
print(str1.startswith('zh'))    #判断是否以'zh'开头
print(str1.endswith('123'))     #判断是否以'123'结尾
print(str1.isalnum())           #判断是否都是数字或字母
print(str1.isspace())           #判断是否只包含空格
print(str1.isdigit())           #判断是否只包含数字
print(str1.isalpha())           #判断是否只包含字母