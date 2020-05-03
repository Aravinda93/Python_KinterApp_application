from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Check Box')
root.iconbitmap('./Icon_File.ico')
root.geometry('500x500')

var = StringVar()

def checker():
    myLabel = Label(root, text=var.get()).pack()

check = Checkbutton(root, text='Check Me', variable=var, onvalue='Pizza', offvalue='Burger')
check.deselect()
check.pack()

button = Button(root, text='Click', command=checker).pack()

root.mainloop()