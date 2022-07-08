from tkinter import *
from tkinter import messagebox
import os                          # os means operating system
import pymysql
from tkinter import ttk

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

    combo_gender = ttk.Combobox(Manage_Frame, textvariable=Gender_var, font=("arial", 7, "bold"),state='readonly')
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

    Addbtn = Button(btn_Frame, text="Add", width=10,activebackground="yellow").grid(row=0, column=0, padx=10, pady=10)
    updatebtn = Button(btn_Frame, text="Update",bg="blue", fg="white", width=10).grid(row=0, column=1, padx=10,
                                                                                          pady=10)
    deletebtn = Button(btn_Frame, text="Delete",bg="red",fg="white",  width=10).grid(row=0, column=2, padx=10,
                                                                                          pady=10)
    clearbtn = Button(btn_Frame, text="Clear", width=10,activebackground="yellow" ).grid(row=0, column=3, padx=10, pady=10)

    # ======================================Detail_Frame============================
    global Detail_Frame
    Detail_Frame = Frame(login_success_screen, bd=4, relief=RIDGE, bg="gray")
    Detail_Frame.place(x=500, y=40, width=800, height=580)

    global search_by_var
    global search_txt_var
    search_by_var = StringVar()
    search_by_var.set("Select")
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

    txt_Search = Entry(Detail_Frame, width=20, textvariable=search_txt_var, font=("arial", 10, "bold"), bd=5,
                       relief=GROOVE)
    txt_Search.grid(row=0, column=2, padx=10, pady=20, sticky="w")

    searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5).grid(row=0, column=3,
                                                                                                     padx=10, pady=10)
    showbtn = Button(Detail_Frame, text="Show", width=10, pady=5).grid(row=0, column=4,
                                                                                                padx=10, pady=10)


    #=======================================Table Frame=======================================
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

    Student_table.heading("Roll",text="Roll No")
    Student_table.heading("Name", text="Name")
    Student_table.heading("Gender", text="Gender")
    Student_table.heading("Dept.", text="Dept.")
    Student_table['show']='headings'
    Student_table.column('Roll',width=150)
    Student_table.column('Name', width=150)
    Student_table.column('Gender', width=150)
    Student_table.column('Dept.', width=150)
    Student_table.pack(fill=BOTH,expand=1)
    #Student_table.bind("<ButtonRelease-1>",get_cursor)
    #fetch_data()



#=======================================add_students==========================================================

def add_students():
    if Id_var.get() == "" or Name_var.get() == "" or Gender_var.get() == "" or Department_var.get()=="":
        messagebox.showerror(title="Error", message="All fields are required")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s)", (Id_var.get(),
                                                              Name_var.get(),
                                                              Gender_var.get(),
                                                              Department_var.get()

                                                              ))
        con.commit()
        con.close()


# =====================================password_not_recognised=======================================================
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

def Student():        # code start and 1st widget
    root = Tk()
    root.title("Register & Login")
    root.geometry("1350x700+0+0")
    root.iconbitmap(r'identifier.ico')

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
    register_frame = LabelFrame(root, bd=2, relief=GROOVE, bg='pink')
    register_frame.place(x=900, y=10, width=400, height=110)

    global username_r_entry
    global password_r_entry


    username_r_label = Label(register_frame, text="Username*", bg="pink")
    username_r_label.place(x=50, y=10)

    username_r_entry = Entry(register_frame,textvariable=username_r_var)
    username_r_entry.place(x=20, y=40)

    password_r_label = Label(register_frame, text="Password*", bg="pink")
    password_r_label.place(x=190, y=10)

    password_r_entry = Entry(register_frame,textvariable=password_r_var, show="*")
    password_r_entry.place(x=160, y=40)

    # Label(register_frame, text="").pack()
    register_photo = PhotoImage(file='sign.png')
    register_button = Button(register_frame, image=register_photo,command=register_user)
    register_button.place(x=300, y=20)

    # =============================================Login Frame====================================================
    global login_frame
    login_frame = LabelFrame(root, bd=2, relief=GROOVE, bg='pink')
    login_frame.place(x=300, y=180, width=800, height=450)

    global username_l_entry
    global password_l_entry


    login_photo = PhotoImage(file='website.png')
    login_button = Label(login_frame, image=login_photo)
    login_button.place(x=320, y=20)

    username_l_label = Label(login_frame, text="Username", bg="pink")
    username_l_label.place(x=230, y=180)

    username_l_entry = Entry(login_frame)
    username_l_entry.place(x=320, y=180)

    password_l_label = Label(login_frame, text="Password", bg="pink")
    password_l_label.place(x=230, y=220)

    password_l_entry = Entry(login_frame, show="*")
    password_l_entry.place(x=320, y=220)

    # Label(register_frame, text="").pack()
    login1_photo = PhotoImage(file='register.png')
    login_button = Button(login_frame, image=login1_photo,command=login_verify)
    login_button.place(x=345, y=250)

    # ==========================================Login Frame END===================================================
    root.mainloop()



Student()


