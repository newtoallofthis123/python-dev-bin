import time
from datetime import datetime
from playsound import playsound

print("Timer")

alarm_time = input("Enter time in format HH:MM:SS AM/PM")

alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

# Defining variables to take action when alarm time is reached
while True:
    now = datetime.now()

    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

# Defining when the alarm time is reached to the program
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_min == current_min:
                if alarm_sec == current_sec:
                    print("Alarm Done")
                    # Set the Path to your song between the two comments
                    playsound("D:\Songs\Hailee Steinfeld, Alesso - Let Me Go ft. Florida Georgia Line, WATT (Official Video)-BQ_0QLL2gqI.wav")
                    # Don't Change the code after this to change the song
                    break
    


