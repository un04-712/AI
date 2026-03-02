
from threading import Thread, Event
import time
import random

event = Event()

def bus():
    print('公交车即将到站')
    time.sleep(3)
    print('公交车到站了')
    # 告诉等车的人可以上车了
    event.set()#发射信号,车来了赶紧上车

def passenger (name):
    print(name,'正在等车')
    event.wait()
    print(name,'上车出发')

if  __name__== '__main__':
    t = Thread(target=bus)
    t.start()
    for i in range(10):
        t = Thread(target=passenger, args=(f'{i}',))
        t.start()






