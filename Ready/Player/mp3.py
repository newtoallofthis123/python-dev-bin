from tkinter import *
from tkinter.messagebox import showerror
try:
    import pygame
    from mutagen.mp3 import MP3
except:
    showerror("Pygame Not found", "Pygame is required to run Player. Install it with pip install pygame and try again....Closing Application")
    quit()
from tkinter import filedialog
import time 
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

def main():
    gui = Tk()
    gui.title("Player")
    gui.iconbitmap("Assets/icon.ico")
    gui.geometry('500x550')
    #gui.resizable(False, False)

    pygame.mixer.init()

    def add_song(e):
        song = filedialog.askopenfilename(initialdir='D:\Songs', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
        #song = song.replace("D:/Songs/", "")
        #song = song.replace(".mp3", "")
        box.insert(END, song)

    def add_multisong(e):
        songs = filedialog.askopenfilenames(initialdir='D:\Songs', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

        for song in songs:
            box.insert(END, song)

    def add_folder(e):
        import os
        songs = filedialog.askdirectory(initialdir='D:\Songs', title="Choose A folder",)
        os.chdir(songs)
        playlist = os.listdir(songs)
        #if songs.endswith(".mp3"):
        for song in playlist:
            #realdir = os.path.realpath(files)
            #audio = ID3(realdir)
            #realnames.append(audio['TIT2'].text[0])
            box.insert(END, song)

    def del_song(e):
        stop()
        box.delete(ANCHOR)
        pygame.mixer.music.stop()

    def del_songs(e):
        try:
            stop()
            box.delete(0, END)
            pygame.mixer.music.stop()
        except:
            showerror("Error", "Unable to delete, select a file and try again")
        
    def play():
        try:
            global stopped
            stopped = False
            song = box.get(ACTIVE)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            song_time()

            #slider_position = int(song_length)
            #slider.config(to=slider_position, value=0)
        except:
            showerror("Play Error", "Select a valid music file(mp3, wav, ogg)")
            box.delete(ANCHOR)
    global stopped
    stopped = False
    def stop():
        status.config(text="")
        slider.config(value=0)
        pygame.mixer.music.stop()
        box.selection_clear(ACTIVE)
        status.config(text="")

        global stopped
        stopped = True

    global paused
    paused = False

    About = "Player is a beginner friendly python project.It is registered under the MIT lisence. Feel free to use it however you like"
    Author = "I am a learning python and wrote this to learn tkinter. Check out some of my other projects at https://github.com/newtoallofthis123. Also Check out my Website for other projects https://newtoallofthis123.github.io/About"

    def pause(is_paused):
        global paused
        paused = is_paused

        if paused:
            pygame.mixer.music.unpause()
            paused = False
        else:
            pygame.mixer.music.pause()
            paused = True

    def forward():
        try:
            status.config(text="")
            slider.config(value=0)
            next_song = box.curselection()
            #print(next_song)
            #print(next_song[0])
            next_song = next_song[0]+1
            song = box.get(next_song)
            #print(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            box.selection_clear(0, END)
            box.activate(next_song)
            box.selection_set(next_song, last=None)
        except:
            showerror("Unable to foward", "No song selected to foward")

    def back():
        try:
            status.config(text="")
            slider.config(value=0)
            prev_song = box.curselection()
            #print(next_song)
            #print(next_song[0])
            prev_song = prev_song[0]-1
            song = box.get(prev_song)
            #print(song)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)

            box.selection_clear(0, END)
            box.activate(prev_song)
            box.selection_set(prev_song, last=None)
        except:
            showerror("Unable to move back", "No song selected to move back")

    def song_time():
        if stopped:
            return
        current_t = (pygame.mixer.music.get_pos()) / 1000

        #slider_label.config(text=f'Slider: {int(slider.get())} and Song Position: {int(current_t)}')
        converted_t = time.strftime('%H:%M:%S' , time.gmtime(current_t))
        #current_s = box.curselection()
        song = box.get(ACTIVE)

        song_mutagen = MP3(song)
        global song_length
        song_length = song_mutagen.info.length
        converted_s_t = time.strftime('%H:%M:%S' , time.gmtime(song_length))
        current_t +=1

        if int(slider.get()) == int(song_length):
            status.config(text=f'Time passed: {converted_s_t} of {converted_s_t}  ')

        elif paused:
            pass

        elif int(slider.get()) == int(current_t):
            slider_position = int(song_length)
            slider.config(to=slider_position, value=int(current_t))
        else:
            slider_position = int(song_length)
            slider.config(to=slider_position, value=int(slider.get()))
            converted_t = time.strftime('%H:%M:%S' , time.gmtime(int(slider.get())))
            status.config(text=f'Time passed: {converted_t} of {converted_s_t}  ')
            next_time = int(slider.get()) + 1
            slider.config(value=next_time)
        #status.config(text=f'Time passed: {converted_t} of {converted_s_t}   ')
        #slider.config(value=current_t)
        #temp = Label(gui, text=int(current_t))
        #temp.pack(pady=10)

        #slider_position = int(song_length)
        #slider.config(to=slider_position, value=int(current_t))
        status.after(1000, song_time)

    def slide(x):
        #hi = slider.get()
        #slider_label.config(text=f'{int(slider.get())} of {int(song_length)}')
        song = box.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0, start=int(slider.get()))

    def vol(x):
        pygame.mixer.music.set_volume(vol_slider.get())
        
    def quit1(e):
        gui.quit()
        
    def openNoobweb():
        webbrowser.open("https://newtoallofthis123.github.io/About")
        
    def showInfo():
        showinfo("About NoobNote", About)
            
    def aboutAuthor():
        showinfo("NoobScience", Author)
        
    def projects():
        webbrowser.open("https://github.com/newtoallofthis123")
            
    root = Frame(gui)
    root.pack(pady=20)

    title = Label(root, text="Player", borderwidth=0,fg="black", font=("Cascadia", 24))
    title.grid(row=0, column=0, ipady=10, ipadx=10)

    box = Listbox(root, bg="#F0F0F0", fg="black", width=40, selectbackground=("blue"), selectforeground=("black"), borderwidth=0, font=("Cascadia", 15), selectborderwidth=0,)
    box.grid(row=1, column=0)

    back_img = PhotoImage(file='Assets/prev.png')
    forward_img = PhotoImage(file='Assets/next.png')
    play_img = PhotoImage(file='Assets/play.png')
    pause_img = PhotoImage(file='Assets/pause.png')
    stop_img = PhotoImage(file='Assets/stop.png')
    exit_img = PhotoImage(file='Assets/exit.png')

    control_frame = Frame(root)
    control_frame.grid(row=2, column=0)

    back_btn = Button(control_frame, image=back_img, borderwidth=0, command=back)
    forward_btn = Button(control_frame, image=forward_img, borderwidth=0, command=forward)
    play_btn = Button(control_frame, image=play_img, borderwidth=0, command=play)
    pause_btn = Button(control_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
    stop_btn = Button(control_frame, image=stop_img, borderwidth=0, command=stop)
    exit_btn = Button(control_frame, image=exit_img, borderwidth=0, command=gui.quit)

    back_btn.grid(row=0, column=0, padx=0)
    forward_btn.grid(row=0, column=1, padx=2)
    play_btn.grid(row=0, column=2, padx=12)
    pause_btn.grid(row=0, column=3, padx=12)
    stop_btn.grid(row=0, column=4, padx=12)
    exit_btn.grid(row=0, column=5, padx=12)


    file_menu = Menu(gui)
    gui.config(menu=file_menu)
     
    addSongmenu = Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label="File", menu=addSongmenu)
    addSongmenu.add_command(label="Add One Song To Playlist", command=lambda: add_song(False))
    addSongmenu.add_command(label="Add Multiple Files", command=lambda: add_multisong(False))
    addSongmenu.add_command(label="Add folder", command=lambda: add_folder(False))
    addSongmenu.add_separator()
    #addSongmenu.add_command(label="New Window", command=lambda: new_win(False))
    addSongmenu.add_command(label="Quit", command=lambda: quit1(False))

    removeSong = Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label="Edit", menu=removeSong)
    removeSong.add_command(label="Delete the selected song", command=lambda: del_song(False))
    removeSong.add_command(label="Delete all the songs in the playlist", command=lambda: del_songs(False))

    aboutMenu = Menu(file_menu, tearoff=False)
    file_menu.add_cascade(label="Help", menu=aboutMenu)
    aboutMenu.add_command(label="About Author", command=aboutAuthor)
    aboutMenu.add_command(label="About Player", command=showInfo)
    aboutMenu.add_command(label="NoobScience Website", command=openNoobweb)
    aboutMenu.add_command(label="Some of my other projects", command=projects)

    status = Label(gui, text="", bd=1, relief=GROOVE, anchor=S,)
    status.pack(fill=X, side=BOTTOM, ipady=2)
    status.config(font=("Cascadia", 12))
    status.config(borderwidth=0)

    slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=300, command=slide)
    slider.grid(row=3, column=0, pady=10)

    vol_slider = ttk.Scale(root, from_=0, to=1, orient=VERTICAL, value=1, length=100, command=vol)
    vol_slider.grid(row=2, column=3)

    #vol_frame = Label(root, text="Volume").grid(row=0, column=6)

    #slider_label = Label(gui, text="0")
    #slider_label.pack()

    gui.bind('<Control-Key-o>', add_song)
    gui.bind('<Control-Key-O>', add_multisong)
    gui.bind('<Control-Key-f>', add_folder)
    gui.bind('<Control-Key-d>', del_song)
    gui.bind('<Control-Key-D>', del_songs)
    gui.bind('<Control-Key-q>', quit1)
    #gui.bind('<Control-Key-N>', new_win)


    gui.mainloop()

if __name__ == '__main__':
    main()