import socket
import subprocess
# 1、创建socket对象  SOCK_STREAM 流式传输  SOCK_DGRAM (报文传输)  UDP
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# 2、绑定地址和端口  127.0.0.1 为自己本机地址 0.0.0.0 代表本机所有地址
# 端口：1024之前为系统保留 0-65535
server.bind(('127.0.0.1',5000))

# 3、监听连接请求  允许5个客户端接入
server.listen(5)

print('服务端启动成功，在5000端口等待客户端连接')

while True:
    # 4、取出连接请求，开始服务 conn为连接对象 addr为客户端ip和端口
    conn,addr =  server.accept()

    print('连接对象',conn)
    print('客户端的ip和端口',addr)

    # 5、数据传输

    while True :
        data = conn.recv(1024)
        data = data.decode('utf-8')
        print('客户端发过来的数据',data)


        if not data:  # 没有数据客户端断开连接
            break
        obj = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        out_res = obj.stdout.read()
        data_size = len(out_res)
        print(data_size)
        # 先发长度
        header = str(data_size).encode('gbk').zfill(8)
        conn.send(header)
        conn.send(out_res)
        # conn.send(out_res)

    # 6、结束服务
    conn.close() # 关闭当前连接
# sk.close() # 一般不会做  这样相当于把服务器关掉