import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

count = 0

while True:
   inputValue = GPIO.input(24)
   if (inputValue == True):
      count = count + 1
      print("Number of times the button has been pressed: " + int(count))
   time.sleep(.01)