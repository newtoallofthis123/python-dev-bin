# Name of the Project : alaram-cli.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : datetime, playsound

''' The following is registered under the MIT License, NoobScience 2021. You are free to use it
as you like as long as you know what you are doing.
Enjoy using and check some of my other projects at https://github.com/newtoallofthis123'''

# Don't Change the code after this line unless you know what you are doing.

#! /usr/bin/env python3

'''
A simple cli tools written in python to set alarm in 12hr format and
ring you favorite song or tune as an alarm. By NoobScience. To use it,
just switch to the directory you stored it in and open the terminal there and
type python alarm.py
Available for Windows, Mac, Linux and written in python'''

# Enter the path to the Sound or Song you want to play as the alarm at line 66

# Importing the neccesary modules
from datetime import datetime   #To set date and time
from playsound import playsound     #To play sound

# Defining function validate_time to Validate the time format entered by the user
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"

# Setting alarm and informing the user that the alarm has been set
while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        print(f"Done setting alrm. It will ring at {alarm_time}")
        break
    
# defining the alarm variables
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
