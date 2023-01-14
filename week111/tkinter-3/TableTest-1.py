# Table in Tkinter
from tkinter import *
from tkinter import ttk
from PersonManager import all

window = Tk()
window.title("Table in tkinter")
window.geometry("550x350")
window.resizable(False, False)

def displayAll():
    tableFrame = Frame(window)
    tableFrame.pack()

    tblPersons = ttk.Treeview(tableFrame)
    tblPersons['columns']=('pid', 'name', 'address')

    tblPersons.column("#0", width=0, stretch=NO)
    tblPersons.column("pid", width=50, anchor=CENTER)
    tblPersons.column("name", width=100, anchor=CENTER)
    tblPersons.column("address", width=100, anchor=CENTER)

    tblPersons.heading('#0', text='', anchor=CENTER)
    tblPersons.heading('pid', text='PID', anchor=CENTER)
    tblPersons.heading('name', text='NAME', anchor=CENTER)
    tblPersons.heading('address', text='ADDRESS', anchor=CENTER)
    # tblPersons.insert(parent='', index='end', iid=0, values=('1', 'Anil', 'KTM'))
    persons = all()
    for person in persons:
        tblPersons.insert(parent='', index='end', iid=person[0], values=(person[0], person[1], person[2]))
    tblPersons.pack()

displayAll()
window.mainloop()