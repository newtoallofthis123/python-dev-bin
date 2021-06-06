try:
    from tkinter import *
    import os
    from tkinter.messagebox import showerror
    import tkinter.ttk as ttk

    gui = Tk()
    gui.title("Dl")
    try:
        gui.iconbitmap("Assets/Gallery/icon.ico")
    except:
        pass
    gui.geometry("400x260")
    gui.configure(bg="black")

    def yt_dl():
        try:
            url_ = str(url.get())
            name1 = str(name.get())
            name_ = f'%USERPROFILE%/Downloads/{name1}.%(ext)s'
            if value.get() == 'Song':
                command = f'youtube-dl -o {name_} --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                os.system(command)
            elif value.get() == 'Video':
                command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                os.system(command)
            elif value1.get() == 'Subtitle' and value.get() == 'Video':
                command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --no-playlist -i {url_}'
                os.system(command)
            elif value1.get() == 'Playlist' and value.get() == 'Video':
                command = f'youtube-dl -o {name_} --no-mtime --write-sub --embed-subs --yes-playlist  -i {url_}'
                os.system(command)
            elif value1.get() == 'Playlist' and value.get() == 'Song':
                command = f'youtube-dl -o {name_} --no-mtime --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 --no-mtime --embed-thumbnail -i {url_}'
                os.system(command)
            else:
                command = f'youtube-dl -o {name_} --no-playlist --no-mtime -i {url_}'
                os.system(command) 
        except:
            showerror("Error", "Someting went wrong, try agian with correct commands")

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

    value = StringVar(gui)
    value.set("Select format")

    value1 = StringVar(gui)
    value1.set("Other parameters")

    options = ttk.OptionMenu(gui, value, *list_,)
    options.grid(row=3, column=1, pady=10, padx=10)

    ext_option = ttk.OptionMenu(gui, value1, *list1,)
    ext_option.grid(row=4, column=1, pady=10, padx=10)

    button = Button(gui, command=yt_dl, text="Download", font=("Cascadia", 16), borderwidth=0, fg="#00FCFF", bg="black")
    button.grid(row=3, column=0, ipady=2, ipadx=4, pady=10,)

    gui.mainloop()

except:
    from tkinter.messagebox import showerror
    showerror("Something Went wrong", "Try again or report the issue to https://github.com/newtoallofthis123/python-dev-bin/issues")