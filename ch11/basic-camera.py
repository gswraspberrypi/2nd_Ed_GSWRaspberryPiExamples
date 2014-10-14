from SimpleCV import Camera, Display
from time import sleep

myCamera = Camera(prop_set={'wdith': 320, 'height': 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
   myCamera.getImage().save(myDisplay)
   sleep(.1)