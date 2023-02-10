import pygame
from pygame import mixer
import time
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog  import askopenfilename

from pydub import AudioSegment
from pydub.playback import play

pygame.init
pygame.mixer.init()

num = 0
multiplefiles = 0

def PlayMusic():
    global multiplefiles 
    multiplefiles +=1
    musicFile = askopenfilename(filetypes=[("Audio Files","*.wav")])
    print(musicFile)
    sound = pygame.mixer.Sound(musicFile)
    sound.play()
    if (multiplefiles %2) == 0:
        print('test')
        sound.stop()
def PauseMusic():
    global num
    num += 1

    #if music is playing
    if pygame.mixer.get_busy():
        if (num%2) == 0:
            pygame.mixer.unpause()
            print("Music UnPaused!")
        else: 
            pygame.mixer.pause()
            print("Music Paused")
    else:
        print("Music is not playing.")

def StopMusic():
    sound.stop()
        


root = Tk()
#Title at the top of the window
root.title("Shep's Tech Flex")
#Size of the screen
root.geometry("485x700+290+10")
#Sets the background colour to a nice pink
root.configure(background="#FFC1CC")
#Window can't be resized anymore. Helps because now the GUI wont be stretched/messed with during presentation
root.resizable(False, False)

lower_frame = Frame(root, bg = "#FFFFFF", width = "485", height = "200")
lower_frame.place(x=0, y=500)

#Play music button.
playImage = PhotoImage(file =r"play1.png")
Button(root, image=playImage, bg = "#FFFFFF", command=PlayMusic, height=60, width=60).place(x=120, y= 500)

#Pause music button
pauseButton = PhotoImage(file = 'pause1.png')
Button(root, image = pauseButton, bg = "#FFFFFF", height = 60, width = 60, command = PauseMusic).place(x=300, y=500)

#Stop button
stopButton = PhotoImage(file = 'stop1.png')
Button(root, image = stopButton, bg = "#FFFFFF", height = 60, width = 60, command = StopMusic).place(x=120, y = 600)

#Browse file button (might not need, added because I was on autopilot)
#browseFiles = PhotoImage(file = 'gas.png')
#Button(root, image=browseFiles, bg = "#FFFFFF", height = 60, width = 60, command =BrowseMusic).place(x=300, y = 600)

#runs all the tkinter code
root.mainloop()
