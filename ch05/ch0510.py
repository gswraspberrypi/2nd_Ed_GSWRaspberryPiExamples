import pygame
import pygame.midi

pygame.init()
pygame.midi.init()
for id in range(pygame.midi.get_count()): 
    print pygame.midi.get_device_info(id)