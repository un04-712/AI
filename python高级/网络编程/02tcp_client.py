import socket
import time
from threading import Thread
import queue

msgQueue = queue.Queue()

def RecvTask():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            data = data.decode('gbk')
            print('服务端发过来的数据:', data)
            time.sleep(0.01)
        except Exception as e:
            print(f"接收数据时发生错误: {e}")
            break


# 1、创建socket对象  SOCK_STREAM 流式传输  SOCK_DGRAM (报文传输)  UDP
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# 2、建连接
client.connect(('127.0.0.1',5000))


t = Thread(target=RecvTask)
t.start()

#3、 传输数据

try:
    while True:
        data = input('请输入>>>').strip()
        if data == 'exit':
            break
        client.send(data.encode('utf-8'))
except KeyboardInterrupt:
    print("\n连接关闭")
finally:
        client.close()


        data_size = int(client.recv(8).decode('gbk'))
        print(data_size)
        recv_size = 0
        data = b''
        while recv_size < data_size:
            res = client.recv(1024)
            recv_size += len(res)
            data += res

        print('服务端发过来的数据', data.decode('gbk'))
        # print(len(data))
        # msgQueue.put(data)

        # while msgQueue.empty():
        #     data = msgQueue.get()
        #     print('服务端发过来的数据', data)



# 4、结束服务
client.close() # 关闭当前连接






