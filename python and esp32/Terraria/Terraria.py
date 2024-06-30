import pygame

# 初始化
pygame.init()

# 设置
win_kuan = 850
win_gao = 500

m_l = False

m_r = False

h_x=400
h_y=200

x=1000
y=1000

cc = [(400,300)]

def sjc(x,y):
    win.blit(P,(x,y))

# 创建窗口
win = pygame.display.set_mode((win_kuan, win_gao))

# 设置窗口
pygame.display.set_caption("Terraria")

small_photo_title = pygame.image.load(r"photo\title.png")
pygame.display.set_icon(small_photo_title) 

#NPC
haed = pygame.image.load(r"photo\ren.png")
P = pygame.image.load(r"photo\tu.png")

#时钟
time = pygame.time.Clock()

# 循环
done = True
while  done:
    # 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = not done
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                m_l = True
            elif event.key == pygame.K_RIGHT:
                m_r = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                m_l = False
            elif event.key == pygame.K_RIGHT:
                m_r = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            a,b = pygame.mouse.get_pos()
            aa = (a-(h_x+25))**2
            bb = (b-(h_y+50))**2
            c = aa + bb
            if c<14400:
                a = a//50*50
                b = b//50*50
                if (a,b) not in cc:
                    cc.append((a,b))
                print(cc)

    if m_l == True and h_x>=5:
         h_x -= 5
    elif m_r == True and h_x<=745:
         h_x+= 5

    # 绘制
    win.fill((0, 162, 232))

    win.blit(haed,(h_x,h_y))
    
    for (x,y)in cc:
        sjc(x,y)
    
    # 更新
    pygame.display.update()

    # 帧率
    time.tick(60)

# 退出
pygame.quit()
