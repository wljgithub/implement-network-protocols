import socket

#构造socket，连接新浪
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

'''
一定要符合HTTP标准，每一行记得带上换行符\n，不然服务器不返回请求
请求行: 方法 uri http版本
请求头: Host:... Connection:...
请求体:...
'''
# http_headers=b'GET / HTTP/1.1 \nHost:www.sina.com.cn\nConnection:close\n\n'
http=b'GET / HTTP/1.1 \n Host: www.sina.com.cn \n Connection: keep-alive'

s.send(http)
buffer=[]
while True:
	msg=s.recv(4096)
	#如果接送到信息则放入列表中
	if msg:
		buffer.append(msg)
	#否则关闭socket,退出循环	
	else:
		s.close()
		break
#注意因为这里返回的是字节流，所以字符串前必须得加上b
msg=b''.join(buffer)
print(msg.decode('utf-8',errors='ignore'))



	
