from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('DropDowns')
root.iconbitmap('./Icon_File.ico')
root.geometry('600x600')

#creating a database or connecting
conn    =   sqlite3.connect('address_book.db')

#Create a cursor
cur     =   conn.cursor()

#creating a table
cur.execute(""" CREATE TABLE address(
                    first_name  text,
                    last_name   text,
                    address     text,
                    city        text,
                    state       text,
                    zipcode     integer 
                )
            """)

#commit the changes
conn.commit()

#close the connection
conn.close()

root.mainloop()