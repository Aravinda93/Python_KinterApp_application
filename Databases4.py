from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('DropDowns')
root.iconbitmap('./Icon_File.ico')
root.geometry('400x600')

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
    query_label.grid(row=14, column=0, columnspan=2)

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

def update():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute(""" UPDATE address SET
                     first_name  = :first,
                     last_name   = :last,
                     address     = :address,
                     city        = :city,
                     state       = :state,
                     zipcode     = :zipcode
                     WHERE oid   = :oid """,
                    {
                        'first'     :   f_name_editor.get(),
                        'last'      :   l_name_editor.get(),
                        'address'   :   address_editor.get(),
                        'city'      :   city_editor.get(),
                        'state'     :   state_editor.get(),
                        'zipcode'   :   zipcode_editor.get(),
                        'oid'       :   delete_box.get()

                    })
    conn.commit()
    conn.close()
    editor.destroy()


#Create a Edit function to update record
def edit():
    global editor
    editor = Tk()
    editor.title('DropDowns')
    editor.geometry('400x400')
    f_name_label = Label(editor, text='First Name')
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text='Last Name')
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text='Address')
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text='City')
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text='State')
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text='Zipcode')
    zipcode_label.grid(row=5, column=0)

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    submit_button = Button(editor, text='Modify Record', command=update)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM address WHERE oid = "+delete_box.get())
    records = cur.fetchall()
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0,record[5])
    conn.commit()
    conn.close()




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
delete_box_label = Label(root, text='Select Id')
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

#Create an UpDtae button
edit_button = Button(root, text='Edit Record', command=edit)
edit_button.grid(row=13, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

root.mainloop()