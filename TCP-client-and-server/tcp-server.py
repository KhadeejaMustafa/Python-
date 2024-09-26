# this program will we used to develop a TCP server, using socket library in Python.
# socket methods used: .sock(), .gethostname(), .bind(), .listen(), .accept()

import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creating 'serverSocket' object. AF_NET = IPv4, SOCK_STREAM = TCP

host = socket.gethostname()
port = 80

serverSocket.bind((host, port))
serverSocket.listen(4)

while True:
    clientSocket, address = serverSocket.accept()
    print(f'Recieved connection from {str(address)}')

    messageToClient = "Thank you for establishing connection with " + host
    clientSocket.send(messageToClient)
    clientSocket.close()
