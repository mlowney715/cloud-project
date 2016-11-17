# TCP Client (simple echo code in Python)

# Import socket module and system module
from socket import *
import sys

if len(sys.argv) <= 2:
	print 'Usage: "python TCPclient.py server_address server_port"'
	sys.exit(2)

# Create a TCP client socket: (AF_INET for IPv4 protocols, SOCK_STREAM for TCP)
clientSocket = socket(AF_INET, SOCK_STREAM)

# Request a TCP connection to the TCP server welcome socket: host = argv[1] & port = argv[2]
clientSocket.connect((sys.argv[1], int(sys.argv[2])))
f = open('myfile.pdf', 'wb')


#do something (request for a file)
while True:
        print 'recd con'        
        message = raw_input ("Type 'm' for a pdf file from the server: ")
	clientSocket.send(message)#send the letter 'm'
        l= clientSocket.recv(10241024)#receive
        while (l):
                print "receiveing.."
                f.write(l)#write to the file
                l= clientSocket.recv(10241024)#receive 1MB at a time
        f.close()
        print "done"
        clientSocket.close()#close the socket
        sys.exit(0)
