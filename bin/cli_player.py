from tkinter import filedialog
import pygame
import os
import random
from tkinter.messagebox import showerror

songs = filedialog.askdirectory(initialdir='D:\Songs', title="Choose A folder",)
os.chdir(songs)
playlist = os.listdir(songs)
print(playlist)
#if songs.endswith(".mp3"):
def play():
	try:
		x = random.choice(playlist)
		print(x)
		pygame.mixer.init()
		pygame.mixer.music.load(x)
		pygame.mixer.music.play(loops=0)
	except:
		showerror("Skipping Songs", "Wrong format skipping to next one")
		play()
try:
	play()
except:
	showerror("Skipping Songs", "Wrong format skipping to next one")
	play()