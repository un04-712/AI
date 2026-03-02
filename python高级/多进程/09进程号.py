from multiprocessing import Process,current_process
import  time


def task():
    print(f'我是子进程{current_process().pid}')
    print(f'任务{current_process().pid}执行中')
    time.sleep(2)
if __name__ == '__main__':

    p = Process(target=task)
    p.start()
    task()
    print('主进程',current_process().pid)