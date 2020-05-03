from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('Check Box')
root.iconbitmap('./Icon_File.ico')
root.geometry('400x200')

def graph():
    housePrices =   np.random.normal(200000,2500,5000)
    plt.hist(housePrices, 50)
    plt.show()

myButton    =   Button(root, text='Graph Maker', command=graph())
myButton.pack()


root.mainloop()