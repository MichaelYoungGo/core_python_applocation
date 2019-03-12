# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 20:50
# @Author  : 杨宏兵
# @File    : 3.2.6 客户端FTP程序示例.py
# @Software: PyCharm
import ftplib
import os
import socket

HOST = "202.196.160.15"
DIRN = "pub/mozilla.org/webtools"
FILE = "bugzilla-LATEST.tar.gz"

def main():
    try:
        print('创建连接')
        f = ftplib.FTP(HOST)
        print('正在连接中..........')
    except (socket.error, socket.gaierror) as e:
        print("ERROR: cannot reach %s" %HOST)
        print(e)
        return
    print('连接成功！！')

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anouymously')
        f.quit()
        return
    print("*** Logged in as 'anonymously'")




if __name__ == "__main__":
    main()