#Script to play music
from playsound import playsound  #Import the modules
import os  
os.system("ls | grep .mp3 > mFile") #Python will read the music to be played as value in a list.
l = open("mFile","r").read().strip().split("\n")

for i in l:
    playsound(i)
