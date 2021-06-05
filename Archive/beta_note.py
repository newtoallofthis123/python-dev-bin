from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
#import time

gui = Tk()
gui.title("NoobNote")
gui.iconbitmap('Assets/Gallery/icon.ico')
gui.geometry("600x600")
global fsVar
fsVar = False
gui.attributes('-fullscreen',fsVar)

global openFilename
openFilename = False

global selectedText
selectedText = False

def newFile():
	text.delete("1.0", END)
	gui.title('New File - NoobNote')
	status_bar.config(text="New File    ")

def openFile():
	text.delete("1.0", END)
	#gui.title('New File - NoobScience')
	#status_bar.config(text="N    ")
	file = filedialog.askopenfilename(initialdir='I:\python-dev-bin', title="Choose A File", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py")))
	if file:
		global openFilename
		openFilename = file
	name = file
	status_bar.config(text=f'{name}  opened')
	gui.title(f'{name} - NoobNote')

	file = open(file, 'r')
	content = file.read()
	text.insert(END, content)
	file.close()
	
def font():
    global finalFont
    font = Tk()
    font.geometry("300x300")
    font.title("Font Chooser")
    font.iconbitmap("Assets/Gallery/icon.ico")
    box = Listbox(font)
    box.grid(row=0, column=0)
    list = ["Arial", "Cascadia", "Helvatica", "Lucida",]
    for item in list:
        box.insert(END, item)
        #box.selection_set(ACTIVE)
    spin = Spinbox(font, from_=18, to=20)
    spin.grid(row=0, column=1)
    #while True:
    fontChoice = box.get(ANCHOR)
    sizeChoice = int(spin.get())
    finalFont = fontChoice
    #finalFont = (f'{fontChoice} {sizeChoice}')
    #time.sleep(5)
    #while True:
    text.config(font=finalFont)
    #print(finalFont)
    font.mainloop()
	
About = "NoobNote is a beginner friendly python project.It is registered under the MIT lisence. Feel free to use it however you like"
Author = "I am a learning python and wrote this to learn tkinter. Check out some of my other projects at https://github.com/newtoallofthis123. Also Check out my Website for other projects https://newtoallofthis123.github.io/About"

def saveAs():
	file = filedialog.asksaveasfilename(defaultextension=".*", initialdir='I:\python-dev-bin', title="Save file as", filetypes=(("Text Files", "*.txt"), ("Python Files", "*.py")))
	if file:
		name = file
		status_bar.config(text=f'{name}  opened')
		gui.title(f'{name} - NoobScience')

		file = open(file, 'w')
		file.write(text.get(1.0, END))
		file.close()
		status_bar.config(text='File saved')

def saveFile():
	global openFilename
	if openFilename:
		file = openFilename
		file = open(file, 'w')
		file.write(text.get(1.0, END))
		file.close()
		status_bar.config(text='File saved')
	else:
		saveAs()

def cutText(e):
	global selectedText
	if e:
		selectedText = gui.clipboard_get()
	else:
		if text.selection_get():
			selectedText = text.selection_get()
			status_bar.config(text='cut selected text')
			text.delete("sel.first", "sel.last")
			gui.clipboard_clear()
			gui.clipboard_append(selectedText)	

def copyText(e):
	global selectedText
	if e:
		selectedText = gui.clipboard_get()
	if text.selection_get():
		selectedText = text.selection_get()
		status_bar.config(text='copied selected text')
		gui.clipboard_clear()
		gui.clipboard_append(selectedText)

def pasteText(e):
	global selectedText
	if e:
		selectedText = gui.clipboard_get()
	else:
		if selectedText:
			positionCursor = text.index(INSERT)
			text.insert(positionCursor, selectedText)
			status_bar.config(text='pasted')

def boldText(e):
	boldFont = font.Font(text, text.cget("font"))
	boldFont.configure(weight="bold")

	text.tag_configure("bold", font=boldFont)
	current_tags = text.tag_names("sel.first")
	if "bold" in current_tags:
		text.tag_remove("bold",  "sel.first", "sel.last")
	else:
		text.tag_add("bold", "sel.first", "sel.last")

def italicText(e):
	italicFont = font.Font(text, text.cget("font"))
	italicFont.configure(slant="italic")

	text.tag_configure("italic", font=italicFont)
	current_tags = text.tag_names("sel.first")
	if "italic" in current_tags:
		text.tag_remove("italic",  "sel.first", "sel.last")
	else:
		text.tag_add("italic", "sel.first", "sel.last")

def underlineText(e):
	underlineFont = font.Font(text, text.cget("font"))
	underlineFont.configure(underline=True)

	text.tag_configure("underline", font=underlineFont)
	current_tags = text.tag_names("sel.first")
	if "underline" in current_tags:
		text.tag_remove("underline",  "sel.first", "sel.last")
	else:
		text.tag_add("underline", "sel.first", "sel.last")

def textColor():
	colorChoice = colorchooser.askcolor()[1]
	status_bar.config(text=f'Selected Font Color Set to: {colorChoice}')
	bgFont = font.Font(text, text.cget("font"))
	#bgFont.configure(slant="italic")

	text.tag_configure("colored", font=bgFont, foreground=colorChoice)
	current_tags = text.tag_names("sel.first")
	if "colored" in current_tags:
		text.tag_remove("colored",  "sel.first", "sel.last")
	else:
		text.tag_add("colored", "sel.first", "sel.last")

def ColorAllText():
	colorChoice = colorchooser.askcolor()[1]
	status_bar.config(text=f'All Font Color Set to: {colorChoice}')
	if colorChoice:
		text.config(fg=colorChoice)

def bgColor():
	colorChoice = colorchooser.askcolor()[1]
	status_bar.config(text=f'Background Color set to : {colorChoice}')
	if colorChoice:
		text.config(bg=colorChoice)

def showInfo():
    showinfo("About NoobNote", About)
    
def aboutAuthor():
	showinfo("NoobScience", Author)

def docOpen():
    text.delete(1.0, END)
    doc = open("README.txt")
    gui.title("NoobNote Docs")
    docContent = doc.read()
    text.insert(END, docContent)
    
def fullScreen():
    global fsVar
    if fsVar:
        gui.attributes('-fullscreen',False)
        fsVar = False
    else:
        fsVar = True
        gui.attributes('-fullscreen',True)
	
def lightTheme():
	#colorChoice = colorchooser.askcolor()[1]
	status_bar.config(text=f'Theme set to : light')
	text.config(fg = "black",bg="white", selectbackground="blue", selectforeground="white")
	
def darkTheme():
	status_bar.config(text=f'Theme set to : dark')
	text.config(fg="white",bg="black", selectbackground="yellow", selectforeground="black")

root = Frame(gui)
root.pack()


scroll_text = Scrollbar(root,)
scroll_text.pack(side=RIGHT, fill=Y)

horizontal_scroll = Scrollbar(root,orient='horizontal')
horizontal_scroll.pack(side=BOTTOM, fill=X, ipadx=10)

text = Text(root, width=100, height=22, font=("Cascadia", 16), selectbackground="green", selectforeground="black", undo=True, yscrollcommand=scroll_text.set, wrap="none", xscrollcommand=horizontal_scroll.set)
text.pack()

menu = Menu(gui)
gui.config(menu=menu)

fileMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New", command=newFile)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_command(label="SaveAs", command=saveAs)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=gui.quit)

editMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=lambda: cutText(False))
editMenu.add_command(label="Copy", command=lambda: copyText(False))
editMenu.add_command(label="Paste", command=lambda: pasteText(False))
editMenu.add_separator()
editMenu.add_command(label="Undo", command=text.edit_undo)
editMenu.add_command(label="Redo", command=text.edit_redo)

textFormatMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Format", menu=textFormatMenu)
textFormatMenu.add_command(label="Bold", command=lambda: boldText(False))
textFormatMenu.add_command(label="Italic", command=lambda: italicText(False))
textFormatMenu.add_command(label="Underline", command=lambda: underlineText(False))
textFormatMenu.add_command(label="Font", command=font)


viewMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="View", menu=viewMenu)
viewMenu.add_command(label="Toggle FullScreen", command=fullScreen)
viewMenu.add_command(label="Docs", command=docOpen)
#colorMenu.add_command(label="Selected 		Text Color", command=textColor)
viewMenu.add_separator()

colorMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Color", menu=colorMenu)
colorMenu.add_command(label="All Text Color", command=ColorAllText)
colorMenu.add_command(label="BackGround", command=bgColor)
colorMenu.add_command(label="Selected Text Color", command=textColor)
colorMenu.add_separator()
colorMenu.add_command(label="Light Theme", command=lightTheme)
colorMenu.add_command(label="Dark Theme", command=darkTheme)

aboutMenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=aboutMenu)
aboutMenu.add_command(label="About Author", command=aboutAuthor)
aboutMenu.add_command(label="About NoobNote", command=showInfo)
aboutMenu.add_separator()

status_bar = Label(gui, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=15)

scroll_text.config(command=text.yview)
horizontal_scroll.config(command=text.xview)

gui.bind('<Control-Key-x>', cutText)
gui.bind('<Control-Key-c>', copyText)
gui.bind('<Control-Key-v>', pasteText)
#gui.bind('<Control-Key-b>', boldText)
#gui.bind('<Control-Key-i>', italicText)
#gui.bind('<Control-Key-u>', underlineText)

gui.mainloop()
