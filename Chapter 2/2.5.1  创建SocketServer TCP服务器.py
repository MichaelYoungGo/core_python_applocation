# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 0018 下午 2:34
# @Author  : 杨宏兵
# @File    : 2.5.1  创建SocketServer TCP服务器.py
# @Software: PyCharm

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequuestHandler(SRH):
    def handle(self):
        print('oonnected from:', self.client_address)
        self.wfile.write(('[%s] %s' % (ctime(), self.rfile.readline())).encode('utf-8'))
tcpServ = TCP(ADDR, MyRequuestHandler)
print('waiting for connecting...')
tcpServ.serve_forever()