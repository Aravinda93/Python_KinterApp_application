from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('DropDowns')
root.iconbitmap('./Icon_File.ico')
root.geometry('600x600')

def selection():
    myLabell = Label(root, text=selected.get()).pack()

options = ['Monday','Tuesday', 'Wednesday','Thursday', 'Friday'];

selected = StringVar()
selected.set(options[0])

dropdown = OptionMenu(root, selected, *options)
dropdown.pack()

myButton = Button(root, text='Click Me', command=selection).pack()


root.mainloop()