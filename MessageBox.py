from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Box')
root.iconbitmap('./Icon_File.ico')

#showinfo, showwarning

def popup():
   #messagebox.showinfo('This is my pop up', 'Hello aravinda')
    #messagebox.showwarning('This is my pop up', 'Hello aravinda')
   #messagebox.showerror('This is my pop up', 'Hello aravinda')
   #messagebox.askquestion('This is my pop up', 'Hello aravinda')
   #messagebox.askokcancel('This is my pop up', 'Hello aravinda')
   #messagebox.askyesno('This is my pop up', 'Hello aravinda')
   response = messagebox.askokcancel('This is my pop up', 'Hello aravinda')
   Label(root,text=response).pack()
   if(response == 1):
       Label(root, text='You clicked YES').pack()
   else:
       Label(root, text='You clicked NO').pack()

Button(root, text='PopUp', command=popup).pack()


root.mainloop()