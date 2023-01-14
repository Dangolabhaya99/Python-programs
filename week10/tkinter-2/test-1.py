import tkinter
from tkinter import *

window = Tk()
window.title("Windows-1")
window.geometry("400x400")
window.resizable(False, False)
v = tkinter.IntVar()
variable = StringVar(window)
variable.set("January") # default value

lblPCPS = Label(window, text="PCPS College")
lblPassword = Label(window, text="Password")
lblTextBox = Label(window, text="Message")
lblRadio = Label(window, text="Radio")
lblCheck = Label(window, text="Check Box")
lblDrop = Label(window, text="Month")

txtPCPS = Entry(window, width=30)
txtPassword = Entry(window, show="*", width=30)
txtTextBox = Text(window, height=4, width=22)
txtTextBox.pack()
txtRadio = Radiobutton(window, text="Yes", value=1)
txtRadio1 = Radiobutton(window, text="No", value=2)
txtCheck = Checkbutton(window, text="Option1")
txtCheck1 = Checkbutton(window, text="Option2")
txtDrop = OptionMenu(window, variable, "January", "February", "March")
txtDrop.pack()

lblPCPS.place(x=20, y=10)
txtPCPS.place(x=100, y=10)

lblPassword.place(x=20, y=40)
txtPassword.place(x=100, y=40)

lblTextBox.place(x=20, y=70)
txtTextBox.place(x=100, y=70)

lblRadio.place(x=20, y=150)
txtRadio.place(x=100, y=150)
txtRadio1.place(x=150, y=150)

lblCheck.place(x=20, y=180)
txtCheck.place(x=100, y=180)
txtCheck1.place(x=180, y=180)

lblDrop.place(x=20, y=210)
txtDrop.place(x=100, y=210)

window.mainloop()
