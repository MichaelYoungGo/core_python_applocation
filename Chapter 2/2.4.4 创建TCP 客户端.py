# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 0014 下午 1:10
# @Author  : 杨宏兵
# @File    : 2.4.4 创建TCP 客户端.py
# @Software: PyCharm
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()

