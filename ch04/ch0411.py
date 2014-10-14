# Getting Started with Raspberry Pi Ch 4 Example 11

import pygame
from time import sleep
pygame.init()
screen = pygame.display.set_mode((320,240)) 
movie = pygame.movie.Movie("foo.mpg")
movie.play()
while True:
    if not(movie.get_busy()):
        print("rewind")
        movie.rewind()
        movie.play()
    if pygame.QUIT in [e.type for e in pygame.event.get()]:
        break
