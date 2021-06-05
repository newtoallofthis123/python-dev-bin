import gtts
import time
import webbrowser
from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3
from tkinter import filedialog
import os
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from playsound import playsound

print("Wait, I am freshning up, don't input anything in the keyboard")
ts = gtts.gTTS("Hello, I am Noob, how may I help you?")
ts.save("intro.mp3")
#time.sleep(5)
ts = gtts.gTTS("Choose an option below")
ts.save("op.mp3")
ts = gtts.gTTS("That one was easy, anything else or shall I sleep?")
ts.save("exit.mp3")
ts = gtts.gTTS("Oh the calendar? I will use NS-Calendar and show you in the terminal")
ts.save("calendar.mp3")
ts = gtts.gTTS("I will gladly set the alarm for you, please follow the instructions on your terminal to set the alarm ")
ts.save("alaram.mp3")
ts = gtts.gTTS("Oh, your alarm is done, Oh, your alarm is done, Oh, your alarm is done,")
ts.save("alaram_sound.mp3")
ts = gtts.gTTS("I will gladly launch the stopwatch")
ts.save("stopwatch.mp3")
ts = gtts.gTTS("Want to know the current time? Okay, it is")
ts.save("time.mp3")
ts = gtts.gTTS("Want to set the timer? Okay")
ts.save("timer.mp3")
ts = gtts.gTTS("Well, Wikipedia allows web scraping, what do you want to search in wikipedia? ")
ts.save("wikicli.mp3")
ts = gtts.gTTS("What a gui for wikicli? I understand. I will launch it")
ts.save("wiki.mp3")
ts = gtts.gTTS("Sppedtest using okla? Okay")
ts.save("speed.mp3")
ts = gtts.gTTS("Joke? I will become a tech savy Chandler and tell you tech jokes")
ts.save("joke.mp3")
ts = gtts.gTTS("Want to generate a Qr-Code, okay")
ts.save("qr.mp3")
ts = gtts.gTTS("Qr-Code saved in the same folder you saved me")
ts.save("qr_exit.mp3")
ts = gtts.gTTS("Thanks for letting me sleep, wake me up if you need anything else")
ts.save("sleep.mp3")
ts = gtts.gTTS("Shortern Url in a gui")
ts.save("url.mp3")
ts = gtts.gTTS("NSnote is so lightweight and awesome. I will launch it")
ts.save("note.mp3")
ts = gtts.gTTS("Want to listen to songs? Okay")
ts.save("song.mp3")
ts = gtts.gTTS("Latest news from google news")
ts.save("news.mp3")
ts = gtts.gTTS("Getting ready to Chat, I will chat through text, by the way")
ts.save("chat.mp3")
ts = gtts.gTTS("Having a good password is very Important. I will help you generate one")
ts.save("pwd.mp3")
ts = gtts.gTTS("I will open the website you give me in your default browser")
ts.save("link.mp3")
ts = gtts.gTTS("Google search in terminal? Okay, I will help you search google")
ts.save("google.mp3")
ts = gtts.gTTS("Want to fork me? Okay. I am opening the github repo in your deflaut browser")
ts.save("fork.mp3")
ts = gtts.gTTS("Vist NoobScience website to know about the other projects. I am opening the Website in your Deflaut Browser")
ts.save("web.mp3")
playsound("intro.mp3")
applist = ("0 for a text Editor \n1 for Calculator \n2 for Calendar \n3 for Alaram \n4 for the StopWatch \n5 for knowing the Time \n6 for Timer Gui \n7 for searching with Wikipedia \n8 for searching with wiki gui \n9 for a SpeedTest \n10 for a joke \n11 for a qr-code generator \n12 for a Url Shortner \n13 for a song player \n14 to know the latest news \n15 for a password generator \n16 to just talk to me \n17 to search with google \n18 to open websites \n19 to fork me \n20 to know about NoobScience")
print(applist)
    
def cal():
    print("Cal-cli by NoobScience")
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second Number "))
    operator= input("Enter the operator ")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Unknown, please try again")

