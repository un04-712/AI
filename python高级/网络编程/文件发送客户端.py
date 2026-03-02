import os
import pickle
import socket


if __name__ == '__main__':
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client.connect(('127.0.0.1', 2346))

    while True:
        file_path = input("请输入你要发送的文件路径(包含文件名)>>>")

        if os.path.isfile(file_path):
            # 获取文件名
            # print(os.path.split(file_path)[-1])
            # print(os.path.basename(file_path))
            file_name = os.path.basename(file_path)
            # 获取文件大小
            file_size = os.path.getsize(file_path)
            print(file_name,file_size)
            data = {
                'mode' : 'file',
                'file_name' : file_name,
                'file_size' : file_size,
            }
            # 将字典转为字节类型
            data_bytes = pickle.dumps(data)
            # 获取发送数据的大小 转为8个字节进行存储
            data_len = len(data_bytes).to_bytes(8, byteorder='big')
            # 发送数据
            tcp_client.send(data_len)
            tcp_client.send(data_bytes)
            # 发送文件内容  分块发送
            with open(file_path,'rb') as f:
                while True:
                    # 分块读取
                    temp =  f.read(4096)
                    if not temp:
                      break
                    # 分块发送
                    tcp_client.send(temp)
            print(f"{file_path}发送成功")

            """客户端接收服务端响应数据"""
            byte_len = tcp_client.recv(8)
            data_len = int.from_bytes(byte_len, byteorder='big')

            data_bytes = bytes()
            while data_len>0:
                if data_len < 4096:
                    temp =  tcp_client.recv(data_len)
                else :
                    temp = tcp_client.recv(4096)
                data_bytes += temp
                # 计算剩余长度
                data_len = data_len - len(temp)

            # 将字节转为字典
            data_dict =   pickle.loads(data_bytes)
            print(data_dict.get('msg'))