"""
        要通过函数接口来实现
        字符串查询：最核心的功能为字符是否在字符中

        find():检测字符串是否包含指定字符，如果是则放回索引值，否则放回-1
        index():检测字符串是否包含指定的字符串，如果是则放回索引值。否则报错
        rfind()从右到左检测字符串是否包含指定字符，如果是则放回索引值，否则放回-1
        rindex():从右到左检测字符串是否包含指定的字符串，如果是则放回索引值。否则报错
"""

from asyncio.windows_events import NULL

fruit_sentence = '苹果、香蕉、橙子'
while True:

    user_input = input("请输入你要查找的水果：")
    find_result = fruit_sentence.find(user_input)
    if  find_result != -1:
        print(f"find:{user_input}的起始位置是:{find_result}")
    else:
        print(f"未找到:{user_input}")

x = [3, 7, 5, 4, 3]
print(x.index(3))
