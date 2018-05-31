import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 8848))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))

while True:
    send_data=input('type whatever you what!')
    if send_data=='exit':
        s.close()
        break
   # 发送数据:
    s.send(send_data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))

