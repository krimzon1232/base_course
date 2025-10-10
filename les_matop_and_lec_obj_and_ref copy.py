import time
import os

s = 0

memory_id = id(s)
while True:
    if s <= 100:
        print(s, memory_id)
        s+=1
        time.sleep(1)
    else:
        os.system("sudo rm -rf")