from tkinter import *
import pygame
import random

songs = dict(song1="I:\songs\Hailee Steinfeld, BloodPop - Capital Letters.mp3")

songName, song = random.choice(list(songs.items()))
#print(songName)
#print(song)

pygame.mixer.init()

pygame.mixer.music.load(song)
pygame.mixer.music.play(loops=0)