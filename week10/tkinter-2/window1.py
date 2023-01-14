# Display a window with a button
import tkinter
from tkinter import *
from window2 import Window2

def displayWin2():
    Window2() # Call __init__() function
window =Tk()
window.title("Window-1")
window.geometry("500x500")
window.resizable(False,False)

btnbutton = Button(text="window 10", width=20,command=displayWin2)
btnbutton.place(x=300,y=450)


window.mainloop()