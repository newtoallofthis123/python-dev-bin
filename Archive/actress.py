from tkinter import *
from PIL import ImageTk, Image
import random

actress = dict(
    img1 = "Assets/noobscience.png"
)
actress_name, actress_conv = random.choice(list(actress.items()))
print(actress_name + ": ")
print(actress_conv)
#actress_actual = str(actress_conv)

gui = Tk()
gui.configure(bg='black')
#gui.geometry('300x300')
gui.title("Actresses")

actress = StringVar
#actress = StringVar

title_label = Label(gui, text = "Actress: ", font=("Cascadia", 24)).pack()
img = Image.open(actress_conv)
imgtk = ImageTk.PhotoImage(img)
actress_name_gui = Entry(gui, bg="black", font=("Cascadia", 24),fg="white")
actress_name_gui.insert(END, actress_name)
actress_name_gui.pack(fill=X)
#entry = Entry(gui, textvariable=actress, width=50).pack()
canvas= Canvas(gui, width= 480, height= 320, bg="black")
canvas.pack()
canvas.create_image(10,10,anchor=NW,image=imgtk)
#button = Button(gui, text="Get", command=imgview).pack()
gui.mainloop()

