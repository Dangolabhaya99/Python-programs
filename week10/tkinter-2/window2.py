from tkinter import *
from tkinter import ttk # Combobox
from PIL import ImageTk, Image
class Window2():
    def __init__(self):
        window =Tk()
        window.title("Window 10")
        window.geometry("700x700")
        window.resizable(False,False)

        # Add Label
        lblCollege = Label(window, text="PCPS College")
        lblCollege.place(x=20, y=20)

        # Add Entry - text box - single line
        txtName = Entry(window,width=20)
        txtName.place(x=20, y=50)

        # Add Password box
        txtPass = Entry(window, width=20, show="#")
        txtPass.place(x=20,y=80)

        #text - Comment box/Text Area
        txtComments = Text(window, width=30,height=3)
        txtComments.place(x=20, y=140)

        # Radiobutton - Single selstion from multiple options
        rb1 = Radiobutton(window, text="Opera",value='v1')
        rb2 = Radiobutton(window, text="Chrome",value='v2')
        rb1.place(x=20, y=200)
        rb2.place(x=20, y=250)

        # Checkbutton - Check box (SElect multiple values from multiple option
        ck1 = Checkbutton(window, text="Neutron")
        ck2 = Checkbutton(window, text="Electron")
        ck3 = Checkbutton(window, text="Proton")
        ck1.place(x=20, y=280)
        ck2.place(x=20, y=320)
        ck3.place(x=20, y=360)

        cmb1 = ttk.Combobox(window)
        cmb1['values'] = ('Top', 'Middle', 'Down')
        cmb1.place(x=20, y=400)

        # Canvas - Image Viewer
        # pip install pillow
        # from PIL import ImageTk, Image

        tmpImage= Image.open('Untitled.png')
        imgFile = ImageTk.PhotoImage(tmpImage)
        canvas = Canvas(window, width=150, height=50)
        canvas.create_image(0,0, image=imgFile)
        canvas.place(x=20, y=450)

        # Button
        btnSave = Button(window, text="SAVE")
        btnSave.place(x=20,y=450)

        window.mainloop()