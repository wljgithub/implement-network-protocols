import socket

#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#服务器IP和端口号
address=('127.0.0.1',9998)

#向服务器发送消息
s.sendto('hello'.encode('utf-8'),address)

#接受服务器消息
print(s.recv(1024).decode('utf-8'))
s.close()