# Name of the Project : NS-Calendar.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : datetime

# Don't Change the code after this line unless you know what you are doing.

#! /usr/bin/env python3

'''
A simple cli tools written in python to look at the calendar in your terminal. By NoobScience. To use it,
just switch to the directory you stored it in and open the terminal there and
type python alarm.py
Available for Windows, Mac, Linux and written in python'''

#                                              NS-CALENDAR
''' The following is registered under the MIT License, NoobScience 2021. You are free to use it
as you like as long as you know what you are doing.
Enjoy using and check some of my other projects at https://github.com/newtoallofthis123'''

# The Module datetime is being used here, It is installed by deflaut in python3 or you can download it and append the file directory in the below code
from datetime import date
import datetime

# A whole database of conversion parameters I am using. If you want your own shortcuts, add some to the code below
monthConversions = {
    "january": 1,
    "febuary": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
    "j": 1,
    "f": 2,
    "m": 3,
    "a": 4,
    "ma": 5,
    "j": 6,
    "ju": 7,
    "au": 8,
    "s": 9,
    "o": 10,
    "n": 11,
    "d": 12,
}

#Intro
print("                                    NS-CALENDAR                                              ")
print("                                                           by NoobScience                    ")
print("Hello, today is a wonderfull day.")
print("                            Today, the date is " + str(date.today()))

# using datetime module to show current date and time
from datetime import datetime

current = datetime.now()
current_time_in_format = current.strftime("%H:%M:%S")
print("                            The current time is " + (current_time_in_format))

#The Module calendar is being used to render a text calendar
import calendar

#Providing Logic to the CLI tool
chk = str.upper(input("Do you want to see the calender? (Y/N)"))
if chk == "Y":
    year = int(input("Which year?"))
    chk1 = str.lower(input("The Whole Year or a Particular Month? (Whole/Month)"))
    if chk1 == "whole":
            print("Showing you the calendar of " + str(year))
            print(calendar.calendar(year))
    elif chk1 == "month":
            month = str.lower(input("Which Month?(January,Febuary...) "))
            month_converted = int(monthConversions[month])
            print(calendar.month(year, month_converted))
    else:
        print("Sorry Invalid operator, try again")
elif chk == "N":
    print("Okay, Have a Nice Day \nNoobScience")
else:
    print("Sorry Invalid operator, try again")

#Thanks for using NS-Calendar
