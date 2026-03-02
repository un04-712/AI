import socket
import time
import threading


online = {}
server_lock = threading.Lock()


def fun_server(sock,addr):
    username = sock.recv(1024).decode('utf-8')

    server_lock.acquire()
    online[sock] = (addr, username)
    online_len = len(sock)
    server_lock.release()

    print(f" {username}({addr}) 加入，当前在线：{online_len}")

    while True:
        data = sock.recv(1024)
        if not data:
            break
        mesg = data.decode("utf-8")
        if mesg.lower() == 'exit':
            break

def main():
    listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_sock.bind(('127.0.0.1',5000))
    listen_sock.listen()


    while True:
        sock, addr = listen_sock.accept()
        t = threading.Thread(target=fun_server, args=(sock, addr))
        t.daemon = True
        t.start()

if __name__ == '__main__':
    main()
