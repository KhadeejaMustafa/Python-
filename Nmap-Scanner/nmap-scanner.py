# Nmap scanner will ask the user to input an IP address of choice, and choose which type of scan they want to run.
import nmap

scanner = nmap.PortScanner()
print("------ Nmap automation tool ------")

ip_address = input('Please enter the IP address you wish to scan: ')
print(f'The IP address you entered: ', ip_address)
type(ip_address)

response = input("""\n Select the type of scan you wish to run:
                     1. SYN ACK Scan
                     2. UDP Scan
                     3. Comprehensive Scan\n """)
print(f'The scan type you selected is: ', response)

if response == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_address].state()) # prints the status of the IP address; up or down
    print(scanner[ip_address].all_protocols) 
    print('Open ports: ', scanner[ip_address]['tcp'].keys())

elif response == '2':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU') # UDP scan
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_address].state()) 
    print(scanner[ip_address].all_protocols) 
    print('Open ports: ', scanner[ip_address]['udp'].keys())

elif response == '3':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sC -sV -A -O')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols()) 
    print('Open ports: ', scanner[ip_address]['tcp'].keys())

else:
    print("Invalid input.")


