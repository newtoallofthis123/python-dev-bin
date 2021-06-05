import random
from tkinter import *
from tkinter import ttk
import time

gui = Tk()
gui.title("Rock Paper Scissor")
gui.geometry("400x400")
gui.config(bg="#002240")

#choice = StringVar(gui)
#choice.set("Rock Paper or Scissor")

def user_op(e):
    if op.get() == "Rock":
        user = 1
    if op.get() == "Paper":
        user = 2
    if op.get() == "Scissor":
        user = 3
    user_text = "You Choose " + op.get() + ""
    user_label = Label(gui, text=user_text, fg="black", bg="#FFEC47", font=("Cascadia", 16)).pack()
    label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()
    #label = Label(gui, text="Computer is procressing...", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
    comp_op = int(random.randint(1, 3))
    if comp_op == 1:
        com = "Rock"
    if comp_op == 2:
        com = "Paper"
    if comp_op == 3:
        com = "Scissor"
    comp_text = "The Computer choose " + com + ""
    comp_label = Label(gui, text=comp_text, fg="black", bg="#75EBFF", font=("Cascadia", 16)).pack()
    label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()
    #label = Label(gui, text="Processing Options...", fg="white", bg="#002240", font=("Cascadia", 14)).pack()

    if user == comp_op:
        user_label = Label(gui, text="It's a Tie, exiting application, try again", fg="black", bg="#23FF8F", font=("Cascadia", 12)).pack()
        label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
    if user == 1 and comp_op == 3 or user == 3 and comp_op == 2 or user == 2 and comp_op == 1:
        user_label = Label(gui, text="You Won.Play Again", fg="black", bg="#23FF8F", font=("Cascadia", 16)).pack()
        label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
    if user == 3 and comp_op == 1 or user == 2 and comp_op == 3 or user == 1 and comp_op == 2:
        user_label = Label(gui, text="You Lost. Play Again", fg="black", bg="#23FF8F", font=("Cascadia", 16)).pack()
        label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()

op_list = ["Rock", "Paper", "Scissor",]

label = Label(gui, text="Rock Paper Scissor", fg="white", bg="#002240", font=("Cascadia", 18)).pack()

#label = Label(gui, text="choose an option  below", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
op = ttk.Combobox(gui, value=op_list, font=("Cascadia", 16))
op.pack()
#op.current(3)
op.bind("<<ComboboxSelected>>", user_op)

def processor():
    return

gui.mainloop()
