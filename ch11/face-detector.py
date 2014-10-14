from SimpleCV import Camera, Display
from time import sleep

myCamera = Camera(prop_set={'width':320, 'height': 240})

myDisplay = Display(resolution=(320, 240))

while not myDisplay.isDone():
   frame = myCamera.getImage()
   faces = frame.findHaarFeatures('face')
   if faces:
      for face in faces:
         print "Face at: " + str(face.coordinates())
   else:
      print "No faces detected."
   frame.save(myDisplay)
   sleep(.1)