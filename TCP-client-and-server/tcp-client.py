# this program will be used to develop a TCP client using socket library in Python.

import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientSocket.connect(('host', port)) #replace host with the IP address
message = clientSocket.recv(1024)
clientSocket.close()

print(message.decode('ascii'))
