import serial

port = "/dev/ttyACM0"
serialFromArduino = serial.Serial(port,9600) 
serialFromArduino.flushInput() 
while True:
    input = serialFromArduino.readline()
    inputAsInteger = int(input) 
    print(inputAsInteger) 