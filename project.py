from pygame import mixer
import time
from tkinter import filedialog
from tkinter import *
import os

def PlayMusic():
    print('soon')


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

playButton = PhotoImage(file = 'play.png')
Button(root, image = playButton, bg = "#FFFFFF", height = 60, width = 60, command = PlayMusic).place(x=120, y= 500)

pauseButton = PhotoImage(file = 'pause.png')
Button(root, image = pauseButton, bg = "#FFFFFF", height = 60, width = 60, command = mixer.music.pause).place(x=300, y=500)

stopButton = PhotoImage(file = 'stop.png')
Button(root, image = pauseButton, bg = "#FFFFFF", height = 60, width = 60, command = mixer.music.stop).place(x=210, y = 600)



#runs all the tkinter code
root.mainloop()
