# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 0015 上午 9:34
# @Author  : 杨宏兵
# @File    : 2.4.6 创建UDP服务器.py
# @Software: PyCharm
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto(('[%s] %s' % (ctime(), data)).encode('utf-8'), addr)
    print('.....received from and returned to:', addr)
udpSerSock.close()