# TCPServer.py
# Section 2.7.2 TCP Socket Programming page 167

from socket import *
import sys
import thread

def clientConnection(connectionSocket, addr):
    print("Connection Received: "+addr[0])
    s = open('small','rb')
    m = open('medium', 'rb')
    b = open('medium', 'rb')
    connected = 1;
    while connected:
        try:
            req = connectionSocket.recv(1024)
            print("Received a request for "+req)
            if req == 't':
                connectionSocket.send("YOU GET NOTHING")
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
            elif req == 'q':
                connectionSocket.close()
                connected = 0
            print("Done Sending")
        except:
            connectionSocket.close()

running = 1
serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))


serverSocket.listen(5)	# serverSocket is the welcoming Connection

while running:
    print("The server is ready to receive")
    thread.start_new_thread(clientConnection, serverSocket.accept())
