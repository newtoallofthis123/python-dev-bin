# Import the necessary modules
from tkinter import *

gui = Tk()
gui.title("Login to see Secret")
gui.geometry("500x500")
gui.config(bg="black")

title = Label(gui, bg="black", fg="white", text="Login", font=("Cascadia Code", 48))
title.pack()

entry = Entry(gui, bg="black", fg="white",font=("Cascadia Code", 36))
entry.pack()

gui.mainloop()

