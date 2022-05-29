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

from developer import Developer
from guide import Guide



class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

     #====set background image =======
        img4=Image.open(r"image\help.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)

        #===adding frame for buttons=====
        button_exit_Frame=Frame(self.root,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=7,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)



#====set button 7(Developer) image =======
        img11=Image.open(r"image\img11.jpg")
        img11=img11.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg11=ImageTk.PhotoImage(img11)
    #======show button 7 image in window=====
        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.developer_data)
        b7.place(x=400,y=60,width=200,height=200)
    #======show button 7 text in window======
        b7_1=Button(bg_img,text="Developer",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.developer_data)
        b7_1.place(x=400,y=260,width=200,height=38)


#====set button 7(help) image =======
        help=Image.open(r"image\help2.jpg")
        help=help.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg12=ImageTk.PhotoImage(help)
    #======show button 7 image in window=====
        b7=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.guide_data)
        b7.place(x=100,y=60,width=200,height=200)
    #======show button 7 text in window======
        b7_2=Button(bg_img,text="Guide",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.guide_data)
        b7_2.place(x=100,y=260,width=200,height=38)



#===making the developer button =====
    def developer_data(self):
        self.new_window=Toplevel(self.root) #new window to on the top of old window
        self.app=Developer(self.new_window)  

#===making the guide button =====
    def guide_data(self):
        self.new_window=Toplevel(self.root) #new window to on the top of old window
        self.app=Guide(self.new_window) 


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
    obj=Help(root)
    root.mainloop()