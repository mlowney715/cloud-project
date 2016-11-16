# TCPClient.py
# Section 2.7.2 TCP Socket Programming page 164

from socket import *

serverName = '192.168.0.101'
serverPort = 4321
clientSocket = socket(AF_INET, SOCK_STREAM)

# TCP Socket has been created

clientSocket.connect((serverName,serverPort))

# Three way handshake happens

sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)	# Bytes dropped right into TCP Connection

modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
