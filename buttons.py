from tkinter import *

root        =   Tk()

def myClick():
    myLabel    =    Label(root,text='I Clicked it')
    myLabel.pack()

myButton    =   Button(root, text='Click Me!!', command=myClick, fg='blue', bg='green')
myButton.pack()

root.mainloop()