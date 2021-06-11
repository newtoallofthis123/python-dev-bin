# NS-DL 
# By NoobScience
# Github: https://github.com/newtoallofthis123/python-dev-bin
# Website: https://newtoallofthis123.github.io/About
# Description: A Gui for Youtube-DL
# Modules used: tkinter, sys, subprocesses, pkg_resources, os

# Importing the neccessary Modules
from tkinter import *
import os
from tkinter.messagebox import showerror, showinfo
import tkinter.ttk as ttk
import sys
import subprocess
import pkg_resources
from tkinter import filedialog

# Definig our main fucntion
def main():
    try:
        gui = Tk()
        gui.title("NS-Dl")
        # Icon is needed, but not neccessary
        try:
            gui.iconbitmap("Assets/Gallery/dl.ico")
        except:
            pass
        gui.geometry("400x260")
        gui.configure(bg="black")

        # Check if youtube-dl is installed if not, install it
        required = {'youtube-dl'}
        installed = {pkg.key for pkg in pkg_resources.working_set}
        missing = required - installed
        if missing:
            python = sys.executable
            subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
        else:
            pass

        def yt_dl():
            try:
                if value2.get() == 'Downloads':
                    url_ = str(url.get())
                    name1 = str(name.get())
                    name_ = f'%USERPROFILE%/Downloads/{name1}.%(ext)s'
                    if value.get() == 'Song':
                        command = f'youtube-dl -o {name_} --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Subtitle' and value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --no-playlist -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Playlist' and value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --yes-playlist  -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Playlist' and value.get() == 'Song':
                        command = f'youtube-dl -o {name_} --no-mtime --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    else:
                        command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                        os.system(command) 
                        showinfo("Downloading", "Press Okay to continue")
                elif value2.get() == 'Choose file Location':
                    url_ = str(url.get())
                    name1 = str(name.get())
                    folder = filedialog.askdirectory(initialdir='', title="Choose A Folder",)
                    name_ = f'{folder}/{name1}.%(ext)s'
                    if value.get() == 'Song':
                        command = f'youtube-dl -o {name_} --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Subtitle' and value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --no-playlist -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Playlist' and value.get() == 'Video':
                        command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --yes-playlist  -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    elif value1.get() == 'Playlist' and value.get() == 'Song':
                        command = f'youtube-dl -o {name_} --no-mtime --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue")
                    else:
                        command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                        os.system(command)
                        showinfo("Downloading", "Press Okay to continue") 
            except:
                showerror("Error", "Someting went wrong, try againn with correct commands and check if youtube-dl is installed and in system path")

        title = Label(gui, text="Youtube Downloader", font=("Cascadia", 16), fg="#43FF00", bg="black")
        title.grid(row=0, column=0, pady=10)

        url_title = Label(gui, text="Enter Youtube Url", font=("Cascadia", 14), fg="#E500FF", bg="black")
        url_title.grid(row=1, column=0, pady=10)

        url = Entry(gui, font=("Cascadia", 12), fg="white", bg="black")
        url.grid(row=1, column=1, pady=10)

        name_title = Label(gui, text="Enter Name", font=("Cascadia", 14), fg="#E500FF", bg="black")
        name_title.grid(row=2, column=0)

        name = Entry(gui, font=("Cascadia", 12), fg="white", bg="black")
        name.grid(row=2, column=1)

        list_ = ["Video", "Song"]
        list1 = ["Subtitle", "Playlist"]
        list2 = ["Downloads", "Choose file Location"]

        value = StringVar(gui)
        value.set("Select format")

        value1 = StringVar(gui)
        value1.set("Other parameters")

        value2 = StringVar(gui)
        value2.set("Downloads")

        options = ttk.OptionMenu(gui, value, *list_,)
        options.grid(row=3, column=1, pady=10, padx=10)

        ext_option = ttk.OptionMenu(gui, value1, *list1,)
        ext_option.grid(row=4, column=1, pady=10, padx=10)

        file_option = ttk.OptionMenu(gui, value2, *list2,)
        file_option.grid(row=4, column=0, pady=10, padx=10)

        button = Button(gui, command=yt_dl, text="Download", font=("Cascadia", 16), borderwidth=0, fg="#00FCFF", bg="black")
        button.grid(row=3, column=0, ipady=2, ipadx=4, pady=10,)

        gui.mainloop()

    except:
        from tkinter.messagebox import showerror
        showerror("Something Went wrong", "Try again or report the issue to https://github.com/newtoallofthis123/python-dev-bin/issues")

if __name__ == '__main__':
    main()
