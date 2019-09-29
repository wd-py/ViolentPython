# Dictionaries
#Key and Value

services = {'ftp':21,"ssh":22,"smtp":25,"http":80}

print "Keys of services"
print services.keys()

print "Items of dictionary: services"
print services.items()



print "services.has_key('ftp')"
print services.has_key('ftp')


print "Value of service dictionary ex.  services['ftp']"
print services['ftp'] 

print "[+] Found volun with FTP on port " +str(services['ftp'])
