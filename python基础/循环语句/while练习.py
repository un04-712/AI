import random
win = 0.3
print("欢迎来到赌博机!")
while win:
    a = input("输入'play'开始游戏, 或输入'quit'退出: ")
    if a == 'play':
        if random.random() < win:
            print("恭喜你! 你中奖了!")
        else:
            print("很遗憾，你没有中奖。")
    elif a == 'quit':
        print("谢谢你的游戏! 再见!")
        break
    else:
        print("无效的输入，请输入'play'开始游戏或'quit'退出。")