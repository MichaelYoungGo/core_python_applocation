# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 0018 下午 2:48
# @Author  : 杨宏兵
# @File    : 2.5.2 创建SocketServer TCP客户端.py
# @Software: PyCharm
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('>>>>:')
    if not data:
        break
    tcpCliSock.send(('%s\r\n' % data).encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    tcpCliSock.close()