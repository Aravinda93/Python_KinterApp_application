from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Windows')
root.iconbitmap('./Icon_File.ico')

def browser():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir='./', title='Select a File',
                                               filetypes=(('png files', '*.png'), ('All Files', '*.*')))
    mylabel = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).pack()

Button(root, text='Browse Files', command=browser).pack()

root.mainloop()