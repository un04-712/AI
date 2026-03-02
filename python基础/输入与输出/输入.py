"""
    输入：使用input进行输入
    input：获取用户输入，会将用户输入表达式转变成字符串类型

"""
name = input('请输入你的名字：')
print('请输入你的名字：',name)
"""
    input函数
    在python3中，input()获取用户输入，输入内容作为python表达式执行，无论用户输入的是什么获取到的类型都是字符串型
    在python2中，raw_input()和input() raw_input()和python3中input()作用是一样的。
    input()输入的是什么数据类型，获取到的就是什么数据类型
    
    num = input("num:")
    print(type(num))
    
    如何在python3中实现类似python2中的input()行为？
    可以使用eval()来模拟python2中的行为，它会将输入的字符串作为python表达式

"""
