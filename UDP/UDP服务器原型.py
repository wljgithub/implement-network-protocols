import socket

#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#绑定服务器IP和端口号
s.bind(('127.0.0.1',9998))
print('Server is running...')
while True:
	#recvfrom返回客户端信息和地址(ip,port)
	bytes_,address=s.recvfrom(1024)
	#接受客户端消息
	print('Received from{}'.format(address))
	print('Message:%s'%bytes_.decode('utf-8'))
	#向客户端发送消息
	s.sendto('WELCOME'.encode('utf-8'),address)
	

