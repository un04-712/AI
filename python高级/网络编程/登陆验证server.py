import threading

import json
from interface import socket_interface
import socket
import time

from interface import dtime
online_count = 0          # 当前在线人数
count_lock   = threading.Lock()

sockets_list = []

# def client_handle(conn,addr):
#     try:
#         while True:
#             data_dict = socket_interface.recv(conn)
#             # print(f"服务端接收到{ip_port}数据:",data_dict)
#             if data_dict.get("mode")=='login':
#                 login_request(conn,data_dict)
#                 if data_dict.get("mode")=='chat':
#                     chat_request(conn,data_dict)
#     except Exception as e:
#         # print(e)
#         conn.close()


# def send(conn,data_dic):
#     data_str = json.dumps(data_dic)
#     data_len_str = len(data_str.encode('utf-8')).to_bytes(8, byteorder='big')
#     conn.send(data_len_str)
#     conn.send(data_str.encode('utf-8'))


def login_request(conn,requests_dic):
    db_user = requests_dic['user']
    db_pwd = requests_dic['pwd']
    with open('./db/text', 'r') as fg:
        user_count = fg.readlines()
        # print('第一次打印',user_count)
        for i in user_count:
            if i.split(':')[0].strip() == requests_dic.get('user') and i.split(':')[1].strip() == requests_dic.get(
                    'pwd'):
                status = "登录成功"

                break
            else:
                status = '登录失败'

    response_dict = socket_interface.ResponseData2dic(mode='login', user=db_user, power=status,pwd=db_pwd)

    socket_interface.send(conn, response_dict)

def chat_request(conn, data_dict):
    global online_count
    username = data_dict.get("user")
    msg = data_dict.get("msg")
    time = data_dict.get("time")

    if msg.lower() == 'exit':
        print(f"{username} 请求退出聊天室")
        for socket_dict in sockets_list:
            if socket_dict["socket_handle"] == conn:
                print(f"{username} - - {time}")
                sockets_list.remove(socket_dict)  # 移除离线用户
                conn.close()
                with count_lock:
                    online_count -= 1
                print(f"{username} 已退出聊天室，当前在线人数：{online_count}")
                break
    else:
        response_dict = socket_interface.ResponseData2dic('chat', user=username, msg=msg, time=time)
        print(response_dict)
        for socket_dict in sockets_list:
            socket_interface.send(socket_dict["socket_handle"], response_dict)  # 传递 socket 对象


def server_resv_data(conn,addr):
    global online_count
    with count_lock:
        online_count += 1

    # 获取年月日时分秒
    ntime = time.time()
    lotime = time.localtime(ntime)  # 转换为时间结构体
    # 转换为字符串
    str_time = time.strftime("%Y-%m-%d %H:%M:%S", lotime)

    print(f" 用户{addr} 上线---当前时间{str_time}---当前在线：{online_count}")

    while True:
        data_byte_len = conn.recv(8)
        if not data_byte_len:
            with count_lock:
                online_count -= 1

                # 获取年月日时分秒
            ntime = time.time()
            lotime = time.localtime(ntime)  # 转换为时间结构体
            # 转换为字符串
            str_time = time.strftime("%Y-%m-%d %H:%M:%S", lotime)
            print(f"{addr} 下线---当前时间{str_time}---当前在线：{online_count}")
            break
        stream_len = int.from_bytes(data_byte_len, byteorder="big")
        dic_bytes = bytes()
        while stream_len > 0:
            # 数据大小小于4096 直接接完所有数据
            if stream_len < 4096:
                temp = conn.recv(stream_len)
            # 数据大于4096分块接收
            else:
                temp = conn.recv(4096)
            if not temp:
                break
            dic_bytes += temp
            stream_len -= len(temp)
        """字节转字典"""

        requests_dic = json.loads(dic_bytes.decode("utf-8"))
        user = requests_dic.get('user')
        print(f"接受到{user}的数据:",requests_dic)

        db_user = requests_dic['user']
        dtime = requests_dic['time']

        if requests_dic['mode'] == 'register':
            if db_user is None:
                with open('./db/text','a+') as fr:
                    fr.write(f"{requests_dic['user']}:{requests_dic['pwd']}\n")
                    print(f"{requests_dic['user']}注册成功")
                    status = "注册成功"
            else:
                print(f"{requests_dic['user']}账户已存在")

                status = "注册失败"
                response_dict = socket_interface.ResponseData1dic(mode='register',power=status,time=dtime)
                # response_dict = {
                #     'mode':'register',
                #     'power':status
                # }
                socket_interface.send(conn, response_dict)

        if requests_dic['mode'] == 'login':
            login_request(conn,requests_dic)
        if requests_dic['mode'] == 'chat':
            chat_request(conn, requests_dic)




server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1',8080))

server.listen(5)

print('服务端启动成功，在8080端口等待客户端连接')

while True:
    conn,addr = server.accept()
    sockets_list.append({"socket_handle": conn, "addr": addr})
    print(sockets_list)
    threading.Thread(target=server_resv_data, args=(conn, addr)).start()
    print('连接对象',conn)
    print('客户端的ip和端口',addr)
