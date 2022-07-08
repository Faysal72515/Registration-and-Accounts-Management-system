'''
Project name: Registration and Accounts Management system With (registration & Login or Sign-in & Sign-up System)
Creator: Faysal Sarder                        -----
Dept: Computer Science & Engineering
'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date
import face_recognition
import MySQLdb
import pymysql
import time
import os
import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog
import math


# ==================================forgot_password (Open and Save)=====================================
def exit_forgot():
    forgot = messagebox.askyesno(title="previous", message="Do you want to go previous page ")
    if forgot > 0:
        forgot_screen.destroy()
        return


global current_open_file
current_open_file = "no files"
def open_file():
    text_area.delete(1.0, END)
    open_file = filedialog.askopenfile(initialdir="\F", title="select file to open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    if open_file != None:
        for line in open_file:
            text_area.insert(END, line)
        current_open_file = open_file.name
        open_file.close()

def save_file():
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    text2save = text_area.get(1.0, END)
    current_open_file = f.name
    f.write(text2save)
    f.close()
    forgot_screen.destroy()

# ==================================forgot_password================================

def forgot_password():
    confirm=messagebox.askyesno(title="Agree or Not",message="Do you want to forgot  password ?\nAre you sure you want to continue?")
    if confirm >0:
        global forgot_screen
        forgot_screen = Toplevel(login_frame)
        forgot_screen.title("Forgot password")
        forgot_screen.geometry("600x300+350+10")
        #forgot_screen.resizable(False,False)

        global forgot_screen_frame
        forgot_screen_frame=LabelFrame(forgot_screen,bg="lime")
        forgot_screen_frame.place(x=5, y=5, width=590, height=290)

        #open_photo = PhotoImage(file='open.png')
        #open_button = Button(forgot_screen_frame, image=open_photo, activebackground="green")
        #open_button.place(x=50, y=50)

        #save_photo =PhotoImage(file='save-file.png')
        #save_button = Button(forgot_screen_frame, image=save_photo, activebackground="red")
        #save_button.place(x=250, y=50)

        open_button = Button(forgot_screen_frame,text="Open",font=("Times new roman",20,"bold"),bd=2,bg="tomato", activebackground="lime",command=open_file)
        open_button.pack(side=TOP,fill=X)
        save_button = Button(forgot_screen_frame, text="Save", font=("Times new roman", 20, "bold"),bd=2,bg="darkorange",activebackground="forestgreen",command=save_file)
        save_button.pack(side=BOTTOM,fill=X)
        back_button = Button(forgot_screen_frame, text="Back", font=("Times new roman", 10, "bold"), bd=2,pady=63,
                             bg="coral", activebackground="gold",command=exit_forgot)
        back_button.place(x=542,y=64)

        global text_area
        text_area = Text(forgot_screen,width=66,height=9,bd=2,bg="lightyellow")
        text_area.place(x=10,y=70)



# ===================================register_user==================================
def register_user():
    username_r_info =username_r_var.get()
    password_r_info =password_r_var.get()
    if username_r_info !="" and password_r_info!="":
        file = open(username_r_info, "w")
        file.write(username_r_info + "\n")
        file.write(password_r_info)
        file.close()

        username_r_entry.delete(0, END)
        password_r_entry.delete(0, END)

        messagebox.showinfo(title="Welcome",message="REGISTRATION SUCCESSFUL")
        #success_r_label=Label(register_frame, text="Registration Success", fg="blue",bg="pink",font=("calibri", 11))
        #success_r_label.place(x=90,y=80)
    elif username_r_info !="" and password_r_info =="":
        messagebox.showerror(title="Warring", message="Please enter password")
    elif username_r_info =="" and password_r_info !="":
        messagebox.showerror(title="Warring", message="Please enter username")
    else:
        messagebox.showerror(title="Warring",message="Give username and password")

# ==============================login_verify============================================

def login_verify():
    username1 = username_l_entry.get()
    password1 = password_l_entry.get()
    username_l_entry.delete(0, END)
    password_l_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            #print("success")
        else:
            password_not_recognised()
            #print("password not recognised")
    else:
        user_not_found()
        #print("user not found")

# =========================================login_success=======================================================
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_frame)
    login_success_screen.title("Management")
    login_success_screen.geometry("1350x700+0+0")
    #Label(login_success_screen, text="Login Success").pack()
    # Button(login_success_screen, text="OK", command=delete_login_success).pack()

    title=Label(login_success_screen,text="Management System",bd=3,relief=GROOVE,font=("Time new Roman",14,"bold"),bg="yellow",fg='blue')
    title.pack(side=TOP,fill=X)
   #=======================================================Manage_Frame======================================
    global Manage_Frame
    Manage_Frame = Frame(login_success_screen, bd=4, relief=RIDGE, bg="cyan")
    Manage_Frame.place(x=20, y=40, width=400, height=500)
    global Id_var
    global Name_var
    global Gender_var
    global Department_var
    Id_var = StringVar()
    Name_var = StringVar()
    Gender_var = StringVar()
    Department_var=StringVar()

    m_title = Label(Manage_Frame, bg="cyan", fg="red", text="Manage Student", font=("arial",20, "bold"))
    m_title.grid(row=0, columnspan=2, pady=2)

    labl_id = Label(Manage_Frame, bg="cyan", fg="red", text="ID No.", font=("arial", 10, "bold"))
    labl_id.grid(row=1, column=0, padx=10, pady=20, sticky="w")

    txt_id = Entry(Manage_Frame, textvariable=Id_var, font=("arial", 10, "bold"), bd=2, relief=GROOVE)
    txt_id.grid(row=1, column=1, padx=10, pady=20, sticky="w")

    lbl_name = Label(Manage_Frame, bg="cyan", fg="red", text="Name.", font=("arial", 10, "bold"))
    lbl_name.grid(row=2, column=0, padx=10, pady=20, sticky="w")

    txt_name = Entry(Manage_Frame, textvariable=Name_var, font=("arial", 10, "bold"), bd=2, relief=GROOVE)
    txt_name.grid(row=2, column=1, padx=10, pady=20, sticky="w")

    lbl_gender = Label(Manage_Frame, bg="cyan", fg="red", text="Gender", font=("arial", 10, "bold"))
    lbl_gender.grid(row=3, column=0, padx=10, pady=20, sticky="w")

    combo_gender = ttk.Combobox(Manage_Frame,textvariable=Gender_var, font=("arial", 7, "bold"),state='readonly')
    combo_gender['values'] = ["Male", "Female", "Other"]
    combo_gender.set("select")
    #gender_var.set("select")
    combo_gender.grid(row=3,column=1,padx=3,pady=5,sticky="w")

    lbl_department = Label(Manage_Frame, bg="cyan", fg="red", text="Dept.", font=("arial", 10, "bold"))
    lbl_department.grid(row=4, column=0, padx=10, pady=20, sticky="w")

    txt_department = Entry(Manage_Frame, textvariable=Department_var, font=("arial", 10, "bold"), bd=2, relief=GROOVE)
    txt_department.grid(row=4, column=1, padx=10, pady=20, sticky="w")

    # ======================================Button_Frame===========================================
    btn_Frame = Frame(login_success_screen, bd=4, relief=RIDGE, bg="green")
    btn_Frame.place(x=10, y=470, width=410)

    Addbtn = Button(btn_Frame, text="Add", width=10,activebackground="yellow",command=add_students).grid(row=0, column=0, padx=10, pady=10)
    updatebtn = Button(btn_Frame, text="Update",bg="blue", fg="white", width=10,command=update_data).grid(row=0, column=1, padx=10, pady=10)
    deletebtn = Button(btn_Frame, text="Delete",bg="red",fg="white",  width=10,command=delete_data).grid(row=0, column=2, padx=10, pady=10)
    clearbtn = Button(btn_Frame, text="Clear", width=10,activebackground="yellow",command=clear ).grid(row=0, column=3, padx=10, pady=10)

    # ======================================Button===========================================
    Accountsbtn = Button(login_success_screen, text="Accounts", width=10,bg='green', fg="white", activebackground="yellow", command=accunt)
    Accountsbtn.place(x=60,y=600)
    Morebtn = Button(login_success_screen, text="Students", bg="hotpink", fg="white", width=10, command=more_attendance)
    Morebtn.place(x=160, y=600)
    exitbtn = Button(login_success_screen, text="previous", bg="blue", fg="white", width=10, command=iExit)
    exitbtn.place(x=260, y=600)

    main_exitbtn = Button(login_success_screen, text="Quit", bg="maroon", activebackground="red", fg="white", width=10, command=all_exit)
    main_exitbtn.place(x=1220, y=650)


    # ======================================Detail_Frame============================
    global Detail_Frame
    Detail_Frame = Frame(login_success_screen, bd=4, relief=RIDGE, bg="gray")
    Detail_Frame.place(x=500, y=40, width=800, height=580)

    #global search_by_var
    global search_txt_var
    #search_by_var = StringVar()
    #search_by_var.set("Select")
    search_txt_var = StringVar()

    lbl_search = Label(Detail_Frame, bg="gray", fg="white", text="Search by name", font=("arial", 20, "bold"))
    lbl_search.grid(row=0, column=0, padx=10, pady=20, sticky="w")

    #contents1 = ['Roll_no', 'Name']
    #menubutton_search = OptionMenu(Detail_Frame,search_by_var, *contents1)
    #menubutton_search.grid(row=0, column=1, padx=20, pady=10)

    # combo_search = ttk.Combobox(Detail_Frame,width=10,textvariable=self.search_by_var, font=("arial", 10, "bold"), state='readonly')
    # combo_search['values'] = ["Roll_no", "Name"]
    # combo_search.set("select")
    # combo_search.grid(row=0, column=1, padx=20, pady=10)

    txt_Search = Entry(Detail_Frame, width=20, textvariable=search_txt_var, font=("arial", 10, "bold"), bd=5,relief=GROOVE)
    txt_Search.grid(row=0, column=2, padx=10, pady=20, sticky="w")

    searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5,command=search_data).grid(row=0, column=3, padx=10, pady=10)
    showbtn = Button(Detail_Frame, text="Show", width=10, pady=5,command=fetch_data).grid(row=0, column=4, padx=10, pady=10)


    # =======================================Table Frame=======================================
    Table_frame= Frame(Detail_Frame, bd=4, relief=RIDGE, bg="gray")
    Table_frame.place(x=10, y=70, width=760, height=500)

    scroll_x=Scrollbar(Table_frame,orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
    global Student_table
    Student_table=ttk.Treeview(Table_frame,columns=("Roll","Name","Gender","Dept."),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table.xview)
    scroll_y.config(command=Student_table.yview)

    Student_table.heading("Roll",text="ID No")
    Student_table.heading("Name", text="Name")
    Student_table.heading("Gender", text="Gender")
    Student_table.heading("Dept.", text="Dept.")
    Student_table['show']='headings'
    Student_table.column('Roll',width=150)
    Student_table.column('Name', width=150)
    Student_table.column('Gender', width=150)
    Student_table.column('Dept.', width=150)
    Student_table.pack(fill=BOTH,expand=1)
    Student_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()


#=======================================add_students==========================================================

def add_students():
    if Id_var.get() == "" or Name_var.get() == "" or Gender_var.get() == "" or Department_var.get()=="":
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="varsity_management")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s)", (Id_var.get(),
                                                                 Name_var.get(),
                                                                 Gender_var.get(),
                                                                 Department_var.get()

                                                              ))
        con.commit()
        fetch_data()
        clear()
        con.close()


def fetch_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity_management")
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    if len(rows) != 0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('', END, values=row)
        con.commit()
    con.close()

def clear():
    Id_var.set("")
    Name_var.set("")
    Gender_var.set("")
    Department_var.set("")


def get_cursor(s):
    cursor_row = Student_table.focus()
    contents = Student_table.item(cursor_row)
    row = contents['values']
    Id_var.set(row[0])
    Name_var.set(row[1])
    Gender_var.set(row[2])
    Department_var.set(row[3])


def update_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity_management")
    cur = con.cursor()
    cur.execute("update  students set name=%s,gender=%s,dept=%s where id_no=%s", (
                                                                                 Name_var.get(),
                                                                                 Gender_var.get(),
                                                                                 Department_var.get(),
                                                                                 Id_var.get()

    ))
    con.commit()
    fetch_data()
    clear()
    con.close()


def delete_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity_management")
    cur = con.cursor()
    cur.execute("delete from students where id_no=%s", Id_var.get())
    con.commit()
    con.close()
    fetch_data()
    clear()


def search_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity_management")
    cur = con.cursor()
    sql_query = "Select * from students where name=%s "
    vals = ((search_txt_var.get()))
    #cur.execute("select * from students where"+ str(search_txt_var.get()))
    cur.execute(sql_query, vals)
    rows = cur.fetchall()
    if len(rows) != 0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('', END, values=row)
        con.commit()
    con.close()

# =========================================Third window==============================================================================

def iExit():
    iExit = messagebox.askyesno(title="previous", message="Do you want to go Login page ")
    if iExit > 0:
        login_success_screen.destroy()
        return

def all_exit():
    all_exit = messagebox.askyesno(title="Close", message="Do you want to go close all program ")
    if all_exit > 0:
        root.destroy()
        return



def more_attendance():
    global more_screen
    more_screen = Toplevel(login_success_screen)
    more_screen.title("Attendance")
    more_screen.geometry("1350x700+0+0")

    global font_size
    global name3_var
    global time_var
    global date_var
    name3_var = StringVar()
    time_var = StringVar()
    date_var = StringVar()
    font_size = ("arial", 15, "bold")

    # ==============================================Routines===================================================
    global code_var
    global day_var
    global date_time_var
    code_var = StringVar()
    day_var = StringVar()
    date_time_var = StringVar()

    routine_label = Label(more_screen, text="Routine", font=font_size, fg="white", bg="yellow")
    routine_label.place(x=100, y=250)

    routine_label1 = Label(more_screen, text="Course Code*", fg="black")
    routine_label1.place(x=100, y=300)
    course_code_entry = Entry(more_screen, bg="white", textvariable=code_var)
    course_code_entry.place(x=80, y=330)

    routine_label2 = Label(more_screen, text="Day*", fg="black")
    routine_label2.place(x=120, y=360)
    day_entry = Entry(more_screen, bg="white", textvariable=day_var)
    day_entry.place(x=80, y=390)

    routine_label3 = Label(more_screen, text="Date & Time*", fg="black")
    routine_label3.place(x=100, y=420)
    date_entry = Entry(more_screen, bg="white", textvariable=date_time_var)
    date_entry.place(x=80, y=440)


    add_routine_button = Button(more_screen, text="Add", bg="lightgray", activebackground="yellow", command=add_students_5)
    add_routine_button.place(x=80, y=480)
    delete_routine_button = Button(more_screen, text="Delete", bg="lightgray", activebackground="red", command=delete_data_2)
    delete_routine_button.place(x=120, y=480)

    # ==============================================course===================================================
    global course_var
    course_var=StringVar()

    course_label= Label(more_screen, text="course", font=font_size, fg="white", bg="yellow")
    course_label.place(x=1030, y=250)

    course_label1 = Label(more_screen, text="Course Name:", fg="black")
    course_label1.place(x=900, y=300)

    add_course_entry = Entry(more_screen, bg="white", textvariable=course_var)
    add_course_entry.place(x=1000, y=300)

    add_course_button = Button(more_screen, text="Add", bg="lightgray", activebackground="yellow", command=add_students_4)
    add_course_button.place(x=1150, y=300)
    delete_course_button = Button(more_screen, text="Delete", bg="lightgray", activebackground="red", command=delete_data_1)
    delete_course_button.place(x=1200, y=300)

    Table_frame_more_course = Frame(more_screen, bd=4, relief=RIDGE, bg="gray")
    Table_frame_more_course.place(x=900, y=350, width=430, height=200)

    scroll_x = Scrollbar(Table_frame_more_course, orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_frame_more_course, orient=VERTICAL)
    global Student_table_course
    Student_table_course = ttk.Treeview(Table_frame_more_course, columns=("course"), xscrollcommand=scroll_x.set,
                                      yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table_course.xview)
    scroll_y.config(command=Student_table_course.yview)

    Student_table_course.heading("course", text="Course Title")
    Student_table_course['show'] = 'headings'
    Student_table_course.column('course', width=150)
    Student_table_course.pack(fill=BOTH, expand=1)
    Student_table_course.bind("<ButtonRelease-1>", get_cursor_4)
    fetch_data_4()


    # ==============================================attend===================================================
    attend_label= Label(more_screen, text="Attendance & Course", bg="yellow")
    attend_label.pack(side=TOP, fill=X)
    name_label = Label(more_screen, text="Name:", font=font_size, fg="black")
    name_label.place(x=325, y=70)
    time_label = Label(more_screen, text="Time:", font=font_size, fg="black")
    time_label.place(x=325, y=120)
    date_label = Label(more_screen, text="Date:", font=font_size, fg="black")
    date_label.place(x=325, y=170)

    video_capture_button = Button(more_screen, text="VideoRec", bg="hotpink", activebackground="pink", command=webdetRec)
    video_capture_button.place(x=80, y=25)
    captured_button = Button(more_screen, text="Capture", font=("arial", 15, "bold"), bg="lime", activebackground="red",
                             width=33, command=press_captured)
    captured_button.place(x=320, y=20)
    add_button = Button(more_screen, text="Add", font=("arial", 12, "bold"), fg="white", bg="greenyellow", activebackground="blue",
                        width=10, command=add_students3)
    add_button.place(x=600, y=70)
    clear_button = Button(more_screen, text="Clear", font=("arial", 12, "bold"), fg="white", bg="red", width=10, command=clear_press)
    clear_button.place(x=600, y=120)

    previous_button = Button(more_screen, text="Previous", font=("arial", 12, "bold"), fg="white", bg="darkred", width=10,
                         command=iprevious)
    previous_button.place(x=600, y=170)
    exit_button = Button(more_screen, text="Quit", font=("arial", 12, "bold"), fg="white", bg="black", width=10,
                         command=iExit3)
    exit_button.place(x=1050, y=650)

    name_entry = Entry(more_screen, bd=4, textvariable=name3_var, width=15, bg="white", font=font_size)
    name_entry.place(x=410, y=70)
    time_entry = Entry(more_screen, bd=4, width=15, textvariable=time_var, bg="white", font=font_size)
    time_entry.place(x=410, y=120)
    date_entry = Entry(more_screen, bd=4, width=15, textvariable=date_var, bg="white", font=font_size)
    date_entry.place(x=410, y=170)

    Table_frame_more = Frame(more_screen, bd=4, relief=RIDGE, bg="gray")
    Table_frame_more.place(x=250, y=250, width=600, height=350)

    scroll_x = Scrollbar(Table_frame_more, orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_frame_more, orient=VERTICAL)
    global Student_table_more
    Student_table_more = ttk.Treeview(Table_frame_more, columns=("Name", "Time", "Date"), xscrollcommand=scroll_x.set,
                                 yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table_more.xview)
    scroll_y.config(command=Student_table_more.yview)

    Student_table_more.heading("Name", text="Name")
    Student_table_more.heading("Time", text="Time")
    Student_table_more.heading("Date", text="Date")
    Student_table_more['show'] = 'headings'
    Student_table_more.column('Name', width=150)
    Student_table_more.column('Time', width=150)
    Student_table_more.column('Date', width=150)
    Student_table_more.pack(fill=BOTH, expand=1)
    Student_table_more.bind("<ButtonRelease-1>", get_cursor3)
    fetch_data3()

    # ===========================================routine table============================================================
    Table_frame_routine = Frame(more_screen, bd=2, relief=RIDGE)
    Table_frame_routine.place(x=20, y=510, width=210, height=150)

    scroll_x = Scrollbar(Table_frame_routine, orient=HORIZONTAL)
    scroll_y = Scrollbar(Table_frame_routine, orient=VERTICAL)
    global Student_table_routine
    Student_table_routine = ttk.Treeview(Table_frame_routine, columns=("course_code", "day", "date&time"),
                                         xscrollcommand=scroll_x.set,
                                         yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)
    scroll_x.config(command=Student_table_routine.xview)
    scroll_y.config(command=Student_table_routine.yview)

    Student_table_routine.heading("course_code", text="Course Code")
    Student_table_routine.heading("day", text="Day")
    Student_table_routine.heading("date&time", text="Date & Time")
    Student_table_routine['show'] = 'headings'
    Student_table_routine.column('course_code', width=100)
    Student_table_routine.column('day', width=100)
    Student_table_routine.column('date&time', width=100)
    Student_table_routine.pack(fill=BOTH, expand=1)
    Student_table_routine.bind("<ButtonRelease-1>", get_cursor_5)
    fetch_data_5()


    # =============================clock============================================
    cframe = Frame(more_screen, width=50, height=30, bg='green', relief=GROOVE)
    cframe.place(x=1000, y=5)

    clock = Label(cframe, padx=5, pady=20, bd=3, fg='dark green', font=('arial', 15, 'bold'), text=timenow,
                  bg='light green', relief=SUNKEN)
    clock.pack()

    def tick():
        global timenow
        newtime = time.strftime('%H: %M: %S %p')
        if newtime != timenow:
            timenow = newtime
            clock.config(text=timenow)
        clock.after(200, tick)

    tick()
    global today
    today = date.today()
    date_label = Label(more_screen, padx=18, pady=5, fg='dark green', font=('arial', 15, 'bold'), text=today, bg='light green',
                       relief=SUNKEN)
    date_label.place(x=1000, y=73)

def iprevious():
        more_screen.destroy()
        return

def iExit3():
    iExit = messagebox.askyesno(title="Exit or not", message="Do you want to exit??")
    if iExit > 0 :
        root.destroy()
        return


def add_students3():
    if name3_var.get() == " " or time_var.get() == " " or date_var.get() == "" :
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con =MySQLdb.connect("localhost", "root", "", "captured")
        cur = con.cursor()
        cur.execute("insert into students_info values(%s,%s,%s)", (name3_var.get(),
                                                                   time_var.get(),
                                                                   date_var.get()


                                                              ))
        con.commit()
        fetch_data3()
        clear_press()
        con.close()





def fetch_data3():
    con = MySQLdb.connect("localhost", "root", "", "captured")
    cur = con.cursor()
    cur.execute("select * from students_info ")
    rows = cur.fetchall()
    if len(rows) != 0:
        Student_table_more.delete(*Student_table_more.get_children())
        for row in rows:
            Student_table_more.insert('', END, values=row)
        con.commit()
    con.close()

def clear_press():
    name3_var.set("")
    time_var.set("")
    date_var.set("")

def get_cursor3(s):
    cursor_row = Student_table_more.focus()
    contents = Student_table_more.item(cursor_row)
    row = contents['values']
    name3_var.set(row[0])
    time_var.set(row[1])
    date_var.set(row[2])


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("Messenger.mp4")
global timenow
timenow = ''


def press_captured():
    while cap.isOpened():
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

        # display the output
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

    # =========================captured===========================
    if cap.isOpened():
        ret, frame = cap.read()
        #print(ret)
        #print(frame)
        messagebox.showinfo(title="Congress", message=" Photo captured")
        time_var.set(timenow)
        date_var.set(today)

    else:
        ret = False
        messagebox.showinfo(title="Error", message=" Photo captured Failed")

    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    plt.imshow(img1)
    plt.title("photo")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    cap.release()
    cv2.destroyAllWindows()


def webdetRec():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    op = cv2.VideoWriter('Sample2.avi', fourcc, 9.0, (640, 480))

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eye_g = eye_glass.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_g:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        op.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('a'):
            break
    op.release()
    capture.release()
    cv2.destroyAllWindows()



# ============================================database connect for course==================================================
def add_students_4():
    if course_var.get() == " ":
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="subjects")
        cur = con.cursor()
        cur.execute("insert into sub values(%s)", (course_var.get()))
        con.commit()
        fetch_data_4()
        clear_press_1()
        con.close()


def fetch_data_4():
    con_1 = pymysql.connect(host="localhost", user= "root", password="",database="subjects")
    cur_1 = con_1.cursor()
    cur_1.execute("select * from sub ")
    rows_1 = cur_1.fetchall()
    if len(rows_1) != 0:
        Student_table_course.delete(*Student_table_course.get_children())
        for row_1 in rows_1:
            Student_table_course.insert('', END, values=row_1)
        con_1.commit()
    con_1.close()



def clear_press_1():
    course_var.set("")


def get_cursor_4(s):
    cursor_rows = Student_table_course.focus()
    contents = Student_table_course.item(cursor_rows)
    row = contents['values']
    course_var.set(row[0])


def delete_data_1():
    con = pymysql.connect(host="localhost",user="root", password="",database="subjects")
    cur = con.cursor()
    cur.execute("delete from sub where name=%s", course_var.get())
    con.commit()
    con.close()
    fetch_data_4()
    clear_press_1()




# ============================================database connect for routine==================================================
def add_students_5():
    if code_var.get() == " " or day_var.get() == "" or date_time_var.get == "":
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="Daily_Routine")
        cur = con.cursor()
        cur.execute("insert into subs values(%s, %s, %s)", (code_var.get() ,day_var.get(), date_time_var.get() ))
        con.commit()
        fetch_data_5()
        clear_press_2()
        con.close()


def fetch_data_5():
    con_1 = pymysql.connect(host="localhost", user= "root", password="",database="Daily_Routine")
    cur_1 = con_1.cursor()
    cur_1.execute("select * from subs ")
    rows_1 = cur_1.fetchall()
    if len(rows_1) != 0:
        Student_table_routine.delete(*Student_table_routine.get_children())
        for row_1 in rows_1:
            Student_table_routine.insert('', END, values=row_1)
        con_1.commit()
    con_1.close()



def clear_press_2():
    code_var.set("")
    day_var.set("")
    date_time_var.set("")


def get_cursor_5(s):
    cursor_rows = Student_table_routine.focus()
    contents = Student_table_routine.item(cursor_rows)
    row = contents['values']
    code_var.set(row[0])
    day_var.set(row[1])
    date_time_var.set(row[2])


def delete_data_2():
    con = pymysql.connect(host="localhost",user="root", password="",database="Daily_Routine")
    cur = con.cursor()
    cur.execute("delete from subs where course_code=%s", code_var.get())
    con.commit()
    con.close()
    fetch_data_5()
    clear_press_2()


#====================================================================================================================

def accunt():                      #  Third widget (for Accountbtn )
    global accunt_screen
    accunt_screen = Toplevel(login_success_screen)
    accunt_screen.title("Accounts")
    accunt_screen.geometry("1350x700+0+0")

    hints_account_lable=Label(accunt_screen,bg="gray",fg="white",text="Hints: First you will finished the work of Installment_Fee Button then after \n that press Due & Paid Balance Button.")
    hints_account_lable.place(x=20,y=650)

    global Detail_accunt_Frame
    Detail_accunt_Frame = Frame(accunt_screen, bd=4, relief=RIDGE, bg="crimson")
    Detail_accunt_Frame.place(x=20, y=40, width=400, height=600)

    account_title = Label(accunt_screen, bg="gold",bd=3, fg="navy", text="Accounts & Money Info. (Dept. of BCSe)",font=("arial", 14, "bold"))
    account_title.pack(side=TOP,fill=X)

    global f_num
    global math

    def clicked(number):
        current = installment_account_entry.get()
        installment_account_entry.delete(0, END)
        installment_account_entry.insert(0, str(current) + str(number))

    def plus_button():
        first_number = installment_account_entry.get()
        global f_num
        global math
        math = "addition"
        f_num = float(first_number)
        installment_account_entry.delete(0, END)

    def minus_button():
        first_number = installment_account_entry.get()
        global f_num
        global math
        math = "subtraction"
        f_num = float(first_number)
        installment_account_entry.delete(0, END)

    def multy_button():
        first_number = installment_account_entry.get()
        global f_num
        global math
        math = "multiplication"
        f_num = float(first_number)
        installment_account_entry.delete(0, END)

    def divide_button():
        first_number = installment_account_entry.get()
        global f_num
        global math
        math = "division"
        f_num = float(first_number)
        installment_account_entry.delete(0, END)


    def summation():
        second_number = installment_account_entry.get()
        installment_account_entry.delete(0, END)

        if math == "addition":
            installment_account_entry.insert(0, f_num + float(second_number))

        if math == "subtraction":
            installment_account_entry.insert(0, f_num - float(second_number))

        if math == "multiplication":
            installment_account_entry.insert(0, f_num * float(second_number))

        if math == "division":
            installment_account_entry.insert(0, f_num / float(second_number))

    def new():
        item1 = semester_var.get()
        item2 = installment_var.get()
        if item1.isdigit() or item2.isdigit() :
            item3 =float(item1)
            item4 =float(item2)
            item = item3 - item4
            due_var.set(item)
            return True

    def new1():
        item2 = installment_var.get()
        item10 = paid_var.get()
        for i in item2:
            item4 = float(item2)
            item11=float(item10)
            item12=item11+item4
            paid_tuition_account_entry.delete(0,END)
            paid_tuition_account_entry.insert(0,item12)
            return True




        #if semester_account_entry.get()=="" or installment_account_entry.get()=="":
            #messagebox.showerror(title="Error",message="Please entry bill first")




    def iExit_account():
        iExit1 = messagebox.askyesno(title="previous", message="Do you want to go previous page ")
        if iExit1 > 0:
            accunt_screen.destroy()
            return



    global total_tuition_var
    global installment_var
    global due_var
    global name_cal_var
    global semester_var
    global paid_var
    operator=""
    semester_var=StringVar()
    name_cal_var=StringVar()
    total_tuition_var=StringVar()
    paid_var=StringVar()
    installment_var = StringVar()
    due_var=StringVar()


    name_account_label= Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Name", font=("arial", 10, "bold"))
    name_account_label.grid(row=0, column=0, padx=10, pady=20, sticky="w")

    name_account_entry= Entry(Detail_accunt_Frame, textvariable=name_cal_var, font=("arial", 10, "bold"), bd=2, relief=GROOVE)
    name_account_entry.grid(row=0, column=1, padx=10, pady=20, sticky="w")

    total_tuition_account_label = Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Total Tuition", font=("arial", 10, "bold"))
    total_tuition_account_label.grid(row=1, column=0, padx=10, pady=20, sticky="w")

    total_tuition_account_entry = Entry(Detail_accunt_Frame, textvariable=total_tuition_var, font=("arial", 10, "bold"), bd=2, relief=GROOVE)
    total_tuition_account_entry.grid(row=1, column=1, padx=10, pady=20, sticky="w")

    paid_tuition_account_label = Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Total Paid",
                                        font=("arial", 10, "bold"))
    paid_tuition_account_label.grid(row=2, column=0, padx=10, pady=20, sticky="w")

    paid_tuition_account_entry = Entry(Detail_accunt_Frame, textvariable=paid_var, font=("arial", 10, "bold"),
                                        bd=2, relief=GROOVE)
    paid_tuition_account_entry.grid(row=2, column=1, padx=10, pady=20, sticky="w")


    semester_account_label = Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Semester Fee",font=("arial", 10, "bold"))
    semester_account_label.grid(row=3, column=0, padx=10, pady=20, sticky="w")

    semester_account_entry = Entry(Detail_accunt_Frame, textvariable=semester_var, font=("arial", 10, "bold"),
                                        bd=2, relief=GROOVE)
    semester_account_entry.grid(row=3, column=1, padx=10, pady=20, sticky="w")

    installment_account_label = Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Installment Fee",font=("arial", 10, "bold"))
    installment_account_label.grid(row=4, column=0, padx=10, pady=20, sticky="w")

    installment_account_entry = Entry(Detail_accunt_Frame, textvariable=installment_var, font=("arial", 10, "bold"),bd=2, relief=GROOVE)
    installment_account_entry.grid(row=4, column=1, padx=10, pady=20, sticky="w")

    due_account_label = Label(Detail_accunt_Frame, bg="crimson", fg="white", text="Ins. Due", font=("arial", 10, "bold"))
    due_account_label.grid(row=5, column=0, padx=10, pady=20, sticky="w")

    due_account_entry = Entry(Detail_accunt_Frame, textvariable=due_var, font=("arial", 10, "bold"), bd=2,
                              relief=GROOVE)
    due_account_entry.grid(row=5, column=1, padx=10, pady=20, sticky="w")



    add_account_btn = Button(Detail_accunt_Frame, text="Add", width=11, pady=5,command=add_account_students)
    add_account_btn.place(x=10,y=370)
    clear_account_btn = Button(Detail_accunt_Frame, text="Clear", width=10, pady=5,command=clear_account)
    clear_account_btn.place(x=100, y=370)
    update_account_btn = Button(Detail_accunt_Frame, text="Update", width=10, pady=5,command=update_account_data)
    update_account_btn.place(x=180, y=370)
    delete_account_btn = Button(Detail_accunt_Frame, text="Delete", width=10, pady=5,command=delete_account_data)
    delete_account_btn.place(x=260, y=370)

    total_account_btn = Button(Detail_accunt_Frame,bg="cyan" ,text="Installment_Fee",padx=46, width=10, pady=5,command=summation)
    total_account_btn.place(x=10, y=420)
    due_account_btn = Button(Detail_accunt_Frame,bg="cyan", text="Due ", width=4, padx=22, pady=5, command=new)
    due_account_btn.place(x=180, y=420)
    paid_account_btn = Button(Detail_accunt_Frame, bg="cyan", text="Total Paid ", width=4, padx=20, pady=5,command=new1)
    paid_account_btn.place(x=260, y=420)



    plusbutton = Button(Detail_accunt_Frame,text="+",font=("arial", 14, "bold"),padx=30 , bg="white", activebackground="yellow",command=plus_button)
    plusbutton.place(x=10, y=470)
    minusbutton = Button(Detail_accunt_Frame, text="-", font=("arial", 14, "bold"), padx=29, bg="white", activebackground="yellow",command=minus_button)
    minusbutton.place(x=100, y=470)
    multybutton = Button(Detail_accunt_Frame, text="x", font=("arial", 14, "bold"), padx=25, bg="white",activebackground="yellow",command=multy_button)
    multybutton.place(x=180, y=470)
    devidebutton = Button(Detail_accunt_Frame, text="/", font=("arial", 14, "bold"), padx=30, bg="white",activebackground="yellow",command=divide_button)
    devidebutton.place(x=257, y=470)
    pointbutton = Button(Detail_accunt_Frame, text=".", padx=38, bg="cyan",activebackground="yellow",command=lambda :clicked('.'))
    pointbutton.place(x=10, y=520)

    exit_account_btn = Button(Detail_accunt_Frame, text="Back",activebackground="red", bg="cyan", fg="black",padx=80, width=10,command=iExit_account)
    exit_account_btn.place(x=100, y=520)



    global Frame_account_Frame        #=================================Frame_account_Frame===========================
    Frame_account_Frame = Frame(accunt_screen, bd=4, relief=RIDGE, bg="greenyellow")
    Frame_account_Frame.place(x=500, y=40, width=800, height=580)

    global search_txt_account_var
    search_txt_account_var=StringVar()
    lbl_account_search = Label(Frame_account_Frame, bg="greenyellow", fg="forestgreen", text="Search by name", font=("arial", 20, "bold"))
    lbl_account_search.grid(row=0, column=0, padx=10, pady=20, sticky="w")

    txt_account_Search = Entry(Frame_account_Frame, width=20, textvariable=search_txt_account_var, font=("arial", 10, "bold"), bd=5,relief=GROOVE)
    txt_account_Search.grid(row=0, column=2, padx=10, pady=20, sticky="w")

    search_account_btn = Button(Frame_account_Frame, text="Search", width=10, pady=5,command=search_account_data).grid(row=0, column=3, padx=10, pady=10)
    show_account_btn = Button(Frame_account_Frame, text="Show", width=10, pady=5,command=fetch_account_data).grid(row=0, column=4, padx=10,pady=10)


    Table_account_frame = Frame(Frame_account_Frame, bd=4, relief=RIDGE, bg="gray")# ==============Table Frame=============
    Table_account_frame.place(x=10, y=70, width=760, height=500)

    scroll_account_x = Scrollbar(Table_account_frame, orient=HORIZONTAL)
    scroll_account_y = Scrollbar(Table_account_frame, orient=VERTICAL)
    global Student_account_table
    Student_account_table=ttk.Treeview(Table_account_frame,columns=('name','tuition','paid','semester_fee','installment','due'), xscrollcommand=scroll_account_x.set,  yscrollcommand=scroll_account_y.set)
    #Student_account_table = ttk.Treeview(Table_account_frame, columns=("Name", "Total_Tuition","Semester_Fee", "Installment", "Due","Total_Paid"), xscrollcommand=scroll_account_x.set,  yscrollcommand=scroll_account_y.set)
    scroll_account_x .pack(side=BOTTOM, fill=X)
    scroll_account_y .pack(side=RIGHT, fill=Y)
    scroll_account_x .config(command=Student_account_table.xview)
    scroll_account_y .config(command=Student_account_table.yview)

    Student_account_table.heading("name", text="Name")
    Student_account_table.heading("tuition", text="Total_Tuition")
    Student_account_table.heading("paid", text="Paid")
    Student_account_table.heading("semester_fee", text="Semester_Fee")
    Student_account_table.heading("installment", text="Installment_Fee")
    Student_account_table.heading("due", text="Due")
    Student_account_table['show'] = 'headings'
    Student_account_table.column('name', width=150)
    Student_account_table.column('tuition', width=150)
    Student_account_table.column('paid', width=150)
    Student_account_table.column('semester_fee', width=150)
    Student_account_table.column('installment', width=150)
    Student_account_table.column('due', width=150)
    Student_account_table.pack(fill=BOTH, expand=1)
    Student_account_table.bind("<ButtonRelease-1>", get_account_cursor)
    fetch_account_data()

def add_account_students():
    if installment_var.get() > semester_var.get():
        messagebox.showerror(title="Error", message="Installment fee is greater than Semester fee, please try again !!!")
    elif total_tuition_var.get() == "" or paid_var.get() == "" or semester_var.get() == "" or installment_var.get() == "" or due_var.get()=="":
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="varsity")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s)", (
                                                                 name_cal_var.get(),
                                                                 total_tuition_var.get(),
                                                                 paid_var.get(),
                                                                 semester_var.get(),
                                                                 installment_var.get(),
                                                                 due_var.get()



                                                              ))
        con.commit()
        fetch_account_data()
        clear_account()
        con.close()



def fetch_account_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity")
    cur= con.cursor()
    cur.execute("select * from students")
    rowss = cur.fetchall()
    if len(rowss) != 0:
        Student_account_table.delete(*Student_account_table.get_children())
        for r in rowss:
            Student_account_table.insert('', END, values=r)
        con.commit()
    con.close()
def clear_account():
    name_cal_var.set("")
    total_tuition_var.set("")
    paid_var.set("")
    semester_var.set("")
    installment_var.set("")
    due_var.set("")



def get_account_cursor(a):
    cursor_row1 = Student_account_table.focus()
    contents1 = Student_account_table.item(cursor_row1)
    row1 = contents1['values']
    name_cal_var.set(row1[0])
    total_tuition_var.set(row1[1])
    paid_var.set(row1[2])
    semester_var.set(row1[3])
    installment_var.set(row1[4])
    due_var.set(row1[5])
def update_account_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity")
    cur = con.cursor()
    cur.execute("update  students set tuition=%s,paid=%s,semester_fee=%s,installment=%s,due=%s where name=%s", (
        total_tuition_var.get(),
        paid_var.get(),
        semester_var.get(),
        installment_var.get(),
        due_var.get(),
        name_cal_var.get(),

    ))
    con.commit()
    fetch_account_data()
    clear_account()
    con.close()





def delete_account_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity")
    cur = con.cursor()
    cur.execute("delete from students where name=%s", name_cal_var.get())
    con.commit()
    con.close()
    fetch_account_data()
    clear_account()

def search_account_data():
    con = pymysql.connect(host="localhost", user="root", password="", database="varsity")
    cur = con.cursor()
    sql_query1 = "Select * from students where name=%s "
    vals1 = ((search_txt_account_var.get()))
    #cur.execute("select * from students where"+ str(search_txt_var.get()))
    cur.execute(sql_query1, vals1)
    rows1 = cur.fetchall()
    if len(rows1) != 0:
        Student_account_table.delete(*Student_account_table.get_children())
        for r1 in rows1:
            Student_account_table.insert('', END, values=r1)
        con.commit()
    con.close()



# =====================================password_not_recognised===============================================================
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_frame)
    password_not_recog_screen.title("Error")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

# ==========================================user_not_found=======================================================
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_frame)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
# ========================================delete_login_success============================================

#def delete_login_success():
    #login_success_screen.destroy()

# ========================================delete_password_not_recognised============================================
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
# ========================================delete_user_not_found_screen============================================

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
#======================================================================================================================
#======================================================================================================================
def exit_main():
    exit_main = messagebox.askyesno(title="Quit", message=" Quit !!! ")
    if exit_main > 0:
        root.destroy()
        return

def Student():        # code start and 1st widget
    global root
    root = Tk()
    root.title("Register & Login")
    root.geometry("1350x700+0+0")
    root.iconbitmap(r'identifier.ico')
    # =================================exit root=======================================

    exit_photo = PhotoImage(file='signs.png')
    exit_root_button = Button(root, image=exit_photo, activebackground="red",command=exit_main)
    exit_root_button.place(x=20, y=10)

    # =================================All variable=====================================
    global username_r_var
    global password_r_var
    global username_l_var
    global password_l_var

    username_r_var=StringVar()
    password_r_var=StringVar()
    username_l_var=StringVar()
    password_l_var=StringVar()


    # =============================================Register Frame====================================================
    global register_frame
    register_frame = LabelFrame(root, bd=2, relief=GROOVE, bg='lime')
    register_frame.place(x=900, y=10, width=400, height=110)

    global username_r_entry
    global password_r_entry


    username_r_label = Label(register_frame, text="Username*", bg="lime")
    username_r_label.place(x=50, y=10)

    username_r_entry = Entry(register_frame,textvariable=username_r_var)
    username_r_entry.place(x=20, y=40)

    password_r_label = Label(register_frame, text="Password*", bg="lime")
    password_r_label.place(x=190, y=10)

    password_r_entry = Entry(register_frame,textvariable=password_r_var, show="*")
    password_r_entry.place(x=160, y=40)

    # Label(register_frame, text="").pack()
    register_photo = PhotoImage(file='sing1.png')
    register_button = Button(register_frame, image=register_photo,command=register_user,activebackground="black")
    register_button.place(x=300, y=30)

    # =============================================Login Frame=======================================================
    global login_frame
    login_frame = LabelFrame(root, bd=2, relief=GROOVE, bg='forestgreen')
    login_frame.place(x=300, y=180, width=800, height=450)

    global username_l_entry
    global password_l_entry

    my_name_label=Label(login_frame,text="Creator: Faysal Sarder",fg="white",bg="forestgreen")
    my_name_label.pack(side=BOTTOM,fill=X)

    login_photo = PhotoImage(file='website.png')
    login_button = Label(login_frame, image=login_photo)
    login_button.place(x=320, y=20)

    username_l_label = Label(login_frame, text="Username",fg='white', bg="forestgreen")
    username_l_label.place(x=230, y=180)

    username_l_entry = Entry(login_frame)
    username_l_entry.place(x=320, y=180)

    password_l_label = Label(login_frame, text="Password",fg='white', bg="forestgreen")
    password_l_label.place(x=230, y=220)

    password_l_entry = Entry(login_frame, show="*")
    password_l_entry.place(x=320, y=220)

    # Label(register_frame, text="").pack()
    login1_photo = PhotoImage(file='register.png')
    login_button = Button(login_frame, image=login1_photo,command=login_verify,activebackground="darkblue")
    login_button.place(x=345, y=250)

    login2_photo = PhotoImage(file='password.png')
    forgot_button = Button(login_frame, image=login2_photo,activebackground="red",command=forgot_password)
    forgot_button.place(x=750, y=380)

    # ==========================================Login Frame END===================================================
    root.mainloop()


Student()


