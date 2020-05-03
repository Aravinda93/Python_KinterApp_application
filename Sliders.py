from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Sliders')
root.iconbitmap('./Icon_File.ico')
root.geometry('400x400')

def sliderval():
    myLabel = Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()*5)+'x'+str(vertical.get()*5))

vertical = Scale(root, from_=0, to=100)
vertical.pack()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()

Button(root, text='Click', command=sliderval).pack()

root.mainloop()