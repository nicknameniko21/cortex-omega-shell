import os
import time
while True:
    if os.path.exists("autorun.sh"):
        os.system("bash autorun.sh")
    time.sleep(10)
