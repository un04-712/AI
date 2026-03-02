import threading
import socket


def rece(client):
    while True:
        data = client.recv(1024)
        if not data:
            print("已于服务器断开连接/n")
            break
    client.close()


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))

    data = client.recv(1024).decode('utf-8')
    name = input(data)
    client.sendall(name.encode('utf-8'))


    t = threading.Thread(target=rece,args=(client,))
    t.daemon = True
    t.start()

    print('已进入聊天室')
    while True:
        mesg = input(">>>")
        if not mesg:
            continue
        client.sendall(mesg.encode('utf-8'))
        if mesg.lower()  == 'exit':
            break
    client.close()


if __name__ =="__main__":
    main()