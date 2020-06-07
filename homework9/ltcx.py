# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；
#消息发送端--客户端
 
import socket
#创建一个socket，用函数socket()；
client_send = socket.socket(type=socket.SOCK_DGRAM)
# 设置对方的IP地址和端口等属性;
ip_port = ("11.10.54.63",10086)
#发送数据，用函数sendto()
msg = input("请输入消息：")
client_send.sendto(bytes(msg,encoding="utf-8"),ip_port)
#关闭网络连接；
client_send.close()
#消息接收端--服务器端
 
client_send = socket.socket(type=socket.SOCK_DGRAM)
ip_port = ("11.10.54.63",10086)
client_send.bind(ip_port)
data,addr = client_send.recvfrom(1024)
print(str(data,encoding="utf-8"))
# 关闭网络连接
client_send.close()