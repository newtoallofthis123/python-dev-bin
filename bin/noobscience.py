import time
import webbrowser
from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter.filedialog import askdirectory
from turtle import *

'''            Noob Science   '''

class NSnote:

    gui = Tk()
    gui.configure(bg="black")
    
    Width = 300
    Height = 300
    #TextArea = Text(gui)
    MenuBar = Menu(gui)
    Applications = Menu(MenuBar, tearoff=0, bg="white", fg="black")
    Fun = Menu(MenuBar, tearoff=0, bg="white", fg="black")
    Music = Menu(MenuBar, tearoff=0, bg="white", fg="black")
    Cli_Tools = Menu(MenuBar, tearoff=0, bg="white", fg="black")
    Web = Menu(MenuBar, tearoff=0, bg="white", fg="black")
    try:
        background = PhotoImage(file="Assets/noobscience.png")
        canvas = Canvas(gui, bg="black", width=800, height=480)
        canvas.pack(fill="both", expand=True, anchor="nw")
        canvas.create_image(380,245, image = background)
    except:
            pass

    #ScrollBar = Scrollbar(TextArea)	
    #file = None

    def __init__(self,**kwargs):

            try:
                self.gui.wm_iconbitmap("Assets/Gallery/icon.ico")
            except:
                    pass
            try:
                from PIL import Image,ImageTk
                bg = ImageTk.PhotoImage(file="Assets/noobscience.png")
                def resizer(e):
                    global bg1, resized_bg, new_bg
                    bg1 = Image.open("Assets/noobscience.png")
                    resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
                    bg = ImageTk.PhotoImage(file=resized_bg)
            except:
                    pass

            try:
                self.gui.resizable(False,False)
            except:
                    pass
            # Win Size
            try:
                self.Width = kwargs['width']
            except KeyError:
                pass

            try:
                self.Height = kwargs['height']
            except KeyError:
                    pass
                
            self.gui.title("NoobScience")

            screenWidth = self.gui.winfo_screenwidth()
            screenHeight = self.gui.winfo_screenheight()
    
            # For left-alling
            left = (screenWidth / 2) - (self.Width / 2)
            
            # For right-allign
            top = (screenHeight / 2) - (self.Height /2)
            
            # For top and bottom
            self.gui.geometry('%dx%d+%d+%d' % (self.Width,self.Height,left, top))
            self.gui.grid_rowconfigure(0, weight=1)
            self.gui.grid_columnconfigure(0, weight=1)

            # Add controls (widget)
            #self.TextArea.grid(sticky = N + E + S + W)

            # Controls
            self.Applications.add_command(label="Wiki",command=self.wiki)	
            self.Applications.add_command(label="Calendar",command=self.calendar)
            self.Applications.add_command(label="Url Shorterner",command=self.shorturl)
            self.Applications.add_command(label="Song Player",command=self.song)
            self.Applications.add_command(label="Clock",command=self.clock)
            self.Applications.add_command(label="Analog Clock",command=self.analog_clock)
            self.Applications.add_command(label="Qr Code Generator",command=self.qr)
            self.Applications.add_command(label="Note",command=self.note)
            self.Applications.add_command(label="Calculator",command=self.cal)
            self.Applications.add_command(label="Password Generator",command=self.pwdgen)
            
            self.Applications.add_separator()										
            self.Applications.add_command(label="Exit",command=self.quit1)
            self.MenuBar.add_cascade(label="Applications",menu=self.Applications)
            
            self.Fun.add_command(label="Tech Joke",command=self.joke)			
            self.Fun.add_command(label="RockPaperScissor",command=self.rps)		
            self.Fun.add_command(label="Snakes",command=self.snakes)
            self.Fun.add_command(label="Ping Pong",command=self.pong)
            self.Fun.add_command(label="Tic Tac Toe",command=self.tictactoe)
            self.Fun.add_command(label="Flappy Bird",command=self.flappy_bird)
            self.MenuBar.add_cascade(label="Fun",menu=self.Fun)

            self.Music.add_command(label="Play Relaxing Music",command=self.play)			
            self.Music.add_command(label="Pause",command=self.pause)		
            self.Music.add_command(label="Stop",command=self.stop)		
            self.MenuBar.add_cascade(label="Music",menu=self.Music)

            '''self.Web.add_command(label="Source",command=self.source)			
            self.Web.add_command(label="Projects",command=self.projects)		
            self.Web.add_command(label="Website",command=self.website)
            self.Web.add_command(label="Github",command=self.github)
            self.Web.add_command(label="Youtube",command=self.youtube)
            self.Web.add_command(label="Blog",command=self.blog)
            self.MenuBar.add_cascade(label="Resources",menu=self.Web)'''
    
            self.Cli_Tools.add_command(label="Alaram",command=self.alarm)
            self.Cli_Tools.add_command(label="Wikid",command=self.wikid)
            self.Cli_Tools.add_command(label="noob",command=self.noob)
            #self.Cli_Tools.add_command(label="Password Generator",command=self.pwd)
            self.Cli_Tools.add_command(label="Google Search",command=self.google)
            self.MenuBar.add_cascade(label="Cli-Tools", menu=self.Cli_Tools)
            self.Cli_Tools.add_command(label="Open Links",command=self.links)
            self.Cli_Tools.add_command(label="Youtube Downloader",command=self.yt_dl)

            self.gui.config(menu=self.MenuBar)

            #self.ScrollBar.pack(side=RIGHT,fill=Y)					
            
            # Scrollbar will adjust automatically according to the content		
            #self.ScrollBar.config(command=self.TextArea.yview)	
            #self.TextArea.config(yscrollcommand=self.ScrollBar.set)
            
    def wiki(self):
        import wikipedia
        from tkinter.messagebox import showinfo
        wiki = Tk() 
        wiki.title('WIKIPEDIA SEARCH')
        wiki.iconbitmap("Assets/Gallery/icon.ico")
        wiki.geometry('200x70')

        def wikid() :
            search = entry.get()
            wikisum = wikipedia.summary(search)
            showinfo(search,wikisum)

        label = Label(wiki,text="Wikipedia Search :")
        label.grid(row=0,column=0)

        entry = Entry(wiki)
        entry.grid(row=1,column=0)

        button = Button(wiki,text="Search",command=wikid)
        button.grid(row=1,column=1,padx=10)

        wiki.mainloop()
        wiki.quit()

    def calendar(self):
        import calendar
        from datetime import datetime
        gui = Tk()
        gui.geometry("400x300")
        gui.title("NS-Calendar")
        gui.iconbitmap("Assets/Gallery/icon.ico")
        gui.configure(bg="#4A3B52")
        gui.resizable(False,False)

        def cal():
            month_int = int(month.get())
            year_int = int(year.get())
            cal = calendar.month(year_int, month_int)
            textfield.delete(0.0, END)
            textfield.insert(INSERT, cal)

        label1 = Label(gui, text="Month:", bg="#C5FFB8", font=("Arial", 18),)
        label1.grid(row=0, column=5)

        label2 = Label(gui, text="Year:", bg="#C5FFB8", font=("Arial", 18),)
        label2.grid(row=0, column=6)

        month = Spinbox(gui, from_=1, to=12, width=8, bg="#FA8574")
        month.grid(row=1, column=5, padx=5)

        year = Spinbox(gui, from_=2000, to=2100, width=10, bg="#FA8574")
        year.grid(row=1, column=6, padx=10)

        button = Button(gui, text="Get The Calendar", command=cal, fg="black", bg="#FDA600")
        button.grid(row=1, column=7, padx=10)

        textfield = Text(gui, width=20, height=10, fg="black", bg="#FFC400")
        textfield.grid(row=2, columnspan=12, padx=5, pady=5)
        
        gui.mainloop()

    def shorturl(self):
        import pyperclip
        import pyshorteners
        import tkinter as tk

        def processor():
            shorten = pyshorteners.Shortener()
            shortening = shorten.gitio.short(url.get())

            short_url.set(shortening)

        def copy():
            pyperclip.copy( short_url.get())

        if __name__=="__main__":
            gui = tk.Tk()
            gui.title("IJ_URL")
            gui.geometry("600x600")
            gui.configure(bg="black")
            gui.iconbitmap("Assets/Gallery/icon.ico")

            url = StringVar()
            short_url= StringVar()

            label = tk.Label(
                gui,
                text = "IJ URL Shortner",
                font=("Arial", 36),
                bg="black",
                fg="red",
                ).pack(fill=tk.X, pady=2)
     
            entry = tk.Entry(
               
                gui,
                textvariable=url, width =100).pack(pady=5)
         
            button = tk.Button(
                gui,
                text = "Give URL",
                font=("Arial", 18),
                bg="yellow",
                fg="black",
                command =processor,).pack(pady=2)

            label = tk.Label(
                gui,
                text = "Shorten URL using git.io",
                font=("Arial", 36),
                bg="black",
                fg="red",
                ).pack(fill=tk.X, pady=2)

            entry = tk.Entry(
                gui,
                textvariable=short_url, width =100).pack(pady=5)

            button = tk.Button(
                gui,
                text = "Copy URL",
                font=("Arial", 18),
                bg="yellow",
                fg="black",
                command =copy,).pack(pady=2)
            
            gui.mainloop()
    
    def song(self):
        import os
        from tkinter.filedialog import askdirectory

        # pygame is used in this program, you can install it by using pip install pygame
        import pygame

        # We will be using mtagrn.id3 also
        from mutagen.id3 import ID3

        # We will be using tkinter to build the gui
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        import tkinter.messagebox

        # We will use the web Browser to open the web browser
        import webbrowser

        # Building the GUI
        gui = Tk()
        gui.minsize(546,580)
        gui.configure(bg="#002240")
        gui.title("NSPlayer")
        gui.geometry('500x500')
        gui.iconbitmap("Assets/Gallery/icon.ico")
        gui.resizable(False,False)
        
        listofsongs = []
        realnames = []

        # Defining a variable to hold song name
        v = StringVar()
        songlabel = Label(gui,textvariable=v,width=72, bg="#002240", fg="white", font=('Cascadia Code', 14))

        # Song Indexing
        index = 0

        # Function to choose directory
        def directorychooser():

            directory = askdirectory()
            os.chdir(directory)

        # Types of files to import, change after comment to add more type of audio files
            for files in os.listdir(directory):
                if files.endswith(".mp3"):

        # Files
                    realdir = os.path.realpath(files)
                    audio = ID3(realdir)
                    realnames.append(audio['TIT2'].text[0])


                    listofsongs.append(files)

        # Intiating pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load(listofsongs[0])
            #pygame.mixer.music.play()

        # Calling upon the directorychooser function
        directorychooser()

        # To update song labels
        def updatelabel():
            global index
            global songname
            v.set(realnames[index])
            #return songname


        # To get Next Song
        def nextsong(event):
            global index
            index += 1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            updatelabel()

        # To get Previous Song
        def prevsong(event):
            global index
            index -= 1
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            updatelabel()

        # To stop the song
        def stopsong(event):
            pygame.mixer.music.stop()
            v.set("")
            #return songname

        # To Play Song in order
        def playsong(event):
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.play()
            v.set("")
            updatelabel()

        # To pause Song
        def pausesong(event):
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.pause()
            v.set("")
            updatelabel()

        # To unpause Song
        def unpausesong(event):
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.unpause()
            v.set("")
            updatelabel()

        # To rewind the Song
        def rewindsong(event):
            pygame.mixer.music.load(listofsongs[index])
            pygame.mixer.music.rewind()
            v.set("")
            updatelabel()

        # To open a pop up window containing info
        def NS_info(event):
            tkinter.messagebox.showinfo('About NoobScience', NS_text)
            webbrowser.open('https://newtoallofthis123.github.io/About')


        # To ask if the user wants to visit the NSPlayer Website
        def NS_title():
           result = tkinter.messagebox.askquestion('Fork', 'Do you want to go the NSPlayer Website?')
           if result=='yes':
               webbrowser.open('https://newtoallofthis123.github.io/NSPlayer')
           else:
                print("Okay")

                
        # The Text Pop up box info
        NS_text = "This Project is built by NoobScience using python and pygame. This is a beginner-friendly project and you can use this to learn pygame as well. This project is registered under MIT lisence (copy right NoobScience 2021), which makes it open-source. You are free to use it however you wish. Check out the code at my repo: https://github.com/newtoallofthis123 , Any issues, be sure to tell me at https://github.com/newtoallofthis123/issues , Check out the website at https://newtoallofthis123.github.io/NSPlayer, To troubleshoot any problems, check out the documentation at the website. Be sure to get pygame from 'pip install pygame'"

            #return songname

        # The Title Button
        titleButton = Button(gui,text='NSPlayer', bg="#FFE600", fg="#002240", font=("Cascadia Code", 20), command = NS_title)
        titleButton.pack(padx=3, pady=12)

        # The song list
        listbox = Listbox(gui, bg="#002240", fg="white", width="76", font=("Cascadia Code", 12),)
        listbox.pack(padx=5, pady=10)

        #listofsongs.reverse()
        realnames.reverse()

        for items in realnames:
            listbox.insert(0,items)

        realnames.reverse()
        #listofsongs.reverse()

        # Play Button
        playbutton = Button(gui,text='|> Play Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        playbutton.pack()
        playbutton.place(x=34, y=330)

        # Pause Button
        pausebutton = Button(gui,text='|: Pause Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        pausebutton.pack()
        pausebutton.place(x=34, y=380)

        # Unpause Button
        unpausebutton = Button(gui,text=':: Unpause Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        unpausebutton.pack()
        unpausebutton.place(x=300, y=380)

        # Rewind Button
        rewindbutton = Button(gui,text='0 Rewind Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        rewindbutton.pack()
        rewindbutton.place(x=34, y=480)

        # Next Song Button
        nextbutton = Button(gui,text = '--> Next Song', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        nextbutton.pack()
        nextbutton.place(x=300, y=430)

        # Previous Song Button
        previousbutton = Button(gui,text = '<-- Previous Song', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        previousbutton.pack()
        previousbutton.place(x=34, y=430)

        # Stop Song Button
        stopbutton = Button(gui,text='|| Stop Music', font=("Cascadia Code", 12), width=20, bg="#00FFC0")
        stopbutton.pack()
        stopbutton.place(x=300, y=330)

        # Rewind Button
        version = Label(gui,text='v.0.1', font=("Cascadia Code", 8), width=20, bg="#00FFC0")
        version.pack()
        version.place(x=410, y=68)

        # Info button
        infobutton = Button(gui,text = "By NoobScience", font=("Cascadia Code", 12), width=20, bg="#00FFC0", fg="#002240")
        infobutton.pack(padx=1, pady=1)
        infobutton.place(x=300, y=480)

        # Now Playing text
        label = Label(gui, text = "------Now Playing------", font=("Cascadia Code", 12), width=25)
        label.pack(pady=10)
        label.place(x=144, y=524)

        # Defining Button Commands
        playbutton.bind("<Button-1>",playsong)
        nextbutton.bind("<Button-1>",nextsong)
        previousbutton.bind("<Button-1>",prevsong)
        stopbutton.bind("<Button-1>",stopsong)
        infobutton.bind("<Button-1>",NS_info)
        pausebutton.bind("<Button-1>",pausesong)
        unpausebutton.bind("<Button-1>",unpausesong)

        # Song playing Name
        songlabel.pack()
        songlabel.place(x=-124, y=550)
        gui.mainloop()
        
    def clock(self):
        from time import strftime
        gui = Tk()

        gui.title('Digital clock Widget by NoobScience')
        gui.configure(bg='#002240')
        gui.resizable(False,False)
        gui.iconbitmap("Assets/Gallery/icon.ico")
        #photo = PhotoImage(file = "/clock.png")
        #gui.iconphoto(False, photo)

        def clocktime():
            tick = strftime('%H:%M:%S %p')

            label.config(text =tick)

            label.after(1000, clocktime)

        label = Label(gui, font =('sans', 80), background = '#002240', foreground = '#FFC900')
        label.pack(anchor= 'center')

        clocktime()
        mainloop
        
    def test(self):
        return
    
    def analog_clock(self):
        from datetime import datetime

        def jump(distanz, winkel=0):
            penup()
            right(winkel)
            forward(distanz)
            left(winkel)
            pendown()

        def hand(laenge, spitze):
            fd(laenge*1.15)
            rt(90)
            fd(spitze/2.0)
            lt(120)
            fd(spitze)
            lt(120)
            fd(spitze)
            lt(120)
            fd(spitze/2.0)

        def make_hand_shape(name, laenge, spitze):
            reset()
            jump(-laenge*0.15)
            begin_poly()
            hand(laenge, spitze)
            end_poly()
            hand_form = get_poly()
            register_shape(name, hand_form)

        def clockface(radius):
            reset()
            pensize(7)
            for i in range(60):
                jump(radius)
                if i % 5 == 0:
                    fd(25)
                    jump(-radius-25)
                else:
                    dot(3)
                    jump(-radius)
                rt(6)

        def setup():
            global second_hand, minute_hand, hour_hand, writer
            mode("logo")
            make_hand_shape("second_hand", 125, 25)
            make_hand_shape("minute_hand",  130, 25)
            make_hand_shape("hour_hand", 90, 25)
            clockface(160)
            second_hand = Turtle()
            second_hand.shape("second_hand")
            second_hand.color("gray20", "gray80")
            minute_hand = Turtle()
            minute_hand.shape("minute_hand")
            minute_hand.color("blue1", "red1")
            hour_hand = Turtle()
            hour_hand.shape("hour_hand")
            hour_hand.color("blue3", "red3")
            for hand in second_hand, minute_hand, hour_hand:
                hand.resizemode("user")
                hand.shapesize(1, 1, 3)
                hand.speed(0)
            ht()
            writer = Turtle()
            #writer.mode("logo")
            writer.ht()
            writer.pu()
            writer.bk(85)

        def wochentag(t):
            wochentag = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
            return wochentag[t.weekday()]

        def datum(z):
            monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                    "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
            j = z.year
            m = monat[z.month - 1]
            t = z.day
            return "%s %d %d" % (m, t, j)

        def tick():
            t = datetime.today()
            sekunde = t.second + t.microsecond*0.000001
            minute = t.minute + sekunde/60.0
            stunde = t.hour + minute/60.0
            try:
                tracer(False)  # Terminator can occur here
                writer.clear()
                writer.home()
                writer.forward(65)
                writer.write(wochentag(t),
                            align="center", font=("Courier", 14, "bold"))
                writer.back(150)
                writer.write(datum(t),
                            align="center", font=("Courier", 14, "bold"))
                writer.forward(85)
                tracer(True)
                second_hand.setheading(6*sekunde)  # or here
                minute_hand.setheading(6*minute)
                hour_hand.setheading(30*stunde)
                tracer(True)
                ontimer(tick, 100)
            except Terminator:
                pass  # turtledemo user pressed STOP

        def main():
            tracer(False)
            setup()
            tracer(True)
            tick()
            return "EVENTLOOP"

        if __name__ == "__main__":
            mode("logo")
            msg = main()
            print(msg)
            mainloop()

    def qr(self):
        import pyqrcode
        import tkinter as tk
        #from tkinter import *
        from PIL import Image, ImageTk
        from tkinter import filedialog
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        import os

        def qr_processor():
            image = pyqrcode.create(data1.get())
            img_name = str(imgname.get()) + ".png"
            image.png((img_name), scale=10)

        def open_code():
            try:
               file1= filedialog.askopenfilename(initialdir="/", title="Select Png files Only", )
               img1 = ImageTk.PhotoImage(Image.open(file))
               my_label = Label(image=img1).pack()
               os.system('"%s"' %file)
            except:
                tkinter.showerror("No file found", "Create the file first.")

        def open_img():
            try:
                name = str(imgname.get()) + ".png"
                os.system('"%s"' %name)
            except:
                tkinter.showerror("No file found", "Create the file first.")

        if __name__=="__main__":
            gui = tk.Tk(className = "NS QR")
            gui.title("NS QR Code Generator")
            gui.iconbitmap("Assets/Gallery/icon.ico")
            gui.geometry("600x600")
            gui.configure(bg="black")

            data1 = StringVar()
            imgname = StringVar()

            label = tk.Label(
                gui,
                text = "Qr-Code Generator",
                font = ("Arial", 28),
                bg = "#40FAE4",
                fg = "black",
                ).pack(pady=2)
            label = tk.Label(
                gui,
                text = "",
                font = ("Arial", 12),
                bg = "black",
                fg = "black",
                ).pack(pady=2)
            label = tk.Label(
                gui,
                text = "Enter Data",
                font = ("Arial", 18),
                bg = "yellow",
                fg = "black",
                ).pack(pady=2)
            entry = tk.Entry(
                gui,
                font=("Cascadia", 16),
                bg="#002240",
                fg="white",
                textvariable=data1, width =30).pack()
            label = tk.Label(
                gui,
                text = "QR-Code Name",
                font=("Arial", 18),
                bg="#FA4062",
                fg="black",
                ).pack(pady=2)
            entry = tk.Entry(
                gui,
                font=("Cascadia", 16),
                bg="#002240",
                fg="white",
                textvariable=imgname, width =30,
                ).pack()
            label = tk.Label(
                gui,
                text = "",
                font = ("Arial", 16),
                bg = "black",
                fg = "black",
                ).pack(pady=2)
            button = tk.Button(
                gui,
                text = "Generate QR-Code",
                font=("Arial", 18),
                bg="#23FD71",
                fg="black",
                command =qr_processor,).pack(pady=2)
            label = tk.Label(
                gui,
                text = "",
                font = ("Arial", 8),
                bg = "black",
                fg = "black",
                ).pack(pady=2)
            #canvas= Canvas(gui, width= 150, height= 150)
            #canvas.pack()

            #img= ImageTk.PhotoImage(Image.open("ns.png"))

            #canvas.create_image(10,10,anchor=NW,image=img)
            label = tk.Label(
                gui,
                text = "You will find the QR-Code in the directory you stored this program",
                font = ("Arial", 12),
                bg = "black",
                fg = "#C5FFB8",
                ).pack(fill=tk.X, pady=2)
            button = tk.Button(
                gui,
                text = "Open QR-Code",
                font = ("Arial", 12),
                bg = "#C5FFB8",
                fg = "black",
                command = open_img
                ).pack(pady=2)
            label = tk.Label(
                gui,
                text = "",
                font = ("Arial", 56),
                bg = "black",
                fg = "black",
                ).pack(pady=2)
            label = tk.Label(
                gui,
                text = "Made by NoobScience",
                font = ("Arial", 16),
                bg = "black",
                fg = "#C5FFB8",
                ).pack(fill=tk.X, pady=2)
            
            gui.mainloop()

    def note(self):
        class NSnote:

            gui = Tk()
            gui.configure(bg="black")
            
            Width = 300
            Height = 300
            TextArea = Text(gui, font=("Cascadia", 18), bg="black", fg="white",)
            MenuBar = Menu(gui)
            FileMenu = Menu(MenuBar, tearoff=0, bg="white", fg="black")
            EditMenu = Menu(MenuBar, tearoff=0, bg="white", fg="black")
            HelpMenu = Menu(MenuBar, tearoff=0, bg="white", fg="black")

            ScrollBar = Scrollbar(TextArea)	
            file = None

            def __init__(self,**kwargs):

                    try:
                        self.gui.wm_iconbitmap("Assets/Gallery/icon.ico")
                    except:
                            pass
                    # Win Size
                    try:
                        self.Width = kwargs['width']
                    except KeyError:
                        pass

                    try:
                        self.Height = kwargs['height']
                    except KeyError:
                            pass
                        
                    self.gui.title("Untitled - NSnote")

                    screenWidth = self.gui.winfo_screenwidth()
                    screenHeight = self.gui.winfo_screenheight()
            
                    # For left-alling
                    left = (screenWidth / 2) - (self.Width / 2)
                    
                    # For right-allign
                    top = (screenHeight / 2) - (self.Height /2)
                    
                    # For top and bottom
                    self.gui.geometry('%dx%d+%d+%d' % (self.Width,self.Height,left, top))
                    self.gui.grid_rowconfigure(0, weight=1)
                    self.gui.grid_columnconfigure(0, weight=1)

                    # Add controls (widget)
                    self.TextArea.grid(sticky = N + E + S + W)

                    # Controls
                    self.FileMenu.add_command(label="New",command=self.newFile)	
                    self.FileMenu.add_command(label="Open",command=self.openFile)
                    self.FileMenu.add_command(label="Save",command=self.saveFile)	
                    self.FileMenu.add_separator()										
                    self.FileMenu.add_command(label="Exit",command=self.quitApplication)
                    self.MenuBar.add_cascade(label="File",menu=self.FileMenu)	
                    self.EditMenu.add_command(label="Cut",command=self.cut)			
                    self.EditMenu.add_command(label="Copy",command=self.copy)		
                    self.EditMenu.add_command(label="Paste",command=self.paste)		
                    self.MenuBar.add_cascade(label="Edit",menu=self.EditMenu)	
            
                    self.HelpMenu.add_command(label="About NSnote",command=self.showAbout)
                    self.HelpMenu.add_command(label="NoobScience Website",command=self.website)
                    self.HelpMenu.add_command(label="NSnote Website",command=self.NSnoteWeb)
                    self.HelpMenu.add_command(label="Source",command=self.source)
                    self.HelpMenu.add_command(label="Check out my other Projects",command=self.Projects)
                    self.MenuBar.add_cascade(label="Resources", menu=self.HelpMenu)
                    self.HelpMenu.add_command(label="NoobScience",command=self.NoobScience)

                    self.gui.config(menu=self.MenuBar)

                    self.ScrollBar.pack(side=RIGHT,fill=Y)					
                    
                    # Scrollbar will adjust automatically according to the content		
                    self.ScrollBar.config(command=self.TextArea.yview)	
                    self.TextArea.config(yscrollcommand=self.ScrollBar.set)
            
                    
            def quitApplication(self):
                    self.gui.destroy()
                    # exit()

            def showAbout(self):
                    showinfo("NSnote","NoobScience")

            def openFile(self):
                    self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

                    if self.file == "":
                            self.file = None
                    else:
                            self.gui.title(os.path.basename(self.file) + " - NSnote")
                            self.TextArea.delete(1.0,END)

                            file = open(self.file,"r")

                            self.TextArea.insert(1.0,file.read())

                            file.close()

                    
            def newFile(self):
                    self.gui.title("Untitled - NSnote")
                    self.file = None
                    self.TextArea.delete(1.0,END)

            def saveFile(self):

                    if self.file == None:
                            # Save as new file
                            self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])

                            if self.file == "":
                                    self.file = None
                            else:
                                    file = open(self.file,"w")
                                    file.write(self.TextArea.get(1.0,END))
                                    file.close()

                                    self.gui.title(os.path.basename(self.file) + " - NSnote")
                                        
                    else:
                            file = open(self.file,"w")
                            file.write(self.thisTextArea.get(1.0,END))
                            file.close()

            def cut(self):
                    self.TextArea.event_generate("<<Cut>>")

            def copy(self):
                    self.TextArea.event_generate("<<Copy>>")

            def paste(self):
                    self.TextArea.event_generate("<<Paste>>")

            def website(self):
                result = tkinter.messagebox.askquestion('Website', 'Do you want to vist NoobScience Website?')
                if result == 'yes':
                     webbrowser.open('https://newtoallofthis123.github.io/About')
                else:
                    print('okay, it is https://newtoallofthis123.github.io/About by the way')

            def NSnoteWeb(self):
                result = tkinter.messagebox.askquestion('NSnote Website', 'Do you want to vist the NSnote Website?')
                if result == 'yes':
                     webbrowser.open('https://newtoallofthis123.github.io/NSnote')
                else:
                    print('okay, it is https;//newtoallofthis123.github.io/NSnote by the wat')

            def source(self):
                result = tkinter.messagebox.askquestion('NSnote Source', 'Do you want to fork or look at tthe NSnote Website?')
                if result == 'yes':
                     webbrowser.open('https://github.com/newtoallofthis123/NSnote')
                else:
                    print('okay, it is https://github.com/newtoallofthis123/NSnote, by the way')

            def Projects(self):
                result = tkinter.messagebox.askquestion('Projects', 'Do you want to check out some of my other projects?')
                if result == 'yes':
                     webbrowser.open('https://github.com/newtoallofthis123')
                else:
                    print('okay, it is https://github.com/newtoallofthis123, by the way')

            def NoobScience(self):
                showinfo("About NoobScience", word_About)

            def run(self):

                    self.gui.mainloop()



        word_About = str("I am currently learning to program for my IT journey and to practise, I make simple projects like this that are quite uable and light weight. Check me out at https://newtoallofthis123.github.io/About")
        print("NSnote has started with the theme, if you don't see it, press alt+tab and check all the tabs")
        note = NSnote(width=800,height=500)
        note.run()

        print("A Project by NoobScience, check me out at https://newtoallofthis123.github.io/About")

    def cal(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Calculator', 'Do you want to open the calculator')
        if result=='yes':
           import cal
        else:
           tkinter.messagebox.showinfo('Okay', 'Calculator not opened')

    def joke(self):
        import pyjokes

        gui = Tk()
        gui.title("Joke")
        gui.geometry('800x90')
        gui.config(bg="#002240")
        gui.iconbitmap("Assets/Gallery/icon.ico")
        gui.resizable(True, False)

        j = pyjokes.get_joke()
        joke = StringVar(gui, value = j)

        label = Label(gui, text = "Joke",font=("Cascadia", 24), fg="white", bg="#002240").pack()
        entry = Entry(gui, textvariable = joke, width=120, font=("Cascadia", 12), fg="white", bg="#002240").pack(fill=X)
        label = Label(gui, text = "By NoobScience",font=("Cascadia", 16), fg="white", bg="#002240").pack()

        gui.mainloop()

    def rps(self):
        import random
        from tkinter import ttk
        import time

        gui = Tk()
        gui.title("Rock Paper Scissor")
        gui.iconbitmap("Assets/Gallery/icon.ico")
        gui.geometry("400x400")
        gui.config(bg="#002240")

        #choice = StringVar(gui)
        #choice.set("Rock Paper or Scissor")

        def user_op(e):
            if op.get() == "Rock":
                user = 1
            if op.get() == "Paper":
                user = 2
            if op.get() == "Scissor":
                user = 3
            user_text = "You Choose " + op.get() + ""
            user_label = Label(gui, text=user_text, fg="black", bg="#FFEC47", font=("Cascadia", 16)).pack()
            label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()
            #label = Label(gui, text="Computer is procressing...", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
            comp_op = int(random.randint(1, 3))
            if comp_op == 1:
                com = "Rock"
            if comp_op == 2:
                com = "Paper"
            if comp_op == 3:
                com = "Scissor"
            comp_text = "The Computer choose " + com + ""
            comp_label = Label(gui, text=comp_text, fg="black", bg="#75EBFF", font=("Cascadia", 16)).pack()
            label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()
            #label = Label(gui, text="Processing Options...", fg="white", bg="#002240", font=("Cascadia", 14)).pack()

            if user == comp_op:
                user_label = Label(gui, text="It's a Tie,try again", fg="black", bg="#23FF8F", font=("Cascadia", 12)).pack()
                label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
            if user == 1 and comp_op == 3 or user == 3 and comp_op == 2 or user == 2 and comp_op == 1:
                user_label = Label(gui, text="You Won.Play Again", fg="black", bg="#23FF8F", font=("Cascadia", 16)).pack()
                label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
            if user == 3 and comp_op == 1 or user == 2 and comp_op == 3 or user == 1 and comp_op == 2:
                user_label = Label(gui, text="You Lost. try Again", fg="black", bg="#23FF8F", font=("Cascadia", 16)).pack()
                label = Label(gui, text="----------------------------", fg="white", bg="#002240", font=("Cascadia", 14)).pack()

        op_list = ["Rock", "Paper", "Scissor",]

        label = Label(gui, text="Rock Paper Scissor", fg="white", bg="#002240", font=("Cascadia", 18)).pack()

        #label = Label(gui, text="choose an option  below", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
        op = ttk.Combobox(gui, value=op_list, font=("Cascadia", 16))
        op.pack()
        #op.current(3)
        op.bind("<<ComboboxSelected>>", user_op)
        label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()
        label = Label(gui, text="by NoobScience", fg="white", bg="#002240", font=("Cascadia", 14)).pack()
        label = Label(gui, text="", fg="black", bg="#002240", font=("Cascadia", 4)).pack()

        def processor():
            return
        gui.mainloop()

    def play(self):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("D:\Songs\kelsea ballarini\Kelsea Ballerini - Dibs (Official Music Video).mp3")
        pygame.mixer.music.play()
    def pause(self):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("D:\Songs\kelsea ballarini\Kelsea Ballerini - Dibs (Official Music Video).mp3")
        pygame.mixer.music.pause()
    def stop(self):
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load("D:\Songs\kelsea ballarini\Kelsea Ballerini - Dibs (Official Music Video).mp3")
        pygame.mixer.music.stop()

    def actress(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Actress gallery', 'Do you want to open Actresses')
        if result=='yes':
           import actress
        else:
           tkinter.messagebox.showinfo('Okay', 'Actress gallery not opened')

    def snakes(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Snakes', 'Do you want to open the snakes game')
        if result=='yes':
           import snake
        else:
           tkinter.messagebox.showinfo('Okay', 'Snakes not opened')

    def pong(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Ping Pong', 'Do you want to open Ping Pong Game?')
        if result=='yes':
           import pong
        else:
           tkinter.messagebox.showinfo('Okay', 'Ping Pong not opened')

    def alarm(self):
        import subprocess
        subprocess.call([r'alarm.bat'])

    def wikid(self):
        import subprocess
        subprocess.call([r'wikid.bat'])

    def noob(self):
        import subprocess
        subprocess.call([r'noob.bat'])
    def pwd(self):
        return
    def google(self):
        import subprocess
        subprocess.call([r'google.bat'])
    def links(self):
        import subprocess
        subprocess.call([r'links.bat'])
    def pwdgen(self):
        import random
        import string
        
        gui = Tk()
        gui.title("Password Generator")
        gui.resizable(False, False)
        try:
            gui.iconbitmap("Assets/Gallery/icon.ico")
        except:
            pass
        gui.config(bg = "black")

        length = Spinbox(gui, from_=1, to=160, width=8, bg="#B700FF", fg="black", font=("Cascadia", 8))
        length.grid(row=1, column=5, padx=1)

        def password():
            length_int = int(length.get())
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            digits = string.digits
            symbols = string.punctuation

            whole =  lower + upper + digits + symbols

            pwd1 = random.sample(whole,length_int)

            password = "".join(pwd1)

            textfield = Text(gui, width=20, height=1,bg="#01FF7D", fg="black", font=("Cascadia", 12))
            textfield.grid(row=2, columnspan=12, padx=1, pady=1)    
            textfield.delete(0.0, END)
            textfield.insert(INSERT, password)
            

        button = Button(gui, text="Generate Password", command=password, bg="#F9FF47", fg="black", font=("Cascadia", 8))
        button.grid(row=1, column=7, padx=10)

        gui.mainloop()


    def quit1(self):
        self.gui.quit

    def tictactoe(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Tic Tac Toe', 'Do you want to open Tic Tac Toe Game?')
        if result=='yes':
           import tictactoe
        else:
           tkinter.messagebox.showinfo('Okay', 'Tic Tac Toe not opened')
    def flappy_bird(self):
        from tkinter.messagebox import showinfo
        from tkinter.messagebox import askquestion
        result = tkinter.messagebox.askquestion('Flappy Bird', 'Do you want to open Flappy Bird Game?')
        if result=='yes':
           import flappy_bird
        else:
           tkinter.messagebox.showinfo('Okay', 'Flappy Bird not opened')

    def yt_dl(self):
        import subprocess
        subprocess.call([r'yt-dl.bat'])
      
    def run(self):
        #self.gui.bind('<Configure>', resizer)
        self.gui.mainloop()



word_About = str("I am currently learning to program for my IT journey and to practise, I make simple projects like this that are quite uable and light weight. Check me out at https://newtoallofthis123.github.io/About")
print("NSnote has started with the  theme, if you don't see it, press alt+tab and check all the tabs")
note = NSnote(width=800,height=500)
note.run()

print("A Project by NoobScience, check me out at https://newtoallofthis123.github.io/About")
