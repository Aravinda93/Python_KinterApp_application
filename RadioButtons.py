from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('./Icon_File.ico')

#r = IntVar()
#r.set('2')

#Radiobutton(root,text='Option 1', variable=r, value=1, command= lambda: clicked(r.get())).pack()
#Radiobutton(root,text='Option 2', variable=r, value=2, command= lambda: clicked(r.get())).pack()

Toppings = [
    ("Margarita", "Margarita"),
    ("Cheese", "Cheese"),
    ("Onion", "Onion"),
    ("Mushroom", "Mushroom")
]

pizza = StringVar()
pizza.set("Margarita")

for text, topping in Toppings:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

#myLabel = Label(root, text=pizza.get())
#myLabel.pack()

myButton = Button(root, text='Click Me', command= lambda: clicked(pizza.get()))
myButton.pack()


root.mainloop()