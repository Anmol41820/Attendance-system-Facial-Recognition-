from time import strftime
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
import os
import csv
from tkinter import filedialog

# from scipy.misc import face
# global connection 
conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys')

mydata=[]




class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("Attendance")
        self.root.wm_iconbitmap("face.ico")

    #=====making text variable for the database===
        self.var_RollNo =StringVar()
        self.var_Name =StringVar() 
        self.var_email =StringVar() 
        self.var_Department =StringVar() 
        self.var_Time =StringVar()
        self.var_Date =StringVar()
        self.var_Attendance_Status =StringVar()

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


        #======Adding a tilte box contain the ATTENDANCE DETAILS=======
        tilte_lbl= Label(bg_img,text="ATTENDANCE DETAILS",font=("times new roman",35,"bold"),bg="white",fg="green") 
        tilte_lbl.place(x=0,y=0,width=1530,height=45)

    #=====adding time=======
        def time():
            string =strftime('%H:%M:%S %p')   #take the current time
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1 = Label(tilte_lbl,font=('times new roman',14,'bold'),background='white',fg='blue') #make tabel to show time
        lb1.place(x=0,y=0,width=110,height=50) #place the time

        time() #make a call to time function

    #===adding frame for buttons=====
        button_exit_Frame=Frame(tilte_lbl,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=5,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)

        #=====make the box/frame for student details======
        main_frame=Frame(bg_img,bd=3,bg="#988C89")
        main_frame.place(x=15,y=55,width=1497,height=585)

