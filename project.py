import pygame
from pygame import mixer
import time
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog  import askopenfilename

def PlayMusic():
    print('soon')

#for pausing and unpausing
num = 0

def PauseMusic():
    global num
    num += 1

    #if music is playing
    if pygame.mixer.get_busy():
        if (num%2) == 0:
            pygame.mixer.pause()
            print("Music Paused!")
        else: 
            pygame.mixer.unpause()
            print("Music Unpaused!")
    else:
        print("Music is not playing.")

def BrowseMusic():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
        
root = Tk()
#Title at the top of the window
root.title("Shep's Tech Flex")
#Size of the screen
root.geometry("485x700+290+10")
#Sets the background colour to a nice pink
root.configure(background="#FFC1CC")
#Window can't be resized anymore. Helps because now the GUI wont be stretched/messed with during presentation
root.resizable(False, False)
mixer.init()

lower_frame = Frame(root, bg = "#333333", width = "485", height = "200")
lower_frame.place(x=0, y=500)

playImage = PhotoImage(file =r"play1.png")
Button(root, image=playImage, bg = "#FFFFFF", command=PlayMusic, height=60, width=60).place(x=120, y= 500)

pauseButton = PhotoImage(file = 'pause1.png')
Button(root, image = pauseButton, bg = "#FFFFFF", height = 60, width = 60, command = PauseMusic).place(x=300, y=500)

stopButton = PhotoImage(file = 'stop1.png')
Button(root, image = stopButton, bg = "#FFFFFF", height = 60, width = 60, command = mixer.music.stop).place(x=120, y = 600)

browseFiles = PhotoImage(file = 'cloud.png')
Button(root, image=browseFiles, bg = "#FFFFFF", height = 60, width = 60, command =BrowseMusic).place(x=300, y = 600)

#runs all the tkinter code
root.mainloop()
