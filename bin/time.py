from datetime import datetime
from datetime import date
import time
from time import strftime, gmtime
import os

def ti():
    x = strftime("%H:%M:%S %p", gmtime())
    os.system('color a')
    os.system('cls')
    print(x)
#print(datetime.now())
y = True
while y:
    time.sleep(1)
    ti()