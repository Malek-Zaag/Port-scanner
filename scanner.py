#!bin/python3

import sys
import socket
from datetime import datetime as dt

#Define our target

if len(sys.argv) ==2:
	target=socket.gethostbyname(sys.argv[1])
else:
	print('invalid arguments')
	print('Syntax: python3 scanner.py <ip>')
	sys.exit()

print ("-"* 50)
print ("scanning target "+ target)
print ("Time started "+str(dt.now()))
print ("-"* 50)
try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target,port))
		print("checking port{}".format(port))
		if result ==0:
			print("Port {} is open :D".format(port))
			s.close()
except KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()
except socket.gaierror:
	print("Hostname cannot be resolved ")
	sys.exit()
except socket.error:
	print("couldnt connect to server")
	sys.exit()


