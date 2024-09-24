# This port scanner will ask the user to enter the ip address, and which-ever port number they would like to scan. 
# The program will return either the port is open or closed.

import socket

sock_et = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_et.settimeout(4)

host = input('Enter IP address of host: ')
port = int(input('Enter Port number to scan: '))
def portScanner(port):
  if sock_et.connect_ex((host, port)):
    print(f'port {port} is closed.')
  else:
   print(f"port {port} is open.")


portScanner(port)
