import socket 
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.1.207",21))
answer = s.recv(1024)

if ("FreeFloat Ftp Server (Version 1.00)" in answer):
   print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDeamon FTP Server Version 2.0" in answer):
    print "[+] 3CDeamon FTP Server is vulnerable."
elif ("Ability Server 2.34" in answer):
    print "[+] Ability Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in answer):
    print "[+] Sami FTP Server is vulnerable."
else: 
 print "[-] FTP Server is not vulnerble."


