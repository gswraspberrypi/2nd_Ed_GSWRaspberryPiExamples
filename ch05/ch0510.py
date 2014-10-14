# Getting Started with Raspberry Pi Ch 4 Example 10

import pygame
import pygame.midi

pygame.init()
pygame.midi.init()
for id in range(pygame.midi.get_count()): 
    print pygame.midi.get_device_info(id)