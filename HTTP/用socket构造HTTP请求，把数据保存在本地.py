import socket
'''用socket构造HTTP请求，把服务器返回的数据保存到本地,'''

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

'''
一定要符合HTTP标准，每一行记得带上换行符\n，不然服务器不返回请求
请求行: 方法 uri http版本
请求头: Host:... Connection:...
请求体:...
'''
def socket_http():
	http_headers=b'GET / HTTP/1.1 \nHost:www.sina.com.cn\nConnection:close\n\n'

	s.send(http_headers)
	buffer=[]
	while True:
		msg=s.recv(2048)
		#如果接送到信息则放入列表中
		if msg:
			buffer.append(msg)
		#否则关闭socket,退出循环	
		else:
			s.close()
			break
	Response=b''.join(buffer)
	return Response
def data_write(data):
	with open('e:/1.html','wb') as f:
		f.write(data)
		f.close()
if __name__ == '__main__':

	data=socket_http()
	print(data)
	data_write(data)


	
