# pip install tk
from tkinter import Tk # Window
from tkinter import Label# Label
from tkinter import Text
from tkinter import Checkbutton
from tkinter import Radiobutton
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Entry # Entry
from tkinter import Button # Button

# Declare and initialize
window = Tk()#declare and initialize
window.geometry("1360x768")# Resize
window.resizable(False,False)# resizable-> False
window.title("Main Door")

lblFID = Label(window, text="Welcome To")
lblSID = Label(window, text="Hamro Taxi Booking System")
lblTID = Label(window, text="CUSTOMER:")
lblFoID = Label(window, text="DRIVER:")
lblFiID = Label(window, text="User:")
lblSiID = Label(window, text="Password:")
lblSeID = Label(window, text="For Registration")
lblEID = Label(window, text="Click Here in ")

txtTID = Checkbutton(window,width=2)
txtFoID = Checkbutton(window,width=2)
txtFiID = Entry(window,width=20)
txtSiID = Entry(window,width=20,show="*")
txtPages = Entry(window,width=20)
txtPrice = Entry(window,width=20)

btnLogin = Button(window,text="LOGIN")
btnSignin = Button(window,text="SIGN UP")

lblFID.place(x=535, y=125)
lblSID.place(x=505, y=145)
lblTID.place(x=525, y=180)
lblFoID.place(x=525, y=195)
lblFiID.place(x=505, y=225)
lblSiID.place(x=505, y=245)
lblSeID.place(x=535, y=305)
lblEID.place(x=535, y=330)

txtTID.place(x=590, y=180)
txtFoID.place(x=590, y=195)
txtFiID.place(x=560, y=225)
txtSiID.place(x=560, y=245)

btnLogin.place(x=638, y=270)
btnSignin.place(x=634, y=320)

window.mainloop()# display

# Resize window
