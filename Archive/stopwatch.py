import time
import os

print("Press Enter to begin and Ctrl + C to exit")
os.system('color a')
while True:
    try:
        input()
        start = time.time()
        print("Started")
        while True:
            print(round(time.time() - start, 0), 'secs', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopped')
        endtime = time.time()
        print('Total Time:', round(endtime - start, 2), 'secs')
        break