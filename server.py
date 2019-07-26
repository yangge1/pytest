#!/usr/bin/env python3
from socket import *
import os,sys
user={}
def cicleSend(s,ctype,curnam,msg=''):
    for name in user:
        if ctype=='L':
            s.sendto(('%s join the room' % curnam).encode('utf-8'),user[name])
        elif ctype=='C':
            s.sendto(('%s say:%s' % (curnam,msg)).encode('utf-8'),user[name])
        else:
            pass
        
def dochild():
    pass
def dologin(s,name,addr):
    if name not in user:
       user[name]=addr 
       s.sendto(b'OK',addr)
       cicleSend(s,'L',name)
    else:
        s.sendto(b'faild',addr)
def dochart(s,data,name):
    cicleSend(s,'C',name,data)
def doparent(s):
    while True:
        data,addr=s.recvfrom(1024)
        data=data.decode('utf-8')
        darr=data.split(' ')
        if data[0]=='L':
            dologin(s,darr[1],addr)
        elif data[0]=='C':
            dochart(s,darr[2],darr[1])
        else:
            pass
def main():
    s=socket(AF_INET,SOCK_DGRAM)
    s.bind(('0.0.0.0',9999))
    doparent(s)
if __name__=='__main__':
    main()
