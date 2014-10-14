# GSW Raspberry Pi ch 3 example 3

from datetime import datetime
from time import sleep

while True:
    now = str(datetime.now())
    print(now)
    sleep(1)