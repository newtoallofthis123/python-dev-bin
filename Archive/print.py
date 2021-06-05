import win32api
import win32print
import traceback

from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter import font # * doesn't import font or messagebox
from tkinter import messagebox

root = Tk()
root.title("Python Printer")
root.geometry("410x310")
root.resizable(False, False)
root.tk.call('encoding', 'system', 'utf-8')

def font_size(fs):
	return font.Font(family='Helvetica', size=fs, weight='bold')

# Add a grid
mainframe = Frame(root)
#mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.grid(column=0,row=0, sticky=(N) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 10, padx = 0)

# Create a _printer variable
_printer = StringVar(root)
# Create a _color variable
_color = StringVar(root)
_filename = ""

# on change dropdown value
def sel_printer(*args):
    print( _printer.get() )
# link function to change dropdown
_printer.trace('w', sel_printer)

def sel_color(*args):
    print( _color.get() )
# link function to change dropdown
_color.trace('w', sel_color)

def UploadAction(event=None):
	global _filename
	_filename = filedialog.askopenfilename()
    #print('Selected:', _filename)
	
def PrintAction(event=None):

	PRINTER_DEFAULTS = {"DesiredAccess":win32print.PRINTER_ALL_ACCESS} 
	pHandle = win32print.OpenPrinter(_printer.get(), PRINTER_DEFAULTS)
	properties = win32print.GetPrinter(pHandle, 2)
	properties['pDevMode'].Color = 1 if str(_color.get()) == "Color" else 2
	properties['pDevMode'].Copies = 1
	win32print.SetPrinter(pHandle, 2, properties, 0)

	if not _filename:
		messagebox.showerror("Error", "No File Selected")
		return
	elif not _printer.get():
		messagebox.showerror("Error", "No Printer Selected")
		return
		
	try:
		#win32print.SetDefaultPrinter(_printer.get())
		win32api.ShellExecute(0, "print", _filename, None,  ".",  0)
		win32print.ClosePrinter(pHandle)
	except:
		pass
		messagebox.showerror("Error", "There was an error printing the file :(")

choices = [printer[2] for printer in win32print.EnumPrinters(2)]
_printer.set(win32print.GetDefaultPrinter()) # set the default option

popupMenu = OptionMenu(mainframe, _printer, *choices)
popupMenu['font'] = font_size(12)
Label(mainframe, text="SELECT PRINTER").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# Dictionary with options
choices = ["COLOR", "MONOCHROME"]
_color.set("COLOR") # set the default option

popupMenu2 = OptionMenu(mainframe, _color, *choices)
popupMenu2['font'] = font_size(12)
Label(mainframe, text="COLOR MODE").grid(row = 3, column = 1)
popupMenu2.grid(row = 4, column =1)

Label(mainframe, text="SELECT FILE").grid(row = 5, column = 1)
button = Button(mainframe, text=u"\uD83D\uDCC1" ' BROWSE', command=UploadAction)
button['font'] = font_size(12)
button.grid(row = 6, column =1)


_copies = IntVar()
_copies.set(1)

def copies_increase(event=None):
    _copies.set(_copies.get() + 1)
	
def copies_decrease(event=None):
	_copies.set(_copies.get() - 1)
	if _copies.get() < 1 :
		_copies.set(1)

Label(mainframe, textvariable=_copies).grid(columnspan=2)
button_frame = Frame(mainframe)
button_frame.grid(columnspan=2)


dec_button = Button(button_frame, text=u"\u2212", command=copies_decrease, fg="dark green", bg = "white", height=1, width=3 )
dec_button['font'] = font_size(10)

inc_button = Button(button_frame, text=u"\uFF0B", command=copies_increase, fg="dark green", bg = "white", height=1, width=3 )
inc_button['font'] = font_size(10)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

dec_button.grid(row=0, column=0, sticky=W+E)
inc_button.grid(row=0, column=1, sticky=W+E)

Label(mainframe).grid(row = 10, column = 1)
p_button = Button(mainframe, text=u'\uD83D\uDDB6' + " PRINT", command=PrintAction, fg="dark green", bg = "white")
p_button['font'] = font_size(18)
p_button.grid(row = 11, column =1)

root.mainloop()
