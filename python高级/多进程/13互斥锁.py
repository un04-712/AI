'''
    互斥锁:
问题:当多个进程操作同一份数据时候,会出现数据错乱
解决方法:加锁处理,把并发变成串行,牺牲掉运行效率,但保证了数据安全

注意:不要轻易加锁,加锁只应该在争抢数据的环节

'''

import json
import time
from multiprocessing import Process, Lock
import random
    # 查票
def serch_ticket(name):
    # 读取文件,查询车票数量
    with open('./data/tickets','r',encoding='utf-8') as f:
        dic = json. load(f)
        print(f"用户{name}查询余票:{dic['tickets_num']}")

# 买票
def buy_ticket(name):
    with open('./data/tickets', 'r', encoding='utf-8') as f:
        dic = json. load(f)
    if dic['tickets_num']>0:
        dic['tickets_num'] -= 1
        with open('./data/tickets', 'w', encoding='utf-8') as f:
            json.dump(dic,f)
        print(f'用户{name}买票成功')
    else :
        print(f'余票不足,用户{name}买票失败')

def task(name, mutex):
    serch_ticket(name)
    time.sleep(random.randint(1,3))
    mutex.acquire() #请求锁
    buy_ticket(name)
    mutex.release()#释放锁

if __name__ == '__main__':
    l=[]
    mutex = Lock()

for i in range(1,10):
    t = Process(target=task, args=(i,mutex))
    t.start()
    l.append(t)
