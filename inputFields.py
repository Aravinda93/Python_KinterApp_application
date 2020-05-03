from tkinter import *

root        =   Tk()

def myClick():
    myLabel =   Label(root,text='Hello'+e.get())
    myLabel.pack()

e           =   Entry(root, width=50)
e.insert(0,'Enter Your Name')
def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    e.delete(0, "end")
    return None
e.bind("<Button-1>", some_callback)
e.pack()

myButton    =   Button(root, text='Submit',fg='Red', bg='gray', command=myClick)
myButton.pack()

root.mainloop()