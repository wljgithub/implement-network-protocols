import socket

#创建一个socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#服务器IP和端口号
host=socket.gethostname()
port=9999

#连接服务器
s.connect((host,port))

#接受服务器信息
print(s.recv(1024).decode('utf-8'))
#发送信息
s.send('hello,server\nlalal'.encode('utf-8'))
s.close()