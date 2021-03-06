from tkinter import *
from PIL import ImageTk,Image
import glob

root    =   Tk()
root.title('Image Viewer')
root.iconbitmap('./images')

image_list = []
for filename in glob.glob('./Images/*.png'):
    im=ImageTk.PhotoImage(Image.open(filename))
    image_list.append(im)

my_label    =   Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_id):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_id - 1])
    button_forward  = Button(root, text='>', command= lambda:forward(image_id + 1))
    button_back     = Button(root, text='<', command= lambda:backward(image_id - 1))

    if(image_id == len(image_list)-1 ):
        button_forward = Button(root, text='>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

def backward(image_id):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_id - 1])
    button_forward = Button(root, text='>', command=lambda: forward(image_id + 1))
    button_back = Button(root, text='<', command=lambda: backward(image_id - 1))

    if (image_id == 1):
        button_back = Button(root, text='<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back     =   Button(root,text='<', command = backward, state=DISABLED)
button_exit     =   Button(root,text='X', command = root.quit)
button_forward  =   Button(root,text='>', command = lambda : forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()