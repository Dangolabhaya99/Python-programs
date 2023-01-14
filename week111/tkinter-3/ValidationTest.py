from tkinter import *
from tkinter import messagebox

def isNumeric(str1):
    if str1.isnumeric():
        return True
    else:
        return False
def strToInt(str1):
    return int(str1)
def checkRange(num1, num2, num3):
    if num1>=num2 and num1<=num3:
        return True
    else:
        return False
"""    
def save():
    tmpID = txtID.get()
    if tmpID.isnumeric(): # type
        if int(tmpID)>=1 and int(tmpID)<=99: # range
            print("Valid id")
        else:
            print("Out of range")
    else:
        print("Invalid data type")
"""

def save():
    tmpID = txtID.get()
    result1 = isNumeric(tmpID)
    if result1 == True:
        numID = strToInt(tmpID)
        result2 = checkRange(numID, 1, 100)
        if result2 == True:
            # print("Valid id")
            messagebox.showinfo("Title", "Valid ID")
        else:
            # print("Out of range")
            messagebox.showwarning("Title", "ID out of range")
    else:
        # print("Invalid type")
        messagebox.showerror("Title", "Invalid ID")

# Validation
    # Name
    # Address
    # Email
    # Telephone
    # URL (Website)
    # Mobile
    # Credit Card No
    # Amount
    # Other
window = Tk()
window.title("Basic Validation")
window.geometry("350x300")
window.resizable(False, False)

lblID = Label(window, text="ID : ")
txtID = Entry(window, width=15)
btnSave = Button(window, text="SAVE", command=save)

lblID.place(x=20, y=20)
txtID.place(x=75, y=20)
btnSave.place(x=75, y=50)

window.mainloop()

print(help(str))