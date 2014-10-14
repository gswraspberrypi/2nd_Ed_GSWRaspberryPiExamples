# Getting Started with Raspberry Pi Ch 4 Example 2

import pygame

pygame.init()
screen = pygame.display.set_mode((450, 450))
background = pygame.image.load("background.png") 
background.convert_alpha() 
screen.blit(background, (0, 0))
while True:
    pygame.display.update()
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
