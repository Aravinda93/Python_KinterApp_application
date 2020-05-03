from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons, Images and Exit')
root.iconbitmap('./Icon_File.ico')

myImg   =   ImageTk.PhotoImage(Image.open('./aravinda.jpeg'))
myLable =   Label(image=myImg)
myLable.pack()

button_Quit =   Button(root, text='Exit', command=root.quit)
button_Quit.pack()

root.mainloop()