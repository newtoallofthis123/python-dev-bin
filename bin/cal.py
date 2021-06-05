#Calculator
from tkinter import *
w=Tk()
w.geometry("400x400")
w.title("Calculator")
w.configure(bg="black")

#Functions(Keypad)
def calc1():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn1["text"]
    txt1.insert(0, b1)

def calc2():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn2["text"]
    txt1.insert(0, b1)
def calc3():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn3["text"]
    txt1.insert(0, b1)
def calc4():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn4["text"]
    txt1.insert(0, b1)
def calc5():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn5["text"]
    txt1.insert(0, b1)
def calc6():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn6["text"]
    txt1.insert(0, b1)
def calc7():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn7["text"]
    txt1.insert(0, b1)
def calc8():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn8["text"]
    txt1.insert(0, b1)
def calc9():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn9["text"]
    txt1.insert(0, b1)
def calc0():
    b = txt1.get()
    txt1.delete(0, END)
    b1 = b + btn0["text"]
    txt1.insert(0, b1)

#Functions(operators)

x = 0
def add():
    global x
    add.b = (eval(txt1.get()))
    txt1.delete(0, END)
    x = x + 1


def subtract():
    global x
    subtract.b = (eval(txt1.get()))
    txt1.delete(0, END)
    x = x + 2

def get():
    b = txt1.get()

def equals():
    global x
    if x == 1:
        c = (eval(txt1.get())) + add.b
        cls()
        txt1.insert(0, c)

    elif x == 2:
        c = subtract.b - (eval(txt1.get()))
        cls()
        txt1.insert(0, c)

    elif x == 3:
        c = multiply.b*(eval(txt1.get()))
        cls()
        txt1.insert(0, c)
    elif x == 4:
        c = divide.b/(eval(txt1.get()))
        cls()
        txt1.insert(0,c)

def cls():
    global x
    x = 0
    txt1.delete(0, END)

def multiply():
    global x
    multiply.b = (eval(txt1.get()))
    txt1.delete(0, END)
    x = x + 3

def divide():
    global x
    divide.b = (eval(txt1.get()))
    txt1.delete(0, END)
    x = x + 4

#Labels

lbl1 = Label(w, text="Calculator", font=("Cascadia", 36), fg="white", bg="black")

#Entryboxes
txt1 = Entry(w, width=80, font=("Cascadia", 24), bg="#002240", fg="white")

#Buttons

btn1 = Button(w, text="1", font=("Cascadia", 24), command=calc1, bg="grey")
btn2 = Button(w, text="2", font=("Cascadia", 24), command=calc2, bg="grey")
btn3 = Button(w, text="3", font=("Cascadia", 24), command=calc3, bg="grey")
btn4 = Button(w, text="4", font=("Cascadia", 24), command=calc4, bg="grey")
btn5 = Button(w, text="5", font=("Cascadia", 24), command=calc5, bg="grey")
btn6 = Button(w, text="6", font=("Cascadia", 24), command=calc6, bg="grey")
btn7 = Button(w, text="7", font=("Cascadia", 24), command=calc7, bg="grey")
btn8 = Button(w, text="8", font=("Cascadia", 24), command=calc8, bg="grey")
btn9 = Button(w, text="9", font=("Cascadia", 24), command=calc9, bg="grey")
btn0 = Button(w, text="0", font=("Cascadia", 24), command=calc0, bg="grey")

btn_addition = Button(w, text="+", font=("Cascadia", 28), command=add, bg="grey")
btn_equals = Button(w, text="=", font=("Cascadia", 26,), command=equals, bg="grey")
btn_clear = Button(w, text="Clear", font=("Cascadia", 26,), command=cls, bg="grey")
btn_subtract = Button(w, text="-", font=("Cascadia", 28), command=subtract, bg="grey")
btn_multiplication = Button(w, text="x", font=("Cascadia", 28), command=multiply, bg="grey")
btn_division = Button(w, text="÷", font=("Cascadia", 28), command=divide, bg="grey")

#Placements(Labels)

lbl1.place(x=110,y=0)

#Placements(entrybox)
 
txt1.place(x=0, y=50, height=35,)

#Placements(Buttons)
btn1.place(x=60, y=100)
btn2.place(x=110, y=100)
btn3.place(x=160, y=100)
btn4.place(x=60, y=170)
btn5.place(x=110, y=170)        
btn6.place(x=160, y=170)
btn7.place(x=60, y=240)
btn8.place(x=110, y=240)
btn9.place(x=160, y=240)
btn0.place(x=110, y=310)

btn_addition.place(x=230, y=100)
btn_equals.place(x=350, y=280)
btn_clear.place(x=230, y=280)
btn_subtract.place(x=230, y=180)
btn_multiplication.place(x=290, y=100)
btn_division.place(x=290, y=180)

w.mainloop()
