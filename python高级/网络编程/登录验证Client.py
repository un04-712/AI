from multiprocessing import Process

import json

import socket
from interface import socket_interface
from interface import user_interface
from threading import Thread




def home():
    print(f"{'登录管理界面':*^20}")
    print(f"{'01 注册':^20}")
    print(f"{'02 登录':^20}")

def register(client):
    name = input("请输入你要注册的账号:")
    word = input("请输入你要注册的密码:")
    data_dic1 = socket_interface.RequsetData1dic('register',user=name,pwd=word)
    print('res2:',data_dic1)
    socket_interface.send(client,data_dic1)
    socket_interface.recv(client)

def login(client):
    count = input("请输入你要登录的账号:")
    password = input("请输入你要登录的密码:")
    data_dic2 = socket_interface.RequsetData2dic('login', user=count, pwd=password)
    # print('res1:',data_dic2)
    socket_interface.send(client, data_dic2)
    recv_dic = socket_interface.recv(client)
    # print(recv_dic)
    recv_dic.get('power')
    # print('第一次打印',recv_dic.get('power'))
    # print('res:',recv_dic)
    return True  if  recv_dic.get('power') == '登录成功' else False,count

def chat_recv_msg(client,user):
    while True:
        data_dic = socket_interface.recv(client)

        time = data_dic.get('time')
        print(time)
        print(f"{data_dic.get('user')}:{data_dic.get('msg')}")
        print(f"{user}>>>", end="")

def chat(client,user):
    print('欢迎来到聊天室'.center(30,'*'))
    chat_Process = Process(target=chat_recv_msg,args=(client,user))
    chat_Process.daemon = True
    chat_Process.start()
    while True:
        msg = input(f"{user}>>>")

        if msg == "exit":
            socket_interface.out_server()
            chat_Process.terminate()
            break

        data_dic = socket_interface.ResponseData2dic('chat', user=user, msg=msg)
        socket_interface.send(client, data_dic)




if __name__ == '__main__':
    client = socket_interface.client_create('127.0.0.1',8080)
    home()
    user_input = input("请选择你的功能:")
    while True:
        try:
            if user_input == '1':
                register(client)

            elif user_input == "2":
                # login(client)
                ret,user = login(client)
                if ret:
                    chat(client,user)
        except ConnectionRefusedError:
            print("服务器未启动")
        except Exception as e:
            print(e)
            # traceback.print_exc()















