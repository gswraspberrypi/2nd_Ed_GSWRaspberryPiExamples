import serial, sys

if (len(sys.argv) != 2): 
    print("Usage: python ReadSerial.py port") 
    sys.exit()
port = sys.argv[1] 
serialFromArduino = serial.Serial(port,9600) 
serialFromArduino.flushInput() 
while True:
   if (serialFromArduino.inWaiting() > 0):
       input = serialFromArduino.read(1) 
       print(ord(input)) 