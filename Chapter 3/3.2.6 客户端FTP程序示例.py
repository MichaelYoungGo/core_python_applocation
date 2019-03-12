# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 20:50
# @Author  : 杨宏兵
# @File    : 3.2.6 客户端FTP程序示例.py
# @Software: PyCharm
import ftplib
import os
import socket

HOST = "ftp.mozilla.org"
DIRN = "pub/mozilla.org/webtools"
FILE = "bugzilla-LATEST.tar.gz"

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print("ERROR: cannot reach %s" %HOST)
        print(e)
        return

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anouymously')
        f.quit()
        return
    print("*** Logged in as 'anonymously'")




if __name__ == "__main__":
    main()