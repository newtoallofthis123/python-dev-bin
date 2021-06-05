import random
import string
from tkinter import *

gui = Tk()
gui.title("Password Generator")
gui.resizable(False, False)
try:
    gui.iconbitmap("Assets/Gallery/icon.ico")
except:
    pass
gui.config(bg = "black")

length = Spinbox(gui, from_=1, to=160, width=8, bg="#B700FF", fg="black", font=("Cascadia", 8))
length.grid(row=1, column=5, padx=1)

def password():
    length_int = int(length.get())
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    whole =  lower + upper + digits + symbols

    pwd1 = random.sample(whole,length_int)

    password = "".join(pwd1)

    textfield = Text(gui, width=20, height=1,bg="#01FF7D", fg="black", font=("Cascadia", 12))
    textfield.grid(row=2, columnspan=12, padx=1, pady=1)    
    textfield.delete(0.0, END)
    textfield.insert(INSERT, password)
    

button = Button(gui, text="Generate Password", command=password, bg="#F9FF47", fg="black", font=("Cascadia", 8))
button.grid(row=1, column=7, padx=10)

gui.mainloop()

