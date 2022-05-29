from tkinter import*
from tkinter import ttk
import tkinter
# from tkinter.font import BOLD
# from turtle import st
from PIL import Image , ImageTk
from tkinter import messagebox
from face_emotion import Face_Emotion
from sketch import Sketch

from scipy.misc import face
import mysql.connector 
import cv2



class Games:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")


     #====set background image =======
        img4=Image.open(r"image\gamebg.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)


#====set button 7(make emotion) image =======
        img11=Image.open(r"image\emotion.jpg")
        img11=img11.resize((120,120),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg11=ImageTk.PhotoImage(img11)
    #======show button 7 image in window=====
        b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.face_emotion_data)
        b7.place(x=820,y=215,width=120,height=120)
    #======show button 7 text in window======
        b7_1=Button(bg_img,text="Face Emotion",font=("times new roman",15,"bold"),bg="white",fg="red",cursor="hand2",command=self.face_emotion_data)
        b7_1.place(x=820,y=335,width=120,height=30)


#====set button 7(help) image =======
        sketch_img=Image.open(r"image\sketch1.jpg")
        sketch_img=sketch_img.resize((120,120),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg12=ImageTk.PhotoImage(sketch_img)
    #======show button 7 image in window=====
        b7=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.sketch_data)
        b7.place(x=590,y=215,width=120,height=120)
    #======show button 7 text in window======
        b7_2=Button(bg_img,text="Make Sketch",font=("times new roman",15,"bold"),bg="white",fg="red",cursor="hand2",command=self.sketch_data)
        b7_2.place(x=590,y=335,width=120,height=30)

#===adding frame for buttons=====
        button_Frame=Frame(bg_img,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame.place(x=1300,y=700,width=180,height=37)
#===adding exit button=====
        exit_button=Button(button_Frame,width=19,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=1)


#===making the developer button =====
    def face_emotion_data(self):
        self.new_window=Toplevel(self.root) #new window to on the top of old window
        self.app=Face_Emotion(self.new_window)  

#===making the guide button =====
    def sketch_data(self):
        self.new_window=Toplevel(self.root) #new window to on the top of old window
        self.app=Sketch(self.new_window)  


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
    obj=Games(root)
    root.mainloop()