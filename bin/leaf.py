from tkinter import *
import pyqrcode
from tkinter.messagebox import askquestion
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
from tkinter import filedialog
import webbrowser
import os

def main():
    def generate():
        global qr_name
        qr = pyqrcode.create(data.get())
        qr_name = str(name.get()) + ".png"
        qr.png((qr_name), scale=10)
        label.config(text="Qr-Code Generated")

    def openqr():
        try:
            file = qr_name
            os.system('"%s"' %file)
            label_text = str(file) + "Opened"
            label.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to open found")

    def open_any():
        try:
            file = filedialog.askopenfilenames(initialdir='D:/', title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
            os.system('"%s"' %file)
            label_text = str(file) + "Opened"
            label.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code selected")
            
    def delqr():
        try:
            file = qr_name
            os.remove(file)
            label_text = str(file) + "Deleted"
            label.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to delete")

    def del_any():
        try:
            file = filedialog.askopenfilenames(initialdir='D:/', title="Choose a Qr-Code", filetypes=(("Image Files", "*.png"), ("Image Files", "*.jpg")))
            os.remove(file)
            label_text = str(file) + "Deleted"
            label.config(text=label_text)
        except:
            showerror("No file found", "No Qr-Code saved to delete")
        
        
    Author = "I wrote Leaf because I needed a simple QR-Generator which is light-weight, safe and private. It is also very easy to use. It is also free and open source. You can check the code at https://github.com/newtoallofthis123/leaf. Leaf is written purely in python. It is a beginner friendly project. Hope you enjoy using it."    
    About = "Leaf Qr-Code is a small project I made to learn tkinter. This is purely written in python. It is free and open source. It has no telementry and is completely safe and private. Check out some of my other projects at https://newtoallofthis123.github.io/About"
        
    def openNoobweb():
        webbrowser.open("https://newtoallofthis123.github.io/About")
        
    def showInfo():
        showinfo("About NoobNote", About)

    def aboutAuthor():
        showinfo("NoobScience", Author)
        
    def projects():
        webbrowser.open("https://github.com/newtoallofthis123")
        
    def openleafweb():
        webbrowser.open("https://newtoallofthis123.github.io/leaf")
    
    def source():
        webbrowser.open("https://github.com/newtoallofthis123/leaf")
    
    def issue():
        webbrowser.open("https://github.com/newtoallofthis123/leaf/issues")
        
    def new_win(e):
        label.config(text="New Window of Leaf opened")
        main()
    
    def quit1(e):
        gui.quit()

    gui = Tk()
    gui.geometry('500x500')
    gui.title("Leaf Qr-Code Generator")
    gui.configure(bg="black")
    gui.iconbitmap('NoobScience/Assets/Gallery/icon.ico')

    title = Label(gui, text="Leaf QrCode Generator", fg="#3FFFAB", bg="black", borderwidth=0, font=("Cascadia", 24))
    title.pack(padx=10, pady=10, ipady=6)

    data_title = Label(gui, text="Enter the data", fg="black", bg="#FB3649", borderwidth=0, font=("Cascadia", 18))
    data_title.pack(padx=10,pady=4, ipady=4)

    data = Entry(gui, fg="white", bg="#002240", borderwidth=0, font=("Cascadia", 16), width=30)
    data.pack(padx=10,pady=4, ipady=6)

    name_title = Label(gui, text="Enter Qr-Code Name", fg="black", bg="#00F7E3", borderwidth=0, font=("Cascadia", 18))
    name_title.pack(padx=10, pady=4, ipady=4)

    name = Entry(gui,fg="white", bg="#002240", borderwidth=0, font=("Cascadia", 16), width=30)
    name.pack(padx=10, pady=10, ipady=6)

    generate_btn = Button(gui, text="Generate", command=generate, font=("Cascadia", 14), fg="black", bg="#A9F700")
    generate_btn.pack(padx=10, pady=10, ipady=3)

    open_title = Label(gui, text="Press open to open the saved Qr-Code in your deflaut photoviewer", fg="#E8EDDD", bg="black", borderwidth=0, font=("Cascadia", 8))
    open_title.pack(padx=10,)

    open_btn = Button(gui, text="Open", command=openqr, font=("Cascadia", 14), fg="black", bg="#A9F700")
    open_btn.pack(padx=10, pady=10, ipady=3)

    about = Label(gui,text = "Made by NoobScience",font = ("Cascadia", 16),bg = "black",fg = "#C5FFB8",)
    about.pack(fill=X, pady=10)
    
    label = Label(gui, text="Enter data, name and click generate", font=("Cascadia", 8), fg="white", bg="black")
    label.pack()

    _menu = Menu(gui)
    gui.config(menu=_menu)
    file = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="File", menu=file)
    file.add_command(label="Generate Qr-Code", command=generate)
    file.add_command(label="New Window", command=lambda: new_win(False))
    file.add_separator()
    file.add_command(label="Exit", command=gui.quit())

    edit = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="Edit", menu=edit)
    edit.add_command(label="Open current Qr-code", command=openqr)
    edit.add_command(label="Open any Qr-code", command=open_any)
    edit.add_separator()
    edit.add_command(label="Delete Generated QR-Code", command=delqr)
    edit.add_command(label="Delete any QR-Code", command=del_any)

    about = Menu(_menu, tearoff=False)
    _menu.add_cascade(label="Help", menu=about)
    about.add_command(label="About Author", command=aboutAuthor)
    about.add_command(label="About Leaf", command=showInfo)
    about.add_command(label="NoobScience Website", command=openNoobweb)
    about.add_command(label="Leaf Website", command=openleafweb)
    about.add_command(label="View Source Code", command=source)
    about.add_command(label="Report a Issue", command=issue)    
    about.add_command(label="Some of my other projects", command=projects)

    gui.bind('<Control-n>', new_win)
    gui.bind('<Control-q>', quit1)

    gui.mainloop()

if __name__ == '__main__':
    main()
