from playsound import playsound
import time
from time import strftime

def validate(set_alarm):
    if len(set_alarm) != 11:
        return "Invalid format, try again"
    else:
        if int(set_hr) > 12:
            return "Invalid format, try again"
        elif int(set_min) > 59:
            return "Invalid format, try again"
        elif int(set_sec) > 59:
            return "Invalid format, try again"
        else:
            return "Validated, Set Alarm"

while True:
    set_alarm = input("input as HH:MM:SS AM/PM: ")
    set_hr = set_alarm[0:2]
    set_min = set_alarm[3:5]
    set_sec = set_alarm[6:8]
    set_am_pm = str.upper(set_alarm[8:11])
    valid = validate(set_alarm.lower())
    if valid != "Validated, Set Alarm":
        print(valid)
    else:
        print(f"Setting Alarm for {set_alarm}")
        break

set_hr = set_alarm[0:2]
set_min = set_alarm[3:5]
set_sec = set_alarm[6:8]
set_am_pm = str.upper(set_alarm[8:11])

while True:
    time_now = strftime("%I:%M:%S %p")
    hr = time_now[0:2]
    min_ = time_now[3:5]
    sec = time_now[6:8]
    am_pm = time_now[8:11]
    if set_hr == hr:
        if set_min == min_:
            if set_sec == sec:
                if set_am_pm == am_pm:
                    playsound("D:\Songs\Hailee Steinfeld, Alesso - Let Me Go ft. Florida Georgia Line, WATT (Official Video)-BQ_0QLL2gqI.wav")

