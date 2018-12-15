# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 0015 上午 9:57
# @Author  : 杨宏兵
# @File    : 2.4.7 创建UDP客户端.py
# @Software: PyCharm
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('->:')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)
udpCliSock.close()