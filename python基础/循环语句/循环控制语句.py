"""
    break
    continue
    pass    为空语句，作用为代码块进行占位，防止语法报错
"""
#break
i = 1
while 1<=5:
    if i==3:
        i+=1
        break
    print(i)
    i+=1

#continue
i = 1
while 1<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1

#pass
i = 1
while 1 <= 5:
    if i == 3:
        i += 1
        pass
    print(i)
    i+=1
