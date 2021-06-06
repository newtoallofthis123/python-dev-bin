from tkinter import *

gui = Tk()
gui.title("Branch")
gui.iconbitmap("Assets/Gallery/icon.ico")
gui.geometry("360x60")
gui.configure(bg="black")

def wikid():
    pass

title = Label(gui, text="All my python projects", fg="white", bg="black", font=("Cascadia", 24))
title.pack()

app_menu = Menu(gui)
gui.configure(menu=app_menu)

applicationMenu = Menu(app_menu, tearoff=False)
app_menu.add_cascade(label="Cli-Tools", menu=applicationMenu)
app_menu.add_command(label="Wikid", command=wikid)
gui.mainloop()