import random
from itertools import count
guessCount = 1
print("游戏开始")
readNum = random.randint(1,100)

for i in count():
    if guessCount>10:
        print(f"游戏结束，正确数字为{readNum}")
        break
    print(f"这是第{guessCount}次尝试，请输入你猜测的数字：")
    a = int(input())
    if 1 <= a <=100:
        guessCount +=1
    if a < readNum:
            print('猜的数字小了')
    elif  a > readNum:
            print('猜的数字大了')
    elif  a == readNum:
            print('恭喜你猜对了，游戏结束。')
            break
else:
        print('非法输入，请重新输入:')


