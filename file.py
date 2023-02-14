import pygame
from pygame import mixer
import time
from tkinter import filedialog
from tkinter import *
from tkinter.filedialog  import askopenfilename

#Initializes pygame and mixer.
pygame.init()
pygame.mixer.init()

#For pausing and unpausing!
num = 0

def songsQueued(): 
    print('queue')

#Plays Music
def PlayMusic():    
    musicFile = askopenfilename(filetypes=[("Audio Files","*.wav")])
    print(musicFile)
    sound = pygame.mixer.Sound(musicFile)
    sound.play()
    #Checks if music is playing because if a new song is selected this runs so that 2 songs dont play simultaneously 
    if pygame.mixer.get_busy():
        pygame.mixer.stop()
        sound.play()

        noprefix = musicFile.removeprefix('C:/Users/Alexa/Downloads/')
        nosuffix = noprefix.removesuffix('.wav')

        global song2
        global song
        
        T = Text(root, height = '30', width = '100')
        song = Label(root, text = "Currently Playing: ")
        song2 = Label(root, text = str(nosuffix))
        song.config(font=("Monocraft", 10))
        song2.config(font=("Monocraft", 10))
        song.pack()
        song2.pack()

#testing

#Pauses Music
def PauseMusic():
    global num
    num += 1

    #checks if music is playing then it checks if num = an odd number, if number is even, music unpauses, odd it pauses.
    if pygame.mixer.get_busy():
        if (num%2) == 0:
            pygame.mixer.unpause()
            print("Music UnPaused!")
        else: 
            pygame.mixer.pause()
            print("Music Paused")
    else:
        print("Music is not playing.")

#Stops music.
def StopMusic():
    pygame.mixer.stop()
    killText()
        
def killText():
    global song
    global song2
    
    song2.destroy()
    song.destroy()

def increaseVolume():
    print("Volume Increased by 0.1!")
    volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(volume + 1)
    print(volume)


def decreaseVolume():
    print("Volume Decreased by 0.1!")
    volume = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(volume - 1)
    print(volume)


#:)

root = Tk()
#Title at the top of the window
root.title("Shep's Tech Flex")
#Size of the screen
root.geometry("485x700+290+10")
#Sets the background colour to a nice pink
root.configure(background="#FFC1CC")
#Window can't be resized anymore. Helps because now the GUI wont be stretched/messed with during presentation
root.resizable(False, False)

#GIF of stickboy in the middle! 
frameCnt = 30
frames = [PhotoImage(file='aa1.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame, width = '500')
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

#for the buttons!
lower_frame = Frame(root, bg = "#FFC1CC", width = "485", height = "200")
lower_frame.place(x=0, y=500)

#Play music button.
playImage = PhotoImage(file =r"play1.png")
Button(root, image=playImage, bg = "#FFFFFF", command=PlayMusic, height=60, width=60).place(x=290, y= 520)

#Pause music button
pauseButton = PhotoImage(file = 'pause1.png')
Button(root, image = pauseButton, bg = "#FFFFFF", height = 60, width = 60, command = PauseMusic).place(x=360, y=520)

#Stop button
stopButton = PhotoImage(file = 'stop1.png')
Button(root, image = stopButton, bg = "#FFFFFF", height = 60, width = 60, command = StopMusic).place(x=325, y = 600)

plusButton = PhotoImage(file = 'plus.png')
Button(root, image = plusButton, bg = "#FFFFFF", height = 60, width = 60, command = increaseVolume).place(x= 80, y=520)

minusButton = PhotoImage(file = 'minus.png')
Button(root, image = minusButton, bg = "#FFFFFF", height = 60, width = 60, command = decreaseVolume).place(x=80, y= 600)

#runs all the tkinter code
root.mainloop()