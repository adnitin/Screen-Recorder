from tkinter import *

import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Scree Recorder")
root.config(bg='black')
root.resizable(False, False)


def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 5)


def pause_rec():
    rec.pause_recording()


def resume_rec():
    rec.resume_recording()


def stop_rec():
    rec.stop_recording()


rec = pyscreenrec.ScreenRecorder()

# icons
image_icon = PhotoImage(file='screen.png')
root.iconphoto(False, image_icon)

# background image
image_1 = PhotoImage(file='Yellow.png')
Label(root, image=image_1, bg="black").place(x=-2, y=45)

image_2 = PhotoImage(file='blue.png')
Label(root, image=image_2, bg="black").place(x=223, y=200)

# heading
lbl = Label(root, text='Screen Recorder', bg="black", fg="red",  font="arial 16 bold").pack(pady=20)

image_3 = PhotoImage(file='Recording.png')
Label(root, image=image_3, bd=0).pack(pady=28)

# entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15").place(x=72, y=375)
Filename.set("Recording01")

# Buttons
start = Button(root, text="START", bg="gray", fg="Red", font="areal 16", command=start_rec).place(x=128, y=254)

image_4 = PhotoImage(file='pause.png')
pause = Button(root, image=image_4, bg="black", bd=0, command=pause_rec).place(x=57, y=450)

image_5 = PhotoImage(file='resume.png')
resume = Button(root, image=image_5, bg="black", fg="black", bd=0, command=resume_rec).place(x=154, y=450)

image_6 = PhotoImage(file='stop.png')
stop = Button(root, image=image_6, bg="black", fg="black", bd=0, command=stop_rec).place(x=257, y=450)

root.mainloop()
