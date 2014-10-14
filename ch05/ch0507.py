# Getting Started with Raspberry Pi Ch 4 Example 7

import pygame
import random
from time import sleep

running = True
pygame.init()
screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
while running:
    pygame.draw.circle(screen, 
                       pygame.Color(int(random.random()*255),
                                    int(random.random()*255),
                                    int(random.random()*255)), 
                       (int(random.random()*1500),int(random.random()*1500)), 
                       int(random.random()*500), 0)
    pygame.display.update()
    sleep(.1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False
pygame.quit()
