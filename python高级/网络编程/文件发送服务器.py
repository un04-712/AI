import os
import pickle
import socket
import threading

# 服务端文件保存路径
save_dir = r"C:\Users\86132\Desktop\python高级\网络编程\文件发送"
def client_handle(con_socket,ip_port):
    print('%s:%s 连接成功'%ip_port)
    while True:
        byte_len = con_socket.recv(8)
        # 将8个字节转换成int
        dataLen = int.from_bytes(byte_len,byteorder='big')
        print('服务端接收到数据长度为:',dataLen)

        # 创建空字节对象
        dic_byte =bytes()   # 5000
        while dataLen>0 :
            if dataLen < 4096:
                temp = con_socket.recv(dataLen)
            else:
                temp = con_socket.recv(4096)
            dic_byte += temp
            # 得到剩下的数据长度
            dataLen = dataLen - len(temp)

        # 将字节码转为字典
        request_dict =  pickle.loads(dic_byte)
        print("服务器接收到的数据内容:",request_dict)

        """------------------处理客户端的数据----------------"""
        if request_dict.get('mode') == 'file':
            file_name = request_dict.get('file_name')
            file_size = request_dict.get('file_size')
            with open(os.path.join(save_dir,file_name),'wb') as f:
                while file_size > 0 :
                    """分块接收文件数据"""
                    if file_size < 4096:
                        temp = con_socket.recv(file_size)
                    else :
                        temp = con_socket.recv(4096)  # 一次接收4k = 4 * 1024 = 4096Byte
                    """分块写文件数据"""
                    f.write(temp)
                    file_size = file_size - len(temp)
        """------------------给客户端发送响应数据----------------"""
        response = {
            'code': 200,
            'msg' : '文件写入成功'
        }
        #将字典转换为字节数据
        response_bytes =  pickle.dumps(response)
        #得到数据长度并通过8字节进行存储
        response_len = len(response_bytes).to_bytes(8,byteorder='big')
        # 发送8个字节的数据长度
        con_socket.send(response_len)
        # 发送数据内容
        con_socket.send(response_bytes)

if __name__ == '__main__':
    tcp_server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(('127.0.0.1', 2345))
    tcp_server.listen(5)
    while True:
        con_socket,ip_port = tcp_server.accept()
        handle_thread = threading.Thread(target=client_handle,args=(con_socket,ip_port))
        handle_thread.daemon = True
        handle_thread.start()
