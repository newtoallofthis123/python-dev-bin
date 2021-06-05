from tkinter import *
from tkinter.font import Font

gui = Tk()
gui.title("ToDo App")
gui.iconbitmap("Assets/Gallery/icon.ico")
gui.geometry('600x600')

font = Font(family="Cascadia",size=24,weight='bold',)

def end():
	to_do_list.delete(ANCHOR)

def add():
	pass

def done():
	pass

def pend():
	pass

root = Frame(gui)
root.pack(pady=12)

to_do_list=Listbox(root, font=font, width=30, height=5, bg="SystemButtonFace", bd=0, fg="black", highlightthickness=0, selectbackground="grey", activestyle="none" )

to_do_list.pack(side=LEFT, fill=BOTH)

todo = ['Hello', 'Hi', 'How are you']

for do in todo:
	to_do_list.insert(END, do)

scroll_bar = Scrollbar(root)
scroll_bar.pack(side=RIGHT, fill=BOTH)

to_do_list.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=to_do_list.yview)

entry_do = Entry(gui, font=("Cascadia", 16))
entry_do.pack(pady=10)

btn_frame = Frame(gui)
btn_frame.pack()

btn_del = Button(btn_frame, text="Delete ToDo", command="end")
btn_add = Button(btn_frame, text="Add a ToDo", command="add")
btn_done = Button(btn_frame, text="Mark Done", command="done")
btn_pend = Button(btn_frame, text="Mark Pending", command="pend")

btn_add.grid(row=0, column=0)
btn_del.grid(row=0, column=1)
btn_done.grid(row=0, column=2)
btn_pend.grid(row=0, column=3)

#btn_add.pack(padx=10)
#btn_del.pack(padx=10)
#btn_pend.pack(padx=10)
#btn_done.pack(padx=10)




gui.mainloop()