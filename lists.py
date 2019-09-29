
portList = []

#port FTP
portList.append(21)
#port http
portList.append(80)
#port https
portList.append(443)
#port SMTP NIEZALECANY!!!!
portList.append(25) 

print portList


portList.sort()
print portList


portList.sort()
position = portList.index(80)

print "[+] There are "+str(position)+" ports to scan before 80."


portList.remove(443)
print portList 


cnt = len(portList)
print "[+] Scanning "+str(cnt)+" total ports."

