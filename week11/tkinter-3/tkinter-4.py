from tkinter import *
from tkinter import messagebox

window = Tk() # declare and initialize
window.title("Validation Test")
window.geometry("450x300")
window.resizable(False,False)

def save():
    # read text from box
    strID = txtID.get()
    if strID.isnumeric():
        tmpID = int(strID) # String to int
        if tmpID>=1 and tmpID<=99:
            messagebox.showinfo("Title","Valid ID")
        else:
            messagebox.showinfo("Title","Invalid ID")
    else:
        messagebox.showinfo("Title","Invalid data type")

lblID = Label(window, text="ID : ")
lblID.place(x=20, y=20)

txtID = Entry(window, width=15)
txtID.place(x=35, y=20)

btnSave = Button(window, text="SAVE", command=save)
btnSave.place(x=75, y=75)

btnClose = Button(window, text="CLOSE")
btnClose.place(x=200, y=75)

window.mainloop() # display window