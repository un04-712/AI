"""
    partition(obj) 以obj字符串进行分割三部分   前部分 obj字符串 后部分

    rpartition(obj) 从右到左以obj字符串进行分割 前部分 obj字符串 后部分

    split(obj,n)    以从左到右以obj字符串进行分割n次

    splitlines()    以从左到右以\n字符串进行分割n次

"""
#示例
text = "超级英雄：红钢铁侠，蜘蛛侠，白钢铁侠，蝙蝠侠\n欢迎来到我们的超级英雄大会！"
print(text.partition('钢铁侠'))
print(text.rpartition('钢铁侠'))

fruit = '苹果_香蕉_橘子_西瓜'
time = '18:54:59'

print(fruit.split('_',3))
STime = time.split(':',3)
print(STime[0],STime[1],STime[2])
print(text.splitlines())
print('*'*100)
text = '10101\n2006\n12\n26\n0019'
Ttext = text.splitlines()
print(f"我的出生日期{Ttext[1]}年{Ttext[2]}月{Ttext[3]}日")
