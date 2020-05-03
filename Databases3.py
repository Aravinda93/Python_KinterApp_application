from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('DropDowns')
root.iconbitmap('./Icon_File.ico')

#creating a database or connecting
#conn    =   sqlite3.connect('address_book.db')

#Create a cursor
#cur     =   conn.cursor()

#creating a table

#cur.execute(""" CREATE TABLE address(
#                    first_name  text,
#                    last_name   text,
#                    address     text,
#                    city        text,
#                    state       text,
#                    zipcode     integer
#                )
#           """)

#submit function
def submit():
    #clear the text box
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO address VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                    {
                        'f_name'    : f_name.get(),
                        'l_name'    : l_name.get(),
                        'address'   : address.get(),
                        'city'      : city.get(),
                        'state'     : state.get(),
                        'zipcode'   : zipcode.get()

                    }
                )
    conn.commit()
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0,END)

#query to find the records
def query():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("SELECT *,oid FROM address")
    records = cur.fetchall()
    print_records = ''

    #loop through all results
    for record in records:
        print_records += str(record[0]) +'\t'+str(record[1]) + '\t' + str(record[6]) +"\n"

    query_label = Label(root,text=print_records)
    query_label.grid(row=13, column=0, columnspan=2)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM address WHERE oid = "+delete_box.get())
    conn.commit()
    conn.close()
    delete_label = Label(root,text='Record Deleted')
    delete_label.grid(row=12, column=0, columnspan=2)
    delete_box.delete(0, END)


f_name = Entry(root,width=30)
f_name.grid(row=0,column=1, padx=20, pady=(10,0))

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1)

address = Entry(root,width=30)
address.grid(row=2,column=1)

city = Entry(root,width=30)
city.grid(row=3,column=1)

state = Entry(root,width=30)
state.grid(row=4,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=5,column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=10, column=1, pady=5)

#create text box label
f_name_label = Label(root, text='First Name')
f_name_label.grid(row=0, column=0,pady=(10,0))
l_name_label = Label(root, text='Last Name')
l_name_label.grid(row=1, column=0)
address_label = Label(root, text='Address')
address_label.grid(row=2, column=0)
city_label = Label(root, text='City')
city_label.grid(row=3, column=0)
state_label = Label(root, text='State')
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text='Zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text='Delete Id')
delete_box_label.grid(row=10, column=0, pady=5)


#create Submit button
submit_button = Button(root, text='Add Record', command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#query button
query_button = Button(root, text='Show Records', command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Delete button
delete_button = Button(root, text='Delete Record', command=delete)
delete_button.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()