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
from intro2 import Intro2
from main import Face_Recognition_System



class Intro1:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

#====set background image =======
        img4=Image.open(r"image\intro.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)


        tilte_lbl= Label(bg_img,text="Instructions",font=("times new roman",35,"bold"),fg="green") 
        tilte_lbl.place(x=0,y=0,width=1530,height=45)

        


#===adding frame for buttons=====
        button_exit_Frame=Frame(tilte_lbl,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=5,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)


#===adding student information frame=====
        Application_Information_Frame=LabelFrame(bg_img,bd=2.5,bg="light blue",relief=SUNKEN,text="Info for new user")
        Application_Information_Frame.place(x=60,y=150,width=650,height=510)


#==Adding Student ID labels===
        studentID_label=Label(Application_Information_Frame,text="Step 1 :",font=("times new roman",19,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Open 'Student Detail' button",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=1,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Fill up the details to save your information for the 1st time.",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=2,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* Open 'Train data' button to train your photos.",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=3,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="* You can see your 100's of photo sample under 'Photos'",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=4,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="button.",font=("times new roman",15,"bold"),bg="white")
        studentID_label.grid(row=5,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

        studentID_label=Label(Application_Information_Frame,text="*NOTE*-These steps are compulsory for new users.",font=("times new roman",15,"bold"),bg="white",fg="red")
        studentID_label.grid(row=6,column=1,padx=10,pady=10,sticky=W) #make a grid for the details

#===adding frame for buttons=====
        button_next_Frame=Frame(Application_Information_Frame,bd=2.5,bg="white",relief=SUNKEN)
        button_next_Frame.place(x=180,y=430,width=295,height=37)
    
    #===adding next button=====
        next_button=Button(button_next_Frame,command=self.next_data,width=15,text="Next",font=("times new roman",12,"bold"),bg="white",fg="black")
        next_button.grid(row=0,column=0)
    #===adding skip button=====
        skip_button=Button(button_next_Frame,command=self.skip_data,width=15,text="Skip",font=("times new roman",12,"bold"),bg="white",fg="black")
        skip_button.grid(row=0,column=1)


#====set side image =======
        im=Image.open(r"image\intro1.jpg")
        im=im.resize((650,510),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoim=ImageTk.PhotoImage(im)

        #======show backgrond image in window=====
        bg_img=Label(bg_img,image=self.photoim)
        bg_img.place(x=800,y=150,width=650,height=510)



#===making the exit button =====
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Introduction","Are you sure, you want to exit ?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return 


#===making the next button =====
    def next_data(self):
        self.new_window=Toplevel(self.root) #new window to on the top of old window 
        self.app=Intro2(self.new_window)  

#===making the skip button =====
    def skip_data(self):
        self.skip_data=tkinter.messagebox.askyesno("Introduction","Are you sure, you want to skip ?",parent=self.root)
        if self.skip_data>0:
            self.new_window=Toplevel(self.root) #new window to on the top of old window
            self.app=Face_Recognition_System(self.new_window)
        else:
            return
        


#==========calling main============
if __name__=="__main__":
    root=Tk()
    obj=Intro1(root)
    root.mainloop()