import socket

#创建socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#获取本地主机名字
host=socket.gethostname()
port=9999
#绑定端口
s.bind((host,port))

#设置最大连接数，超过后排队
s.listen(5)

while True:
	#建立客户端连接
	clientocket,address=s.accept()
	print('客户端连接地址为{}'.format(address))

	msg='WELCOME TO CONNECT'
	#向客户端发送消息
	clientocket.send(msg.encode('utf-8'))
	#接受客户端的消息
	print(clientocket.recv(1024).decode('utf-8'))
	clientocket.close()
