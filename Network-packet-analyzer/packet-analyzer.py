# incomplete

''' As the name already explains what this program does. The program will capture ingoing and outgoing packets, decode them 
and extract useful information that will aid in analyzing for any anomalities. Furthermore, we will present that information 
in a way that is easy to read and understand. '''

# the libraries we will use in this project, are: Scapy, dpkt, socket, time, psutil and prettytable

from scapy.all import sniff

def packet_handler(packet):
    print(packet.summary())

sniff(prn = packet_handler, count = 15)
