# pip install tk
import sys

# Import Library
from tkinter import Tk # Window
from tkinter import Label # Label
from tkinter import Entry # Text Box
from tkinter import Button # Button
from notebook import NoteBook
from notebookmanager import insert,search,edit,delete

def searchNotebook():
    # reading value from entry and send to library/middleware
    nid = int(txtNID.get())
    record = search(nid)
    if(record==None):
        print("Record Not Found")
        txtPrice['text']=record.getPrice()
    else:
        txtPages.delete(0, len(txtPages.get()))
        txtPages.insert(0, str(record[1]))
        txtPrice.delete(0, len(txtPrice.get()))
        txtPrice.insert(0, str(record[2]))
        print("Record Found!!")

def deleteNotebook():
    # read all values (nid,pagesand price)
    nid = int(txtNID.get())
    # send to edit
    result = delete(nid)
    if result == True:
        print("Record deleted")
    else:
        print("Error to delete")


# Decalre and initialize
window = Tk() # Declare window
window.geometry("250x200")
window.resizable(False, False)
window.title("Insert New Record")

lblNID = Label(window, text="NID: ")
lblPages = Label(window, text="PAGES: ")
lblPrice = Label(window, text="PRICE: ")

txtNID = Entry(window, width=20)
txtPages = Entry(window, width=20)
txtPrice = Entry(window, width=20)

btnSearch = Button(window, text="SEARCH", command=searchNotebook) # calling save function
btnDelete=Button(window, text="DELETE",command=deleteNotebook)

lblNID.place(x=20, y=10)
txtNID.place(x=100, y=10)

lblPages.place(x=20, y=40)
txtPages.place(x=100, y=40)

lblPrice.place(x=20, y=70)
txtPrice.place(x=100, y=70)

btnSearch.place(x=100, y=100)
btnDelete.place(x=150, y=100)

window.mainloop() # Display window


