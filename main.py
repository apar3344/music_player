import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Great Music Player")
root.geometry("485x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()

# Create a function to open a file
def add_music():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     playlist.insert(END, song)


def play_music():
    music_name = playlist.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()

# icon
lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)

image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

frame_count = 6
frames = [PhotoImage(file='aa1.gif', format = 'gif -index %i' % i) for i in range(frame_count)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

# Buttons
button_play = PhotoImage(file="play.png")
Button(root, image=button_play, bg="#FFFFFF", bd=0, height=60, width=60, command=play_music).place(x=215, y=487)

button_stop = PhotoImage(file="stop.png")
Button(root, image=button_stop, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.stop).place(x=130, y=487)

button_volume = PhotoImage(file="volume.png")
Button(root, image=button_volume, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.unpause).place(x=20, y=487)

button_pause = PhotoImage(file="pause.png")
Button(root, image=button_pause, bg="#FFFFFF", bd=0, height=60, width=60, command=mixer.music.pause).place(x=300, y=487)

# Labels
menu_label = PhotoImage(file="menu.png")
Label(root, image=menu_label).place(x=0, y=580, width=485, height=120)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF", command=add_music).place(x=0, y=550)

scroll = Scrollbar(frame_music)
playlist = Listbox(frame_music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=RIGHT, fill=BOTH)

# Execute Tkinter
root.mainloop()
