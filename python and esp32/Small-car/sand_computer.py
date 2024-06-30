import socket  
import time
import pygame
import sys



#加载界面

# 初始化
pygame.init()
# 创建窗口
win = pygame.display.set_mode((200, 200))

# 设置窗口
pygame.display.set_caption("Small Car")

small_photo_title = pygame.image.load(r"car.png")
pygame.display.set_icon(small_photo_title)


  
def send(message):  
    # 创建一个UDP套接字  
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
      
    # 发送数据到指定的主机和端口  # 设置接收程序所在设备的IP地址和端口号  
    udp_socket.sendto(message.encode("utf-8"), ('192.168.0.105', 7788))  
      
    # 关闭套接字  
    udp_socket.close()  



user_input = "1"
a = True

while  a:
    # 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            a = not a
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                send("l1")
            elif event.key == pygame.K_RIGHT:
                send("r1")

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                send("l0")
            elif event.key == pygame.K_RIGHT:
                send("r0")

#退出
pygame.quit()

