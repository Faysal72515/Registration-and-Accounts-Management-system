from tkinter import *
from tkinter import messagebox
import os                          # os means operating system
root=Tk()
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Register & Login")
        self.root.geometry("1350x700+0+0")

        # =============================================Register Frame====================================================
        register_frame=LabelFrame(self.root,bd=2,relief=GROOVE,bg='pink')
        register_frame.place(x=900,y=10,width=400,height=500)

        username_r_label=Label(register_frame,text="Username*",bg="pink")
        username_r_label.place(x=50,y=10)

        username_r_entry=Entry(register_frame)
        username_r_entry.place(x=20,y=40)

        password_r_label = Label(register_frame, text="Password*", bg="pink")
        password_r_label.place(x=190, y=10)

        password_r_entry = Entry(register_frame,show="*")
        password_r_entry.place(x=160, y=40)

        #Label(register_frame, text="").pack()
        register_photo=PhotoImage(file='register.png')
        register_button=Button(register_frame,image=register_photo)
        register_button.place(x=300,y=40)




        # ==========================================Resister Frame END===================================================







#root=Tk()
s=Student(root)
root.mainloop()