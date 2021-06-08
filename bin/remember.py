# importing the necessary modules, I think I will be needing tkinter nad sqlite3
from tkinter import *
import sqlite3
from time import strftime, gmtime

gui = Tk()
gui.iconbitmap('Assets/Gallery/icon.ico')
gui.title('Remember, A Simple To-Do App')
gui.geometry('500x500')

root = Frame(gui)
root.grid()

scroll_bar_x = Scrollbar(root,)
scroll_bar_x.pack(side=RIGHT, fill=BOTH)

box = Listbox(root, font=("Cascadia", 16), fg="black", bg="white", selectborder=0, borderwidth=0, width=30, height=10, highlightthickness=0, activestyle="none",)
box.pack()
box.config(yscrollcommand=scroll_bar_x.set)

# Connecting to the database
conn = sqlite3.connect('remember.db')
c = conn.cursor()
c.execute('SELECT * FROM todo')
x = c.fetchall()
for item in x:
    text_to_insert = item[0] + "                        " + item[1] + "\n"
    box.insert(END, text_to_insert)

try:
     c.execute("""CREATE TABLE todo(
     name text,
     time text
     )""")
except:
    pass

def add():
    time_ = strftime("%H:%M:%S %p")
    add_todo = entry.get()
    add_command = [(add_todo, time_)]
    c.executemany("INSERT INTO todo VALUES (?,?)", add_command)
    conn.commit()
    c.execute('SELECT * FROM todo')


def del_():
    hilo = box.get(ANCHOR)
    c.execute("DELETE from todo WHERE name=y")

def cross():
    z = box.get(ANCHOR)


def uncross():
    pass

add_btn = Button(gui, text="Add", command=add)
add_btn.grid()

del_btn = Button(gui, command=del_)
del_btn.grid()

cross_btn = Button(gui, command=cross)
cross_btn.grid()

uncross_btn = Button(gui, command=uncross)
uncross_btn.grid()

entry = Entry(gui)
entry.grid()

gui.mainloop()