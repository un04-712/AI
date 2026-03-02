from threading import Thread,Lock
import time

num = 100

def task(mutex):
    global num
    mutex.acquire()
    temp = num
    time.sleep(0.05)
    num = temp - 1
    mutex.release()

if __name__ == '__main__':
    l = []
    mutex = Lock()
    for i in range(100):
        t = Thread(target=task,args=(mutex,))
        t.start()
        l.append(t)

    for i in l:
        i.join()

    print(num)
    print('主线程')