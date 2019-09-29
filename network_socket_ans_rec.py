import socket 
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.1.207",21))
answer = s.recv(1024)
print answer 

