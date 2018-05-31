import threading
import socket

def tcplink(sock,addr):
    print('Accept new connection from {}'.format(addr))
    sock.send(b'Welcome!')
    while True:
        data=sock.recv(1024)
        if data.decode('utf-8')=='exit':
            print('Connection from {} closed'.format(addr))
            s.close()
            break
        #把客户端的消息，加上一个hello后返回    
        sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))

if __name__ == '__main__':
    #创建socket对象
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定IP地址和端口
    s.bind(('127.0.0.1',8848))
    #监听
    s.listen(5)
    print('the server is ready!')
    while True:
        sock,addr = s.accept()
        t=threading.Thread(target=tcplink,args=(sock,addr))
        t.start()

