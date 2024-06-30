import network
import time
from socket import *
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('TP-LINK_4311', '85858589')
    while not wlan.isconnected():
        pass
print('network config:', wlan.ifconfig())
udp_socket=socket(AF_INET,SOCK_DGRAM)
dest_addr=('192.168.0.103',5353)
send_data='hello_world'
while True:
    udp_socket.sendto(send_data.encode('utf-8'),dest_addr)