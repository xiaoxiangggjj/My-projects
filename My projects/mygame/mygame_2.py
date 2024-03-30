import sys
import pygame
import random

#初始化 创建窗口 和画布
pygame.init()
pygame.display.set_mode((500,900))
sceern = pygame.display.get_surface()
pygame.display.set_caption("my first game")
#设置时钟
clock = pygame.time.Clock()

#加载元素
background = pygame.image.load('6065b404c7b5ceff18cd98fcecdbbdd.png')
block_w_1 = pygame.image.load('white.png')
block_b_2 = pygame.image.load('black.png')
block_r_3 = pygame.image.load('red.png')
block_y_4 = pygame.image.load('yellow.png')
#combine = pygame.image.load('270×230.png')

#创建游戏背景
sceern.blit(background,(0,0))
pygame.display.update()

#打包游戏色块
block = [block_w_1, block_b_2 ,block_r_3,block_y_4]

#创建色块更新类
class update:
    def __init__(self):
        self.current = None
    def update_block(self):
        self.current = random.randint(0,3)
        sceern.blit(block[self.current],(110,410))
        pygame.display.update()

#创建对象
current_block = update()

#设置色块索引
current_block_current = 0

#添加游戏得分参数
score = 0

#游戏运行过程
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]==1 :
                sceern.blit(block[0],(110,410))
                pygame.display.update()
            elif keys[pygame.K_UP]==1 and current_block_current==0:
                current_block.update_block()
                current_block_current = current_block.current
                score +=10
                continue
            elif keys[pygame.K_DOWN]==1 and current_block_current==1:
                current_block.update_block()
                current_block_current = current_block.current
                score +=10
                continue
            elif keys[pygame.K_RIGHT]==1 and current_block_current==2:
                current_block.update_block()
                current_block_current = current_block.current
                score +=10
                continue
            elif keys[pygame.K_LEFT]==1 and current_block_current==3:
                current_block.update_block()
                current_block_current = current_block.current
                score +=10
                continue
            else:
                print('your score = ',score)
                print('game over')
                pygame.quit()
                sys.exit()
    pygame.display.update()
        



