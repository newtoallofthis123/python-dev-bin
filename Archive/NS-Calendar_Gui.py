# Name of the Project : Calendar.py
# Written by NoobScience : https://github.com/newtoallofthis123
# Modules Used : calendar, tkinter

# Don't Change the code after this line unless you know what you are doing.

''' The following is registered under the MIT License, NoobScience 2021. You are free to use it
as you like as long as you know what you are doing.
Enjoy using and check some of my other projects at https://github.com/newtoallofthis123'''

#! /usr/bin/env python3

'''
A simple program to see the calendar of any year. By NoobScience. To use it,
just switch to the directory you stored it in and open the terminal there and
type python Calendar.py or use the .exe file
Available for Windows, Mac, Linux and written in python'''

# Importing necessary Modules
from tkinter import *
import calendar

# Try the following code, if it fails, go to except
try:

# Creating a User Interface
    gui = Tk()
    gui.geometry("400x300")
    gui.title("NS-Calendar")
    gui.configure(bg="#4A3B52")
    
# Change the icon path between these comments ar file="/icon path"
    photo = PhotoImage(file = "/IJ_Calendar.png")
# Don't Change the code below this line to change the icon

    gui.iconphoto(False, photo)
    gui.resizable(False,False)

# defining function called cal to get the calendar of the month and year provided by the user
    def cal():
        month_int = int(month.get())
        year_int = int(year.get())
        cal = calendar.month(year_int, month_int)
        textfield.delete(0.0, END)
        textfield.insert(INSERT, cal)
        
# Label to define text boxes

    label1 = Label(gui, text="Month:", bg="#C5FFB8", font=("Arial", 18),)
    label1.grid(row=0, column=5)

    label2 = Label(gui, text="Year:", bg="#C5FFB8", font=("Arial", 18),)
    label2.grid(row=0, column=6)

# Defining the spin boxes to select the month and year
    month = Spinbox(gui, from_=1, to=12, width=8, bg="#FA8574")
    month.grid(row=1, column=5, padx=5)

    year = Spinbox(gui, from_=2000, to=2100, width=10, bg="#FA8574")
    year.grid(row=1, column=6, padx=10)

# Button to call upon the calendar, calling upon the function cal
    button = Button(gui, text="Get The Calendar", command=cal, fg="black", bg="#FDA600")
    button.grid(row=1, column=7, padx=10)

# Text field to print the calendar
    textfield = Text(gui, width=20, height=10, fg="black", bg="#FFC400")
    textfield.grid(row=2, columnspan=12, padx=5, pady=5)

# Loop through this
    gui.mainloop()

# What happens if an error is encountered
except:
    print("Sorry, something went wrong")
    choice = input("Do you want to trouble shoot? (y/n): ")
    if choice=="y":
        print("Check if all necessary Modules are installed., Check for: ")
        print("Modules: ")
        print(" pyperclip: pip install calendar,")
        print(" Check if the icon is present: ")
        print("Check the code at line 31, you should change the icon path between the comments")
        print("Check if you have python installed properly.")
        print("If not, get another version of this from my repository https://github.com/newtoallofthis123")
    elif choice=='n':
        print("Okay, Thanks for using. Check out my other projects at https://github.com/newtoallofthis123")

    else:
        print("Thanks for using")

# Enjoy

