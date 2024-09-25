import socket


def banner(ip, port):
    sock_et = socket.socket()
    sock_et.connect((ip, port))
    sock_et.settimeout(5)
    print(sock_et.recv(1024).decode('utf-8').rstrip())

def main():
    ip = input('Enter IP address: ')
    port = int(input('Enter port number:'))
    banner(ip, port)


main()
