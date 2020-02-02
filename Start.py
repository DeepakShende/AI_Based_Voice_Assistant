import os
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
python_scripts = {'here': 'D:/Projects/AIVA DVD/Aiva/Aiva.py'}


def run_python_scrip(voice_note):
    for key, value in python_scripts.items():
        os.system('python {}'.format(value))


root.geometry('1600x900')
root.title("AIVA")

root.iconbitmap(r'icon1.ico')

label_1 = Label(root, bg="white")
label_1.pack()

label_6 = Label(root, bg="white")
label_6.pack()

label_5 = Label(root, bg="white")
label_5.pack()

photo = ImageTk.PhotoImage(Image.open("aiva3.jpg"))
labelphoto = Label(root, image=photo, bg = "white")
labelphoto.pack()

label_4 = Label(root, bg="white")
label_4.pack()

label_7 = Label(root, bg="white")
label_7.pack()

label_2 = Label(root, bg="white")
label_2.pack()

START = Button(root, text="START", fg='white', bg='#228B22', font=("gothic", 20, 'bold'), width=10)
START.bind("<Button-1>", run_python_scrip)
START.pack()

label_3 = Label(root, bg="white")
label_3.pack()

STOP = Button(root, text="STOP", fg='white', bg='red', font=("gothic", 20, 'bold'), width=10, command=root.destroy)
STOP.pack()

root.configure(background='white')

root.mainloop()
