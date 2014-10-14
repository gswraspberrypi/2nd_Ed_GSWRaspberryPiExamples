# Getting Started with Raspberry Pi Ch 4 Example 9

import pygame.mixer
from time import sleep

pygame.mixer.init(48000, -16, 1, 1024) 

sound = pygame.mixer.Sound("WilhelmScream.ogg")
channelA = pygame.mixer.Channel(1)
channelA.play(sound)
sleep(2.0)

