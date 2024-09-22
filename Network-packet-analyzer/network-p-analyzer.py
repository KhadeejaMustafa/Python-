# As the name already explains what this program does. The program will capture ingoing and outgoing packets, decode them 
# and extract useful information that will aid in analyzing for any anomalities. Furthermore, we will present that information 
# in a way that is easy to read and understand.
# the library we will use in this project is: Scapy

import scapy.all as scapy

def save_sniff_packet(interface, outputfile):
 try:
      while True:
          packet = scapy.sniff(iface = interface, count = 5)[0]
          if scapy.IP in packet: 
              save_packet_info_to_file(packet, outputfile)




 except Exception as e:
     print(f'there\s an Error: \n{e}')

def save_packet_info_to_file(packet, filename):
 with open(filename, "a") as file:
    file.write('Packet Details:/n')
    file.write(f'Source IP address: {packet[scapy.IP].src}\n ')
    file.write(f'Destination IP address: {packet[scapy.IP].dst}\n ')

    if scapy.TCP in packet:
       file.write(f'Source Port: {packet[scapy.TCP].sport}\n ')
       file.write(f'Destination Port: {packet[scapy.TCP].dport}\n ')

    elif scapy.UDP in packet:
      file.write(f'Source Port: {packet[scapy.UDP].sport}\n ')
      file.write(f'Destination Port: {packet[scapy.UDP].dport}\n ')

    file.write('Packet Contents: \n')
    file.write(str(packet) + '\n\n')
 
def main():
   interface = 'Wi-Fi'
   outputfile = "E:\packets_captured_info.txt" # location of the output file

   print(f'sniffing packets over the interface {interface}...')
   save_sniff_packet(interface, outputfile)

if __name__ == '__main__':
   main()
