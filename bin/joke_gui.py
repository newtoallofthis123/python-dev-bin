from tkinter import *
import pyjokes
from tkinter.messagebox import showerror

gui = Tk()
gui.title("Joke")
gui.geometry('800x150')
gui.config(bg="#002240")
gui.resizable(True, False)

j = pyjokes.get_joke()
joke = StringVar(gui, value = j)

def main():
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(j)
        engine.runAndWait()
    except:
        showerror("pyttsx3 not installed", "Install pyttsx3 with pip install pyttsx3 to run the command")

label = Label(gui, text = "Joke",font=("Cascadia", 24), fg="white", bg="#002240").pack()
entry = Entry(gui, textvariable = joke, width=120, font=("Cascadia", 12), fg="white", bg="#002240").pack(fill=X)
button = Button(gui, text="Read out loud", font=("Cascadia", 18), fg="white", bg="#002240", borderwidth=0, command=main).pack()
label = Label(gui, text = "By NoobScience",font=("Cascadia", 16), fg="white", bg="#002240").pack()

gui.mainloop()
