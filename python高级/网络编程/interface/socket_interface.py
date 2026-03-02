import socket
import json
from 网络编程.interface import dtime

server_count = 0

def client_create(ip,port):
    """
    :param ip:  ip地址
    :param port:  端口
    :return: 客户端socket对象
    """
    # 创建socket对象 使用IPV4 TCP协议
    socket_client =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务端
    socket_client.connect((ip,port))
    return socket_client

def out_server():
    global server_count
    if server_count <= 0:
        server_count = 0
    else:
        server_count -= 1
    return server_count

# def send(client, data):
#     if not isinstance(client, socket.socket):
#         raise TypeError("client must be a socket object")
#     data_len_str = str(len(data)).encode('utf-8')
#     client.send(data_len_str)
#     client.send(data)

def send(conn,data):
    data_str = json.dumps(data)
    data_len_str = len(data_str.encode('utf-8')).to_bytes(8, byteorder='big')
    conn.send(data_len_str)
    conn.send(data_str.encode('utf-8'))

def recv(client):
    while True:
        byte_len = client.recv(8)
        if not byte_len:
            break
        # 将字节码转为int类型
        stream_len = int.from_bytes(byte_len, byteorder="big")
        """开始接收数据"""
        dic_bytes = bytes()
        while stream_len > 0:
            # 数据大小小于4096 直接接完所有数据
            if stream_len < 4096:
                temp = client.recv(stream_len)
            # 数据大于4096分块接收
            else:
                temp = client.recv(4096)
            if not temp:
                break
            dic_bytes += temp
            stream_len -= len(temp)
        """字节转字典"""
        # requests_dic = json.loads(dic_bytes.decode("utf8"))
        requests_dic = json.loads(dic_bytes)  # 将字节对象反序列化为字典对象
        print('服务器接收的数据',requests_dic)
        # print(requests_dic, type(requests_dic))
        return requests_dic

def  RequsetData1dic(mode,**kwargs):

    if mode == 'login' or mode == 'register':
        data1 = {
            "mode": mode,
            "user": kwargs.get('user'),
            "pwd": kwargs.get('pwd')
        }
        return data1

    return None

def  RequsetData2dic(mode,**kwargs):

    if mode == 'login' or mode == 'register':
        data2 = {
            "mode": mode,
            "user": kwargs.get('user'),
            "pwd": kwargs.get('pwd'),
            'time': dtime.getTime()
        }
        return data2
    elif mode == 'chat':
        data ={
            'mode':mode,
            'msg':kwargs.get('msg'),
            "user": kwargs.get('user'),
            'time': dtime.getTime()

        }

        return data

    return None

def ResponseData1dic(mode,**kwargs):
    if mode == 'login' or mode == 'register':
        data = {
            'mode': mode,
            'power': kwargs.get('power'),
            'time':dtime.getTime()
        }
        return data


def ResponseData2dic(mode,**kwargs):
    if mode == 'login' or mode == 'register':
        data = {
            "mode":mode,
            "user": kwargs.get('user'),
            "pwd": kwargs.get('pwd'),
            'power': '登录成功'
        }
        return data
    elif mode == 'chat':
        data ={
            'mode':mode,
            'msg':kwargs.get('msg'),
            "user": kwargs.get('user'),
            'time': dtime.getTime(),


        }

        return data
    return None