from tkinter import *

root        =   Tk()
#Creating a Label widjet
myLabel1     =   Label(root, text='Hello, Aravinda').grid(row=0, column=0)
myLabel2     =   Label(root, text='You are Awesome').grid(row=1, column=5)

#Display into the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)

root.mainloop()