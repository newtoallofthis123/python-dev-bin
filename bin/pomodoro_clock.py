import time
from tkinter import *
import json

gui = Tk()
gui.title("Pomodoro Clock")
gui.geometry("300x120")
gui.resizable(False, False)
gui.iconbitmap("Assets/pomodoro_icon.ico")
gui.config(bg="#131215")

time_remianing_gui = StringVar()

def time_the_pomodoro():
    try:
        file = open("pomodoro_clock_timer.json", 'r')
        content = file.read()
        json_data = json.loads(content)
        time_to_remind_min = int(json_data["time_in_minutes"])
        time_to_remind_sec = int(json_data["time_in_seconds"])
    except:
        time_to_remind_min = 40
        time_to_remind_sec = 00
    time_in_seconds = time_to_remind_min * 1/40 + time_to_remind_sec
    i = 0
    while i < time_in_seconds:
        i += 1
        time.sleep(1)
        time_remaining_in_seconds = time_in_seconds -i
        time_remaining_min, time_remaining_sec = (time_remaining_in_seconds // 60, time_remaining_in_seconds % 60)
        time_remaining =f'{time_remaining_min}:{time_remaining_sec}'
        time_remianing_gui.set(time_remaining)
        gui.update()
    root = Tk()
    root.title("Timer Completed!!")
    root.geometry("370x94")
    root.iconbitmap("Assets/pomodoro_icon.ico")
    root.config(bg="#131215")
    completed_label = Label(root, font=("Cascadia Code", 24), fg="#E2E9FF", bg="#131215", text="Completed Pomodoro").pack()
    take_a_break_label = Label(root, font=("Cascadia Code", 24), fg="#CB2544", bg="#131215", text="Take a Break :)").pack()
    root.mainloop()

label = Label(gui, font=("Cascadia Code", 24), fg="#E2E9FF", bg="#131215", text="Pomodoro Clock").pack()
entry = Entry(gui, textvariable=time_remianing_gui, font=("Cascadia Code", 16), fg="#CB2544", bg="#131215", borderwidth=0).pack()
button = Button(gui, font=("Cascadia Code", 18), fg="#E2E9FF", bg="#131215", text="Restart", command=time_the_pomodoro, borderwidth=0).pack()
time_the_pomodoro()
gui.mainloop()
