from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Data Table Demo")
window.geometry("500x300")
window.resizable(False, False)

frame1 = Frame(window)
frame1.pack()

tblPersons = ttk.Treeview(frame1)
tblPersons['columns']=('pid','name','address')

tblPersons.column("#0",width=0, stretch=NO)
tblPersons.column("pid",width=50, anchor=CENTER)
tblPersons.column("name",width=100, anchor=CENTER)
tblPersons.column("address",width=150, anchor=CENTER)

tblPersons.heading("#0",text="", anchor=CENTER)
tblPersons.heading("pid",text="ID", anchor=CENTER)
tblPersons.heading("name",text="NAME", anchor=CENTER)
tblPersons.heading("address",text="ADDRESS", anchor=CENTER)

tblPersons.insert(parent='',index='end',iid=2,
                  values=(1, 'Abhaya Dangol','Chandragiri'))
tblPersons.insert(parent='',index='end',iid=3,
                  values=(2, 'Dangol','Chandragiri'))
tblPersons.pack()

window.mainloop()