def calendar():
    # The Module datetime is being used here, It is installed by deflaut in python3 or you can download it and append the file directory in the below code
    from datetime import date
    import datetime

    # A whole database of conversion parameters I am using. If you want your own shortcuts, add some to the code below
    monthConversions = {
        "january": 1,
        "febuary": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12,
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
        "j": 1,
        "f": 2,
        "m": 3,
        "a": 4,
        "ma": 5,
        "j": 6,
        "ju": 7,
        "au": 8,
        "s": 9,
        "o": 10,
        "n": 11,
        "d": 12,
    }

    #Intro
    print("                                    NS-CALENDAR                                              ")
    print("                                                           by NoobScience                    ")
    print("Hello, today is a wonderfull day.")
    print("                            Today, the date is " + str(date.today()))

    # using datetime module to show current date and time
    from datetime import datetime

    current = datetime.now()
    current_time_in_format = current.strftime("%H:%M:%S")
    print("                            The current time is " + (current_time_in_format))

    #The Module calendar is being used to render a text calendar
    import calendar

    #Providing Logic to the CLI tool
    chk = str.upper(input("Do you want to see the calender? (Y/N)"))
    if chk == "Y":
        year = int(input("Which year?"))
        chk1 = str.lower(input("The Whole Year or a Particular Month? (Whole/Month)"))
        if chk1 == "whole":
                print("Showing you the calendar of " + str(year))
                print(calendar.calendar(year))
        elif chk1 == "month":
                month = str.lower(input("Which Month?(January,Febuary...) "))
                month_converted = int(monthConversions[month])
                print(calendar.month(year, month_converted))
        else:
            print("Sorry Invalid operator, try again")
    elif chk == "N":
        print("Okay, Have a Nice Day \nNoobScience")
    else:
        print("Sorry Invalid operator, try again")

def alaram():
    from datetime import datetime   #To set date and time
    from playsound import playsound     #To play sound

    def validate_time(alarm_time):
        if len(alarm_time) != 11:
            return "Invalid time format! Please try again..."
        else:
            if int(alarm_time[0:2]) > 12:
                return "Invalid HOUR format! Please try again..."
            elif int(alarm_time[3:5]) > 59:
                return "Invalid MINUTE format! Please try again..."
            elif int(alarm_time[6:8]) > 59:
                return "Invalid SECOND format! Please try again..."
            else:
                return "ok"

    while True:
        alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
        
        validate = validate_time(alarm_time.lower())
        if validate != "ok":
            print(validate)
        else:
            print(f"Setting alarm for {alarm_time}...")
            print(f"Done setting alrm. It will ring at {alarm_time}")
            break
        
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()

    while True:
        now = datetime.now()

        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        if alarm_period == current_period:
            if alarm_hour == current_hour:
                if alarm_min == current_min:
                    if alarm_sec == current_sec:
                        print("Alarm Done")
                        # Set the Path to your song between the two comments
                        playsound("alaram_sound.mp3")
                        # Don't Change the code after this to change the song
                        break

def stopwatch():
    import time
    print('Press ENTER to begin, Press Ctrl + C to stop')
    while True:
        try:
            input()  # For ENTER. Use raw_input() if you are running python 2.x instead of input()
            starttime = time.time()
            print('Started')
            print("Time Elapsed")
            while True:
                print(round(time.time() - starttime, 0), 'secs', end="\r")
                time.sleep(1) # 1 second delay
        except KeyboardInterrupt:
            print('Stopped')
            endtime = time.time()
            print('Total Time:', round(endtime - starttime, 2), 'secs')
            break

def time():
    from datetime import datetime

    current = datetime.now()
    current_time_in_format = current.strftime("%H:%M:%S")
    print("                            The current time is " + (current_time_in_format))

