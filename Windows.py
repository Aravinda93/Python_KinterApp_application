from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Windows')
root.iconbitmap('./Icon_File.ico')

def open():
    global myimage
    top = Toplevel()
    top.title('Second Window')
    myimage = ImageTk.PhotoImage(Image.open('./images/Profit.png'))
    myLabel = Label(top, image=myimage).pack()
    button2 = Button(top,text='Close Window', command=top.destroy).pack()

button = Button(root, text='Click Me', command=open).pack()
#label = Label(top, text='Hello Aravinda').pack()


mainloop()