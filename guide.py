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



class Guide:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

#====set background image =======
        img4=Image.open(r"image\guide.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)


        tilte_lbl= Label(bg_img,text="Guide",font=("times new roman",35,"bold"),fg="green") 
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


#===adding student information frame=====
        Application_Information_Frame=LabelFrame(bg_img,bd=2.5,bg="white",relief=SUNKEN,text="Application Information")
        Application_Information_Frame.place(x=500,y=60,width=550,height=600)


#==========step 1================
        studentID_label=Label(Application_Information_Frame,text="Step 1 :",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Open 'Student Detail' button",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=0,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Fill up the details to save your information for the 1st time.",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=1,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Open 'Train data' button to train your photos.",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=2,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* You can see your 100's of photo sample under 'Photos' button.",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=3,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="*NOTE*-These steps are compulsory for new users.",font=("times new roman",10,"bold"),bg="white",fg="red")
        studentID_label.grid(row=4,column=1,padx=10,sticky=W) #make a grid for the details

#============step2================
        studentID_label=Label(Application_Information_Frame,text="Step 2 :",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=5,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Open 'Give Attendance' button",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=5,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Give your attendance by your face recognition",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=6,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Click 'enter' to close the the webcamera window",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=7,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Check you attendance under 'See Attendance' button",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=8,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Import the attendance.csv file to check your attendance",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=9,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* You can export the attendance sheet on clicking on 'Export'",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=10,column=1,padx=10,sticky=W) #make a grid for the details

#===============step 3===================
        studentID_label=Label(Application_Information_Frame,text="Step 3 :",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=11,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* You can play some funny games -",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=11,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="(1)'Make Sketch'- Start the Game,Drag the maouse to",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=12,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="select the portion in which you wish to make the sketch",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=13,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="Press enter to make the sketch ",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=14,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="click on 'Q' button to close the window.",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=15,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="(2)'Face Emotion'-Start the Game, to detect the emotion",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=16,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="Make your face still in front of your webcamera",font=("times new roman",10,"bold"),bg="white",fg="red")
        studentID_label.grid(row=17,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="Click on 'Q' to close the window",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=18,column=1,padx=10,sticky=W) #make a grid for the details

#=========step 4================
        studentID_label=Label(Application_Information_Frame,text="Step 4 :",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=19,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* If there is any confusion regarding the application",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=19,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="then there is a 'Help' button provided which will",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=20,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="guide you manually",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=21,column=1,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Also details of developer under 'Developer' button",font=("times new roman",10,"bold"),bg="white")
        studentID_label.grid(row=22,column=1,padx=10,sticky=W) #make a grid for the details


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
    obj=Guide(root)
    root.mainloop()