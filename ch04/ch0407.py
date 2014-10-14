from datetime import datetime
from time import sleep
import subprocess
for count in range(0, 60): 
    filename = str(datetime.now()) + ".jpg"
    subprocess.call(["fswebcam", filename])
    sleep(60)