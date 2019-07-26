#!/usr/bin/env python3
from socket import *
import os,sys
addr=('0.0.0.0',9999)
def dochild(s):
    while True:
        data=s.recv(1024).decode('utf-8')
        print(data)
def doparent(s):
    while True:
        data=input()
        s.sendto(b'C '+name+b' '+data.encode('utf-8'),addr)
def dologin(s):
    while True:
        global name
        name=input('please input your name:')
        s.sendto(('L %s' % name).encode('utf-8'),addr)
        status=s.recv(1024).decode('utf-8')
        if status=='OK':
            return True
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    if dologin(s):
        pid=os.fork()
        if pid<0:
            sys.exit('创建进程失败')
        elif pid==0:
            dochild(s)
        else:
            doparent(s)
if __name__=='__main__':
    main()