def timer():
    import time
    from playsound import playsound 

    gui = Tk()
    gui.geometry('400x300')
    gui.resizable(True,False)

    gui.config(bg='black')

    sec = StringVar()
    Entry(gui, textvariable=sec, width = 2, font = ("Arial", 14)).place(x=220, y=120)
    sec.set('00')
    mins= StringVar()
    Entry(gui, textvariable = mins, width =2, font = ('Arial', 14)).place(x=180, y=120)
    mins.set('00')
    hrs= StringVar()
    Entry(gui, textvariable = hrs, width =2, font = ('Arial', 14)).place(x=142, y=120)
    hrs.set('00')

    def timer():
       times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
       while times > -1:
          minute,second = (times // 60 , times % 60)
          hour =0
          if minute > 60:
             hour , minute = (minute // 60 , minute % 60)
          sec.set(second)
          mins.set(minute)
          hrs.set(hour)
          
          gui.update()
          time.sleep(1)
          if(times == 0):
             sec.set('00')
             mins.set('00')
             hrs.set('00')
             print("Timer Done, playing alarm")
             playsound("alaram_sound.mp3")
          times -= 1
          
    Label(gui, font =('Helvetica bold',22), text = 'Set the Timer',bg
    ='#FA8574',fg="black").place(x=105,y=70)
    Button(gui, text='START', bd ='2', bg = '#FA8574', fg = "black", font =('Helvetica bold',14), command = timer).place(x=167, y=165)
    gui.mainloop()
    #time.sleep(25)
    gui.quit()

def wikicli():
    import wikipedia
    try:
        print("Hello, I will search wikipedia for you using the wikipedia module. What do you want to do? ")
        print("A - WikiSummary B - Full WikiPage C - Search Wiki with Keyword D - Suggest with KeyWord ")
        print("E - Show links F - Show Short given number of lines summary G - Show reference links ")
        print("H - Categories I - All Links in a Wikipedia Page")
        keyword = str.lower(input("Enter your choice "))
        search = str(input("What is the search term? "))
        if keyword == "a":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiSummary = wikipedia.summary(search)
            print(WikiSummary)
            print("By NoobScience 2021")
        elif keyword == "b":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiPage = wikipedia.page(search).content
            print(WikiPage)
            print("By NoobScience 2021")
        elif keyword == "c":
            number_of_results = int(input("Number of search Results "))
            WikiKey = wikipedia.search(search, results=number_of_results)
            print(WikiKey)
            print("By NoobScience 2021")
        elif keyword == "d":
            WikiSuggest = wikipedia.suggest(search)
            print(WikiSuggest)
            print("By NoobScience 2021")
        elif keyword == "e":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiUrl = wikipedia.page(search).url
            print(WikiUrl)
            print("By NoobScience 2021")
        elif keyword == "f":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            number_of_sentences = int(input("Number of Lines "))
            WikiShort = wikipedia.summary(search, sentences=number_of_sentences)
        elif keyword == "g":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiReference == wikipedia.page(search).references
            print(WikiReference)
            print("By NoobScience 2021")
        elif keyword == "h":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiCategories = wikipedia.page(search).categories
            print("By NoobScience 2021")
        elif keyword == "i":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            WikiLinks = wikipedia.page(search).links
            print(WikiLinks)
            print("By NoobScience 2021")
        elif keyword == "j":
            WikiTitle = wikipedia.page(search).title
            print(WikiTitle)
            img = int(input("Which Image Number? (1,2,3...)"))
            WikiImages == wikipedia.page(search).images[img]
        elif keyword == "k":
            WikiHtmml == wikipedia.page(search).html
        else:
            print("Invalid Keyword, try again")
            print("By NoobScience 2021")
            quit()



    except wikipedia.exceptions.DisambiguationError as e:
            print (e.options)
            print("By NoobScience 2021")

def wiki():
    import wikipedia
    gui = Tk() 
    gui.title('WIKIPEDIA SEARCH')
    gui.geometry('200x70')

    def wiki() :
        search = entry.get()
        wikisum = wikipedia.summary(search)
        showinfo(search,wikisum)

    label = Label(gui,text="Wikipedia Search :")
    label.grid(row=0,column=0)

    entry = Entry(gui)
    entry.grid(row=1,column=0)

    button = Button(gui,text="Search",command=wiki)
    button.grid(row=1,column=1,padx=10)

    gui.mainloop()
    gui.quit()

def speed():
    import speedtest as st
    print("Please Wait as I process that request. It will take sometime. It is advised to wait for about 20sec.\nI will notify you when the results will be out")
    stn = st.Speedtest()
    download = stn.download()
    upload = stn.upload()
    download_conv = download / 1000000
    download_str = str(download_conv)
    upload_conv = upload / 1000000
    upload_str = str(upload_conv)
    print("The Download Speed is : " + download_str + " kb/s")
    print("The Upload Speed is : " + upload_str + " kb/s")
    stn.get_servers([])
    ping = stn.results.ping
    ping_str = str(ping)
    print("The Ping is: " + ping_str + " ms")

def joke():
    import pyjokes 
    print(pyjokes.get_joke())

def qr():
    import pyqrcode
    from PIL import Image, ImageTk
    data1 = input("Enter Data for Qr-Code: ")
    name = input("Enter qr-code name: ")
    image = pyqrcode.create(data1)
    image.png((name), scale=10)

def url():
    
    import pyperclip
    import pyshorteners
    import tkinter as tk

    try:
        def processor():
            shorten = pyshorteners.Shortener()
            shortening = shorten.gitio.short(url.get())

            short_url.set(shortening)

        def copy():
            pyperclip.copy( short_url.get())

         # if it is satified,   
        if __name__=="__main__":
            gui = tk.Tk()
            gui.title("IJ_URL")
            gui.geometry("600x600")
            gui.configure(bg="black")

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

    # Loop Continuoesly
            gui.mainloop()

    except:
        print("Sorry, something went wrong")
        choice = input("Do you want to trouble shoot? (y/n): ")
        if choice=="y":
            print("Check if all necessary Modules are installed., Check for: ")
            print("Modules: ")
            print(" pyperclip: pip install pyperclip,")
            print(" pyshorteners: pip install pyshorteners")
            print("Check if you have python installed properly.")
            print("If not, get another version of this from my repository https://github.com/newtoallofthis123")
        elif choice=='n':
            print("Okay, Thanks for using. Check out my other projects at https://github.com/newtoallofthis123")

        else:
            print("Thanks for using")

def note():
    print("NSnote by NoobScience")
    print("Define Specific for gui, Deflault themes: ")
    print("black; dracula; white; red; green; violet; pink")
    choice = str(input("Deflaut themes(y) or custom(n), (y/n)?"))
    if choice == 'y':
        theme = str.lower(input("Which theme?"))
        if theme == 'black':
            bgvar = "black"
            fgvar = "White"
            fontvar = "Arial 12 bold"
        elif theme == 'dracula':
            bgvar = "#002240"
            fgvar = "White"
            fontvar = "Cascadia 16 bold"
        elif theme == 'white':
            bgvar = "White"
            fgvar = "Black"
            fontvar = "Arial 18 bold"
        elif theme == 'red':
            bgvar = "#FF5D4F"
            fgvar = "#434141"
            fontvar = "CascadiaCode 18 bold"
        elif theme == 'green':
            bgvar = "#22FF22"
            fgvar = "black"
            fontvar = "Arial 18 bold"
        elif theme == 'violet':
            bgvar = "#8D54FD"
            fgvar = "#45404F"
            fontvar = "CascadiaCode 18 bold"
        elif theme == 'pink':
            bgvar = "#FF14AB"
            fgvar = "black"
            fontvar = "CascadiaCode 18 bold"
        else:
            print("Request Invalid, try agin")
            print("Quitting application, --------------------------...........NoobScience............-----------------------------")
            exit()
            
    elif choice == 'n':
        bgvar = input("Specify background color: ")
        fgvar = input("Specify font color: ")
        fontvar = input("Specify Font as fontfamily size bold (Arial 18 bold): ")
    else:
        print("Sorry, Invalid Request Try again:")
        print("Quitting application, --------------------------...........NoobScience............-----------------------------")
        exit()
    class NSnote:

        gui = Tk()
        gui.configure(bg="black")
        
        Width = 300
        Height = 300
        TextArea = Text(gui, font=fontvar, bg=bgvar, fg=fgvar,)
        MenuBar = Menu(gui)
        FileMenu = Menu(MenuBar, tearoff=0, bg="#969696", fg=fgvar)
        EditMenu = Menu(MenuBar, tearoff=0, bg="#969696", fg=fgvar)
        HelpMenu = Menu(MenuBar, tearoff=0, bg="#969696", fg=fgvar)

        ScrollBar = Scrollbar(TextArea)	
        file = None

        def __init__(self,**kwargs):

                try:
                    self.gui.wm_iconbitmap("D:\Applications\Custom icons\Papirus-Team-Papirus-Apps-Marknoto.ico")
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
    print("NSnote has started with the " + theme +" theme, if you don't see it, press alt+tab and check all the tabs")
    note = NSnote(width=800,height=500)
    note.run()

    print("A Project by NoobScience, check me out at https://newtoallofthis123.github.io/About")

def song():
    import pygame
    gui = Tk()
    gui.minsize(546,580)
    gui.configure(bg="#002240")
    gui.title("NSPlayer")
    gui.geometry('500x500')
    gui.resizable(False,False)

    # If you encounter error, change the path of the file in the comments and uncomment it to have a file icon (Remove the three quotes)

    '''photo = PhotoImage(file = "pygame/NSPlayer.png")
    gui.iconphoto(False, photo)'''




    # Listing and reading names of the songs
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

    # Loop Through
    gui.mainloop()
    gui.quit()

def news():
    def news(xml_news_url,counter):
        '''Print select details from a html response containing xml
          @param xml_news_url: url to parse
          '''
        context = ssl._create_unverified_context()
        Client = urlopen(xml_news_url, context=context)
        xml_page = Client.read()
        Client.close()
        soup_page = soup(xml_page, "xml")

        news_list = soup_page.findAll("item")
        i = 0  # counter to print n number of news items

        for news in news_list:
            print(f'news title:   {news.title.text}')    # to print title of the news
            print(f'news link:    {news.link.text}')     # to print link of the news
            print(f'news pubDate: {news.pubDate.text}')  # to print published date
            print("+-" * 20, "\n\n")


            if i == counter :
              break
            i = i + 1

    # you can add google news 'xml' URL here for any country/category
    news_url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
    sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

    # now call news function with any of these url or BOTH
    news(news_url,10)    
    news(sports_url,5)

def pwd():
    import random
    import string

    print("PassswordGen")

    pwdlength = int(input("Specify Password Length: "))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    whole =  lower + upper + digits + symbols

    pwd1 = random.sample(whole,pwdlength)

    password = "".join(pwd1)
    print("Copy the below given password and paste it: ")
    print(password)

def link():
    import webbrowser
    url = str(input("What is the website you want to visit? (in the form youtube.com): "))
    url_full = "https://" + url
    print("Opening " + url)
    webbrowser.open(url_full, new=1)
    print("Opened " + url + " in your deflaut browser")

def google():
    from googlesearch import search

    query = str(input("What is the search query: "))
    numb = int(input("Enter number of searching: "))
    print("Searching for links related to " + query + " on google")
    for sear in search(query, tld="co.in", num=numb, stop=10, pause=2):
        print(sear)

def exit1():
    playsound("exit.mp3")
    choice1 = str.lower(input("Shall I sleep(s) or continue(c)? "))
    if choice1 == 'c':
        #print(applist)
        noob()
    elif choice1 == 's':
        print("Bye, Call me if you need me again")
        playsound("sleep.mp3")
        exit()


def noob():
    playsound("op.mp3")
    choice = input("What is your option? ")
    if choice == '1':
        cal()
        exit1()

    if choice == '2':
        playsound("calendar.mp3")
        calendar()
        exit1()
        
    if choice == '3':
        playsound("alaram.mp3")
        alaram()
        exit1()
        
    if choice == '4':
        playsound("stopwatch.mp3")
        stopwatch()
        playsound("exit.mp3")
        exit1()
        
    if choice == '5':
        playsound("time.mp3")
        time()
        exit1()
        
    if choice == '6':
        playsound("timer.mp3")
        timer()
        exit1()
        
    if choice == '7':
        playsound("wikicli.mp3")
        wikicli()
        exit1()
        
    if choice == '8':
        playsound("wiki.mp3")
        wiki()
        exit1()
        
    if choice == '9':
        playsound("speed.mp3")
        speed()
        exit1()
        
    if choice == '10':
        playsound("joke.mp3")
        joke()
        exit1()
        
    if choice == '11':
        playsound("qr.mp3")
        qr()
        playsound("qr_exit.mp3")
        exit1()
        
    if choice == '12':
        playsound("url.mp3")
        url()
        exit1()
        
    if choice == '0':
        playsound("note.mp3")
        note()
        exit1()
        
    if choice == '13':
        playsound("song.mp3")
        song()
        exit1()
        
    if choice == '14':
        playsound("news.mp3")
        news()
        exit1()
        
    if choice == '16':
        playsound("chat.mp3")
        import chat
        exit1()
    if choice =='15':
        playsound("pwd.mp3")
        pwd()
        exit1()
    if choice == '18':
        playsound("link.mp3")
        link()
        exit1()
    if choice == '17':
        playsound("google.mp3")
        google()
        exit1()
    if choice == '19':
        playsound("fork.mp3")
        webbrowser.open("https://github.com/newtoallofthis123/Noob")
        exit1()
    if choice == '20':
        playsound("web.mp3")
        webbrowser.open("https://newtoallofthis123.github.io/About")
        exit1()
noob()
        
    
    

