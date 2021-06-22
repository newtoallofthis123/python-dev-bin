import time
from time import strftime
from playsound import playsound

# NoobScience
# 07:49:00 PM

def validate():
    if len(time_to_set) != 11:
        return("Invalid format")




time_to_set = str(input("Input time in HH:MM:SS AM/PM"))
set_hr = time_to_set[0:2]
print(set_hr)
