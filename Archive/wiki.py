#! /usr/bin/env python3
import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

gui = Tk() #objek
gui.title('WIKIPEDIA SEARCH')
gui.geometry('200x70') #function

#function
def wiki() :
    search = entry.get()
    Hasil = wikipedia.summary(search)
    showinfo(search,Hasil)

label = Label(gui,text="Wikipedia Search :")
label.grid(row=0,column=0)

entry = Entry(gui)
entry.grid(row=1,column=0)

button = Button(gui,text="Search",command=wiki)
button.grid(row=1,column=1,padx=10)

gui.mainloop()

    

