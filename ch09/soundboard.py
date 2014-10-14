import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)

soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav") 
soundB = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Left.wav")
soundC = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Right.wav")

soundChannelA = pygame.mixer.Channel(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelC = pygame.mixer.Channel(3)

print "Soundboard Ready." 

while True:
   try:
      if (GPIO.input(23) == True): 
         soundChannelA.play(soundA)
      if (GPIO.input(24) == True):
         soundChannelB.play(soundB)
      if (GPIO.input(25) == True):
         soundChannelC.play(soundC)
      sleep(.01) 
   except KeyboardInterrupt:
      exit()