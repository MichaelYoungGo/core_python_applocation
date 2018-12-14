# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 0014 下午 12:56
# @Author  : 杨宏兵
# @File    : 2.4.3 创建TCP服务器.py
# @Software: PyCharm
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection.....')
    tcpCliSock, addr = tcpSerSock.accept()
    print('.....connected from : ', addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s' % (ctime(), data)).encode('utf-8'))
        print('收到数据，服务器在运行！！')
    tcpCliSock.close()
tcpSerSock.close









