# TCPServer.py
# Section 2.7.2 TCP Socket Programming page 167

from socket import *

serverPort = 4321
serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

s = open('animals.jpg','rb')
m = open('realbook.pdf', 'rb')
b = open('en_windows_10_education_version_1607_updated_jul_2016_x86_dvd_9055803.iso', 'rb')

serverSocket.listen(1)	# serverSocket is the welcoming Connection

print 'The server is ready to receive'

while 1:
    connectionSocket, addr = serverSocket.accept()
    try:
        print("Connection Received: "+addr[0])

        req = connectionSocket.recv(1024)
        print("Received a request for "+req)
        if req == 't':
            connectionSocket.send("YOU GET NOTHING")
            print("Got here")
        elif req == 's':
            l = s.read(1024*1024)
            while(l):
                print("Sending a picture")
                connectionSocket.send(l)
                l = s.read(1024*1024)
        elif req ==  'm':
            l = m.read(1024)
            while(l):
                print("Sending a book")
                connectionSocket.send(l)
                l = m.read(1024)
        elif req ==  'b':
            l = b.read(1024)
            while(l):
                print("Sending an operating system")
                connectionSocket.send(l)
                l = b.read(1024)

        print("Done Sending")
        connectionSocket.close()
    except:
        connectionSocket.close()
