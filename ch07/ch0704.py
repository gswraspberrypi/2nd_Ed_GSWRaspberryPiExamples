from pyfirmata import Arduino
from time import sleep
board = Arduino('/dev/ttyACM0')
while (1):
    board.digital[13].write(1)
    print("on")
    sleep(1)
    board.digital[13].write(0)
    print("off")
    sleep(1)