#====now working in left frame ========
        left_Frame= LabelFrame(main_frame,bd=2.5,relief=SUNKEN,text="Attendance Detail",font=("times new roman",20,"bold"))
        left_Frame.place(x=10,y=10,width=720,height=580)

    #==put a image in left frame====
        left_img=Image.open(r"image\student5.jpg")
        left_img=left_img.resize((720,130),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.left_photoimg=ImageTk.PhotoImage(left_img)

        #======show left image in window=====
        f_lbl=Label(left_Frame,image=self.left_photoimg)
        f_lbl.place(x=5,y=10,width=720,height=130)

        left_inside_frame=Frame(left_Frame,bd=3,bg="white")
        left_inside_frame.place(x=5,y=140,width=705,height=370)

       
        #==Adding Attendance labels===
        RollNo_label=Label(left_inside_frame,text="RollNo",font=("times new roman",12,"bold"),bg="white")
        RollNo_label.grid(row=0,column=0,padx=10,sticky=W) #make a grid for the details

        RollNo_entry=ttk.Entry(left_inside_frame,textvariable=self.var_RollNo,width=20,font=("times new roman",12,"bold")) #blank box to write the data
        RollNo_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

    #==Adding Student Name labels===
        student_name_label=Label(left_inside_frame,text="Name :",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,sticky=W) #make a grid for the details

        student_name_data=ttk.Entry(left_inside_frame,textvariable=self.var_Name,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_name_data.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #==Adding Student email labels===
        student_email_label=Label(left_inside_frame,text="email :",font=("times new roman",12,"bold"),bg="white")
        student_email_label.grid(row=1,column=0,padx=10,sticky=W) #make a grid for the details

        student_email_data=ttk.Entry(left_inside_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        student_email_data.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #==Adding department labels===
        Department_label=Label(left_inside_frame,text="Department :",font=("times new roman",12,"bold"),bg="white")
        Department_label.grid(row=1,column=2,padx=10,sticky=W) #make a grid for the details

    #===make combo box for the attendance=====
        Department_combo_box=ttk.Combobox(left_inside_frame,textvariable=self.var_Department,font=("times new roman",12,"bold"),state="readonly",width=17) #add the detain of dept in the table using variable in text simmillarly in all the data feild to combobox and entry box
        Department_combo_box["values"]=("Select Department","Computer Science(CSE)","Electrical(EE)","Mathmetical And Computer Science(MnC)","Information Tecnology(IT)","Machenical(ME)","Chemical(CHE)","Aerospace(AE)","Civil(CE)","Material Science(MSE)","Other")
        Department_combo_box.current(0) #make the select department at 1st position
        Department_combo_box.grid(row=1,column=3,padx=2,pady=10,sticky=W)

    #==Adding Time labels===
        Time_label=Label(left_inside_frame,text="Time :",font=("times new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,sticky=W) #make a grid for the details

        Time_data=ttk.Entry(left_inside_frame,textvariable=self.var_Time,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        Time_data.grid(row=2,column=1,padx=10,pady=5,sticky=W)

    #==Adding Date labels===
        Date_label=Label(left_inside_frame,text="Date :",font=("times new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,sticky=W) #make a grid for the details

        Date_data=ttk.Entry(left_inside_frame,textvariable=self.var_Date,width=20,font=("times new roman",12,"bold"))  #blank box to write the data
        Date_data.grid(row=2,column=3,padx=10,pady=5,sticky=W)

    #==Adding Attendance status labels===
        Attendance_Status_label=Label(left_inside_frame,text="Attendance_Status",font=("times new roman",12,"bold"),bg="white")
        Attendance_Status_label.grid(row=3,column=0,padx=10,sticky=W) #make a grid for the details

        #===make combo box for the attendance=====
        self.Attendance_Status_combo_box=ttk.Combobox(left_inside_frame,textvariable=self.var_Attendance_Status,font=("times new roman",12,"bold"),state="readonly",width=17) #add the detain of dept in the table using variable in text simmillarly in all the data feild to combobox and entry box
        self.Attendance_Status_combo_box["values"]=("Mark Attendance","Present","Absent")
        self.Attendance_Status_combo_box.current(0) #make the select department at 1st position
        self.Attendance_Status_combo_box.grid(row=3,column=1,padx=2,pady=10,sticky=W)


#===adding frame for buttons=====
        button_Frame=Frame(left_inside_frame,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame.place(x=5,y=300,width=720,height=40)

    #===adding IMport csv button=====
        save_button=Button(button_Frame,command=self.importCsv,width=24,text="Import csv",font=("times new roman",12,"bold"),bg="green",fg="white")
        save_button.grid(row=0,column=0)

    #===adding export csv button=====
        update_button=Button(button_Frame,command=self.exportCsv,width=24,text="Export csv",font=("times new roman",12,"bold"),bg="green",fg="white")
        update_button.grid(row=0,column=1)


    #===adding reset button=====
        reset_button=Button(button_Frame,command=self.reset_data,width=24,text="Reset",font=("times new roman",12,"bold"),bg="red",fg="white")
        reset_button.grid(row=0,column=2)


       







#===now working in the right frame ======
        right_Frame= LabelFrame(main_frame,bd=2.5,relief=SUNKEN,text="Attendance Database",font=("times new roman",12,"bold"))
        right_Frame.place(x=740,y=10,width=735,height=580)


#====making table frame====
        table_Frame=Frame(right_Frame,relief=SUNKEN)
        table_Frame.place(x=5,y=5,width=720,height=450)

    #===making scoll bar===
        scroll_x=ttk.Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_Frame,orient=VERTICAL)

    #===making table and scroll bar system====
        self.Attendance_table=ttk.Treeview(table_Frame,columns=("RollNo","Name","email","Department","Time","Date","Attendance_Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)   #set scroll in x and y direction 
        scroll_x.pack(side=BOTTOM,fill=X) #pack the scroll in x
        scroll_y.pack(side=RIGHT,fill=Y)  #pack the scroll in y
        scroll_x.config(command=self.Attendance_table.xview) #link x bar with table
        scroll_y.config(command=self.Attendance_table.yview) #link y bar with table


        self.Attendance_table.heading("RollNo",text="RollNo")
        self.Attendance_table.heading("Name",text="Name")
        self.Attendance_table.heading("email",text="email")
        self.Attendance_table.heading("Department",text="Department")
        self.Attendance_table.heading("Time",text="Time")
        self.Attendance_table.heading("Date",text="Date")
        self.Attendance_table.heading("Attendance_Status",text="Attendance_Status")
        self.Attendance_table["show"]="headings"

        self.Attendance_table.column("RollNo",width=100)
        self.Attendance_table.column("Name",width=100)
        self.Attendance_table.column("email",width=100)
        self.Attendance_table.column("Department",width=100)
        self.Attendance_table.column("Time",width=100)
        self.Attendance_table.column("Date",width=100)
        self.Attendance_table.column("Attendance_Status",width=120)

        self.Attendance_table.pack(fill=BOTH,expand=1) #pack
        # self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.Attendance_table.bind("<ButtonRelease>",self.get_cursor) #bind the button to one time clickable


    #fetch the data into the table===
    def fetchData(self,rows):
        self.Attendance_table.delete(*self.Attendance_table.get_children())
        for i in rows:
            self.Attendance_table.insert("",END,values=i)

#==import the data from the csv file
    def importCsv(self):
        global mydata
        mydata.clear()
        file=filedialog.askopenfile(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(r"attendance_data/attendance.csv","r") as myfile:
            csvread=csv.reader(myfile,delimiter=",") #separete by ,
            for i in csvread:
                # print(i)
                mydata.append(i)
            self.fetchData(mydata)

#==export the data from the csv file
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("NO Data","No Daat found to export",parent=self.root)
            file=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(file,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Expoted","Your data esported to "+os.path.basename(file)+" successfully")

        except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)    #exception error


     #===making the cursor so that it point the data od table to update/delete/reset=====
    def get_cursor(self,event=""):
        cursor_focus=self.Attendance_table.focus()
        content=self.Attendance_table.item(cursor_focus)
        data=content["values"]

        
        self.var_RollNo.set(data[0]),
        self.var_Name.set(data[1]),
        self.var_email.set(data[2]),
        self.var_Department.set(data[3]),
        self.var_Time.set(data[4]),
        self.var_Date.set(data[5]),
        self.var_Attendance_Status.set(data[6])
        


    
    #===reset button function=====
    def reset_data(self):
        self.var_RollNo.set(""),
        self.var_Name.set(""),
        self.var_email.set(""),
        self.var_Department.set("Select Department"),
        self.var_Time.set(""),
        self.var_Date.set(""),
        self.var_Attendance_Status.set("")

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
    obj=Attendance(root)
    root.mainloop()