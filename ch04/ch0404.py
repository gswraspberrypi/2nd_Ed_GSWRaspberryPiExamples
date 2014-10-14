# GSW Raspberry Pi ch 3 example 4

from datetime import datetime
from time import sleep
import random

log = open("log.txt", "w")

for i in range(5):
    now = str(datetime.now())
    # Generate some random data in the range 0-1024
    data = random.randint(0, 1024)
    log.write(now + " " + str(data) + "\n")
    print(".")
    sleep(.9)
log.flush()
log.close()
