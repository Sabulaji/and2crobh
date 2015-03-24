#-*- coding:utf-8 -*-
from socket import *
 
host = '192.168.137.3'
port = 8888
bufsiz =1024
addr = (host, port)

def SendComand(cmd):
	s=socket(AF_INET, SOCK_STREAM)
	s.connect(addr)
	s.send(cmd)
	s.close

while 1:	
	cmd = raw_input("command:")
	if cmd == "quit":quit()
	SendComand(cmd)
	