# 整体流程
# 1. 链接wifi
# 2. 启动网络功能（UDP）
# 3. 接收网络数据
# 4. 处理接收的数据


import socket
import time
import network
import machine
from machine import Pin


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('TP-LINK_4311', '85858589')
        i = 1
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            i += 1
            time.sleep(1)
    print('network config:', wlan.ifconfig())


def start_udp():
    # 2. 启动网络功能（UDP）

    # 2.1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.2. 绑定本地信息
    udp_socket.bind(("0.0.0.0", 7788))

    return udp_socket


def main():
    # 1. 链接wifi
    do_connect()
    # 2. 创建UDP
    udp_socket = start_udp()
    # 3. 创建灯对象
    r = machine.Pin(4, machine.Pin.OUT)
    l = machine.Pin(15, machine.Pin.OUT)
    # 4. 接收网络数据
    while True:
        recv_data, sender_info = udp_socket.recvfrom(1024)
        print("{}发送{}".format(sender_info, recv_data))
        recv_data_str = recv_data.decode("utf-8")
        try:
            print(recv_data_str)
        except Exception as ret:
            print("error:", ret)
        
        # 5. 处理接收的数据
        if recv_data_str == "r1":
            r.on()
        elif recv_data_str =="l1":
            l.on()
        elif recv_data_str =="r0":
            r.off()
        elif recv_data_str == "l0":
            l.off()

if __name__ == "__main__":
    main()
