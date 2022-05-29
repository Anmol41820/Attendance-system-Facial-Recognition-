# from curses.panel import bottom_panel
# import numpy
# from numpy import delete
# import mysql
# from mysql import connector
# import mysql.connector
# from ast import Not
from time import strftime
from datetime import datetime
from tkinter import*
from tkinter import ttk
import tkinter
# from tkinter.font import BOLD
# from turtle import st
from PIL import Image , ImageTk
from tkinter import messagebox

from scipy.misc import face
import mysql.connector 
import cv2

# from scipy.misc import face
# global connection 
conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys')




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")


  #=====making text variable for the database===
        self.var_Department =StringVar()
        self.var_Program =StringVar() 
        self.var_Year =StringVar() 
        self.var_Semester =StringVar() 
        self.var_RollNo =StringVar() 
        self.var_Name =StringVar() 
        self.var_Gender =StringVar() 
        self.var_DOB =StringVar() 
        self.var_email =StringVar() 
        self.var_PhoneNo =StringVar() 
        self.var_Address =StringVar() 
        self.var_HOD =StringVar()       

    #====set image 1=======
        img1=Image.open(r"image\student1.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)  #resise and convert high level img to low level img
        self.photoimg1=ImageTk.PhotoImage(img1)

        #======show image 1 in window=====
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)


    #====set image 2=======
        img2=Image.open(r"image\student2.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg2=ImageTk.PhotoImage(img2)

        #======show image 2 in window=====
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)


    #====set image 3=======
        img3=Image.open(r"image\student3.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg3=ImageTk.PhotoImage(img3)

        #======show image 3 in window=====
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=540,height=130)



        #====set background image =======
        img4=Image.open(r"image\student4.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)


        #======Adding a tilte box contain the student details=======
        tilte_lbl= Label(bg_img,text="STUDENT DETAILS",font=("times new roman",35,"bold"),bg="white",fg="green") 
        tilte_lbl.place(x=0,y=0,width=1530,height=45)

#=====adding time=======
        def time():
            string =strftime('%H:%M:%S %p')   #take the current time
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1 = Label(tilte_lbl,font=('times new roman',14,'bold'),background='white',fg='blue') #make tabel to show time
        lb1.place(x=0,y=0,width=110,height=50) #place the time

        time() #make a call to time function



    #=====make the box/frame for student details======
        main_frame=Frame(bg_img,bd=3,bg="#988C89")
        main_frame.place(x=15,y=55,width=1497,height=585)

        #===adding frame for buttons=====
        button_exit_Frame=Frame(bg_img,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=7,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)

#====now working in left frame ========
        left_Frame= LabelFrame(main_frame,bd=2.5,relief=SUNKEN,text="Student Detail",font=("times new roman",20,"bold"))
        left_Frame.place(x=10,y=10,width=720,height=580)

    #==put a image in left frame====
        left_img=Image.open(r"image\student5.jpg")
        left_img=left_img.resize((720,130),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.left_photoimg=ImageTk.PhotoImage(left_img)

        #======show left image in window=====
        f_lbl=Label(left_Frame,image=self.left_photoimg)
        f_lbl.place(x=5,y=10,width=720,height=130)


#===adding course frame=====
        course_Frame=LabelFrame(left_Frame,bd=2.5,bg="white",relief=SUNKEN,text="Current Course Details")
        course_Frame.place(x=5,y=135,width=720,height=150)

        #==Adding department labels===
        dept_label=Label(course_Frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dept_label.grid(row=0,column=0,padx=10,sticky=W) #make a grid for the details

        #===make combo box for the department=====
        dept_combo_box=ttk.Combobox(course_Frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state="readonly",width=17) #add the detain of dept in the table using variable in text simmillarly in all the data feild to combobox and entry box
        dept_combo_box["values"]=("Select Department","Computer Science(CSE)","Electrical(EE)","Mathmetical And Computer Science(MnC)","Information Tecnology(IT)","Machenical(ME)","Chemical(CHE)","Aerospace(AE)","Civil(CE)","Material Science(MSE)","Other")
        dept_combo_box.current(0) #make the select department at 1st position
        dept_combo_box.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #==Adding program labels===
        program_label=Label(course_Frame,text="Program",font=("times new roman",12,"bold"),bg="white")
        program_label.grid(row=0,column=2,padx=10,sticky=W) #make a grid for the details

        #===make combo box for the program=====
        program_combo_box=ttk.Combobox(course_Frame,textvariable=self.var_Program,font=("times new roman",12,"bold"),state="readonly",width=17)
        program_combo_box["values"]=("Select Program","B-Tech","BE","M-Tech","PhD","Other")
        program_combo_box.current(0) 
        program_combo_box.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #==Adding Year labels===
        year_label=Label(course_Frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W) #make a grid for the details

        #===make combo box for the year=====
        year_combo_box=ttk.Combobox(course_Frame,textvariable=self.var_Year,font=("times new roman",12,"bold"),state="readonly",width=17)
        year_combo_box["values"]=("Select Year","2020-2021","2021-2022","2022-2023")
        year_combo_box.current(0) 
        year_combo_box.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #==Adding semester labels===
        sem_label=Label(course_Frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W) #make a grid for the details

        #===make combo box for the semester=====
        sem_combo_box=ttk.Combobox(course_Frame,textvariable=self.var_Semester,font=("times new roman",12,"bold"),state="readonly",width=17)
        sem_combo_box["values"]=("Select Semester","Semester-I","Semester-II")
        sem_combo_box.current(0) 
        sem_combo_box.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#===adding student information frame=====
        student_Information_Frame=LabelFrame(left_Frame,bd=2.5,bg="white",relief=SUNKEN,text="Student Information")
        student_Information_Frame.place(x=5,y=240,width=720,height=400)


    #==Adding Student ID labels===
        studentID_label=Label(student_Information_Frame,text="Student ID/RollNo :",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_data=ttk.Entry(student_Information_Frame,textvariable=self.var_RollNo,width=20,font=("times new roman",12,"bold")) #blank box to write the data
        studentID_data.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #==Adding Student Name labels===
        student_name_label=Label(student_Information_Frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W) #make a grid for the details

        student_name_data=ttk.Entry(student_Information_Frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_name_data.grid(row=0,column=3,padx=10,pady=5,sticky=W)

    #==Adding Student Gender labels===
        student_gender_label=Label(student_Information_Frame,text="Gender :",font=("times new roman",12,"bold"),bg="white")
        student_gender_label.grid(row=1,column=0,padx=10,sticky=W) #make a grid for the details


        #===make combo box for the gender=====
        gender_combo_box=ttk.Combobox(student_Information_Frame,textvariable=self.var_Gender,font=("times new roman",12,"bold"),state="readonly",width=17)
        gender_combo_box["values"]=("Select Gender","Male","Female","Other")
        gender_combo_box.current(0) 
        gender_combo_box.grid(row=1,column=1,padx=2,pady=10,sticky=W)

    #==Adding Student DOB labels===
        student_DOB_label=Label(student_Information_Frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        student_DOB_label.grid(row=1,column=2,padx=10,sticky=W) #make a grid for the details

        student_DOB_data=ttk.Entry(student_Information_Frame,textvariable=self.var_DOB,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_DOB_data.grid(row=1,column=3,padx=10,pady=5,sticky=W)

    #==Adding Student email labels===
        student_email_label=Label(student_Information_Frame,text="email :",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=2,column=0,padx=10,sticky=W) #make a grid for the details

        student_email_data=ttk.Entry(student_Information_Frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_email_data.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #==Adding Student PhoneNo labels===
        student_PhoneNo_label=Label(student_Information_Frame,text="PhoneNo :",font=("times new roman",12,"bold"),bg="white")
        student_PhoneNo_label.grid(row=2,column=2,padx=10,sticky=W) #make a grid for the details

        student_PhoneNo_data=ttk.Entry(student_Information_Frame,textvariable=self.var_PhoneNo,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_PhoneNo_data.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #==Adding Student Address labels===
        student_Address_label=Label(student_Information_Frame,text="Address :",font=("times new roman",12,"bold"),bg="white")
        student_Address_label.grid(row=3,column=0,padx=10,sticky=W) #make a grid for the details

        student_Address_data=ttk.Entry(student_Information_Frame,textvariable=self.var_Address,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_Address_data.grid(row=3,column=1,padx=10,pady=5,sticky=W)

    #==Adding Student Department_HOD labels===
        student_Department_HOD_label=Label(student_Information_Frame,text="HOD :",font=("times new roman",12,"bold"),bg="white")
        student_Department_HOD_label.grid(row=3,column=2,padx=10,sticky=W) #make a grid for the details

        student_Department_HOD_data=ttk.Entry(student_Information_Frame,textvariable=self.var_HOD,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_Department_HOD_data.grid(row=3,column=3,padx=10,pady=5,sticky=W)


#===making radio buttons for take photo and not take photo=====
        self.var_radio1=StringVar()
        radio_button1=ttk.Radiobutton(student_Information_Frame,text="Take Photo",variable=self.var_radio1,value="YES")
        radio_button1.grid(row=4,column=0)

        # self.var_radio2=StringVar()
        radio_button2=ttk.Radiobutton(student_Information_Frame,text="Not Take Photo",variable=self.var_radio1,value="NO")
        radio_button2.grid(row=4,column=1)


#===adding frame for buttons=====
        button_Frame=Frame(student_Information_Frame,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame.place(x=5,y=180,width=720,height=40)

    #===adding Save button=====
        save_button=Button(button_Frame,width=19,text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        save_button.grid(row=0,column=0)

    #===adding update button=====
        update_button=Button(button_Frame,width=19,text="Update",command=self.update_data,font=("times new roman",12,"bold"),bg="green",fg="white")
        update_button.grid(row=0,column=1)

    #===adding delete button=====
        delete_button=Button(button_Frame,width=19,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),bg="red",fg="white")
        delete_button.grid(row=0,column=2)

    #===adding reset button=====
        reset_button=Button(button_Frame,width=19,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_button.grid(row=0,column=3)


#===adding frame2 for buttons=====
        button_Frame2=Frame(student_Information_Frame,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame2.place(x=5,y=220,width=720,height=40)

    #===adding Take photo button=====
        take_photo_button=Button(button_Frame2,width=78,text="Take Photo",command=self.generate_dataset,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=0,column=0)

    # #===adding update photo button=====
    #     update_photo_button=Button(button_Frame2,width=38,text="Update Photo",font=("times new roman",12,"bold"),bg="blue",fg="white")
    #     update_photo_button.grid(row=0,column=1)









#===now working in the right frame ======
        right_Frame= LabelFrame(main_frame,bd=2.5,relief=SUNKEN,text="Student Database",font=("times new roman",12,"bold"))
        right_Frame.place(x=740,y=10,width=735,height=580)

    #==put a image in right frame====
        right_img=Image.open(r"image\student7.jpg")
        right_img=right_img.resize((720,130),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.right_photoimg=ImageTk.PhotoImage(right_img)

        #======show left image in window=====
        f_lbl=Label(right_Frame,image=self.right_photoimg)
        f_lbl.place(x=5,y=10,width=720,height=130)






    
#====making table frame====
        table_Frame=Frame(right_Frame,relief=SUNKEN)
        table_Frame.place(x=5,y=140,width=720,height=400)

    #===making scoll bar===
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

    #===making table and scroll bar system====
        self.student_table=ttk.Treeview(table_Frame,columns=("Department","Program","Year","Semester","RollNo","Name","Gender","DOB","email","PhoneNo","Address","HOD","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   #set scroll in x and y direction 
        scroll_x.pack(side=BOTTOM,fill=X) #pack the scroll in x
        scroll_y.pack(side=RIGHT,fill=Y)  #pack the scroll in y
        scroll_x.config(command=self.student_table.xview) #link x bar with table
        scroll_y.config(command=self.student_table.yview) #link y bar with table

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Program",text="Program")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("RollNo",text="RollNo")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="email")
        self.student_table.heading("PhoneNo",text="PhoneNo")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("HOD",text="HOD")
        self.student_table.heading("Photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Department",width=100)
        self.student_table.column("Program",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("RollNo",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("PhoneNo",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("HOD",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1) #pack
        self.student_table.bind("<ButtonRelease>",self.get_cursor) #bind the button to one time clickable  
        self.fetch_data() #after fetching add the data in table

        
#=======function decration and adding massege box======
    def add_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Program.get()=="Select Program" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_RollNo.get()=="" or self.var_Name.get()=="" or self.var_DOB.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_email.get()=="" or self.var_PhoneNo.get()=="" or self.var_Address.get()=="" or self.var_HOD.get()=="":
            messagebox.showerror("Error","Please fill all the details",parent=self.root) #parent-self.root shows the message in that window only
        else:
            try:
                global conn
                conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys') #connection the mysql to python 
                cursor=conn.cursor()
                cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_Department.get(),self.var_Program.get(),self.var_Year.get(),self.var_Semester.get(),self.var_RollNo.get(),self.var_Name.get(),self.var_Gender.get(),self.var_DOB.get(),self.var_email.get(),self.var_PhoneNo.get(),self.var_Address.get(),self.var_HOD.get(),self.var_radio1.get() )) #execute the data in sql table from the input

                conn.commit() #so that the data remains updated
                self.fetch_data() #fetch the data from sql database
                conn.close()

                messagebox.showinfo("Success","Student Details are added successfully",parent=self.root)  #messagebox for the succcess 

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) #exception cases


    #===now fetching the data in the project from sql database===
    def fetch_data(self):
        global conn
        conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys') #connection the mysql to python
        cursor=conn.cursor()
        cursor.execute("select * from student") #select all the data from sql database

        #==now fetching the data from sql database to the project table
        data=cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children()) #deleting the children of student table

            #inserting the data by fetching
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit() #add
        conn.close()  #close


    #===making the cursor so that it point the data od table to update/delete/reset=====
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_Department.set(data[0]),
        self.var_Program.set(data[1]),
        self.var_Year.set(data[2]),
        self.var_Semester.set(data[3]),
        self.var_RollNo.set(data[4]),
        self.var_Name.set(data[5]),
        self.var_Gender.set(data[6]),
        self.var_DOB.set(data[7]),
        self.var_email.set(data[8]),
        self.var_PhoneNo.set(data[9]),
        self.var_Address.set(data[10]),
        self.var_HOD.set(data[11]),
        self.var_radio1.set(data[12])


    #===make the update button to function properly===
    def update_data(self):
        if self.var_Department.get()=="Select Department" or self.var_Program.get()=="Select Program" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_RollNo.get()=="" or self.var_Name.get()=="" or self.var_DOB.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_email.get()=="" or self.var_PhoneNo.get()=="" or self.var_Address.get()=="" or self.var_HOD.get()=="":
            messagebox.showerror("Error","Please fill all the details",parent=self.root) #parent-self.root shows the message in that window only
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update the details",parent=self.root)
                if Upadate>0:
                    global conn
                    conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys') #connection the mysql to python 
                    cursor=conn.cursor()

                    cursor.execute("update student set Department=%s,Program=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,email=%s,PhoneNo=%s,Address=%s,HOD=%s,Photo=%s where RollNo=%s",(
                        self.var_Department.get(),
                        self.var_Program.get(),
                        self.var_Year.get(),
                        self.var_Semester.get(),
                        self.var_Name.get(),
                        self.var_Gender.get(),
                        self.var_DOB.get(),
                        self.var_email.get(),
                        self.var_PhoneNo.get(),
                        self.var_Address.get(),
                        self.var_HOD.get(),
                        self.var_radio1.get(),
                        self.var_RollNo.get() )) #updating

                else:
                    if not Upadate: #if not updated return the old one
                        return
                
                messagebox.showinfo("Success","Student details are successfully updated",parent=self.root)  #show the sucess message box
                conn.commit() #update the data in sql database 
                self.fetch_data() #fetch the data from sql database to student detail table
                conn.close() #close the connection between sql and python project

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)    #exception error



    #======delete button function=====
    def delete_data(self):
        if self.var_RollNo.get()=="":
            messagebox.showerror("Error","RollNo must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student data delete","Do you want to delete the data of the student",parent=self.root)
                if delete>0:
                    global conn
                    conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys') #connection the mysql to python 
                    cursor=conn.cursor()

                    sql="delete from student where RollNo=%s"
                    val=[self.var_RollNo.get()]
                    cursor.execute(sql,val)
                
                else:
                    if not delete :
                        return

                conn.commit() #update the data in sql database 
                self.fetch_data() #fetch the data from sql database to student detail table
                conn.close() #close the connection between sql and python project
                messagebox.showinfo("Delete","Succussfully deleted sudent details", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    #exception error

    
    #===reset button function=====
    def reset_data(self):
        self.var_Department.set("Select Department")
        self.var_Program.set("Select Program")
        self.var_Year.set("Select Year")
        self.var_Semester.set("Select Semester")
        self.var_RollNo.set("")
        self.var_Name.set("")
        self.var_Gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_email.set("")
        self.var_PhoneNo.set("")
        self.var_Address.set("")
        self.var_HOD.set("")
        self.var_radio1.set("")



    #====Generate data set or take photo sample========
    def generate_dataset(self):
        if self.var_Department.get()=="Select Department" or self.var_Program.get()=="Select Program" or self.var_Year.get()=="Select Year" or self.var_Semester.get()=="Select Semester" or self.var_RollNo.get()=="" or self.var_Name.get()=="" or self.var_DOB.get()=="" or self.var_Gender.get()=="Select Gender" or self.var_email.get()=="" or self.var_PhoneNo.get()=="" or self.var_Address.get()=="" or self.var_HOD.get()=="":
            messagebox.showerror("Error","Please fill all the details",parent=self.root) #parent-self.root shows the message in that window only
        else:
            try: 
                global conn
                conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys') #connection the mysql to python 
                cursor=conn.cursor()
                cursor.execute("select * from student") #quiry to select
                # cursor.execute("select Name from student where RollNo=self.var_Roll_No.get()")
                myresult=cursor.fetchall() #store the all data in myresult
                id=self.var_RollNo.get()
                # for x in myresult:
                #     id+=1
                
                cursor.execute("update student set Department=%s,Program=%s,Year=%s,Semester=%s,Name=%s,Gender=%s,DOB=%s,email=%s,PhoneNo=%s,Address=%s,HOD=%s,Photo=%s where RollNo=%s",(
                                                                self.var_Department.get(),
                                                                self.var_Program.get(),
                                                                self.var_Year.get(),
                                                                self.var_Semester.get(),
                                                                self.var_Name.get(),
                                                                self.var_Gender.get(),
                                                                self.var_DOB.get(),
                                                                self.var_email.get(),
                                                                self.var_PhoneNo.get(),
                                                                self.var_Address.get(),
                                                                self.var_HOD.get(),
                                                                self.var_radio1.get(),
                                                                self.var_RollNo.get()==id 
                                            )) #updating
                # print(id)
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


        #===loading predifiend sata on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #use haarcascade

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert thecolor from rbg to gray
                    faces=face_classifier.detectMultiScale(gray,1.3,5) #scaling factoy =1.3 &minimum neighbor=5

                    for (x,y,w,h) in faces:  #making rectangle
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)#open web camera
                img_id=0 #create the img_id
                while True:
                    ret,my_frame=cap.read() #read the img
                    # my_frame = cv2.imread(cap)
                    if face_cropped(my_frame) is not None:
                        img_id+=1  #taking many images sample
                        face=cv2.resize(face_cropped(my_frame),(450,450)) #resize all the sample and also cropped all the sample
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"  #storing the photo sample in jpg format in the 'data' folder with the name as user.id.img_id.jpg
                        cv2.imwrite(file_name_path,face) #store
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2) #to write the date in the face rectangle
                        cv2.imshow("Crooped Face",face)

                    #stop the loop afer 100 shots or press ender
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows() #destroy the web camera window
                messagebox.showinfo("Result","Generation data sets compled!! Now train your photo")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    #exception error






#===making the exit button =====
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Attendance Application","Are you sure, you want to exit ?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return


#==========calling main============
if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()