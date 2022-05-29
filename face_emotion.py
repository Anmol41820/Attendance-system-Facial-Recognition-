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
from deepface import DeepFace



class Face_Emotion:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("See you Face Emotion")
        self.root.wm_iconbitmap("face.ico")

        #====set background image =======
        img4=Image.open(r"image\emotion1.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)

    #===adding frame for buttons=====
        button_Frame=Frame(bg_img,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame.place(x=750,y=300,width=240,height=55)

        #===adding play button=====
        play_button=Button(button_Frame,width=15,command=self.play,text="Play",font=("times new roman",20,"bold"),bg="green",fg="white")
        play_button.grid(row=0,column=0)


        button1_Frame=Frame(bg_img,bd=2.5,bg="white",relief=SUNKEN)
        button1_Frame.place(x=750,y=400,width=240,height=39)
        #===adding exit button=====
        exit_button=Button(button1_Frame,width=19,command=self.exit,text="Exit",font=("times new roman",15,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)




    def play(self):
        faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        cap=cv2.VideoCapture(0)
        cv2.destroyAllWindows()
        if not cap.isOpened():
            raise IOError("Cannt open webcam")

        while True:
            ret,frame = cap.read()

            result = DeepFace.analyze(frame,actions=['emotion'])
            # result1 = DeepFace.analyze(frame,actions=['age'])

            gray=cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
            faces = faceCascade.detectMultiScale(gray,1.1,4)

            for(x,y,w,h) in faces:
                cv2.rectangle(frame ,(x,y),(x+w,y+h), (0,255,0), 2)

            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame,result['dominant_emotion'],(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

            # cv2.putText(frame,result1['age'],(100,40),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

            # cv2.putText(frame,result['gender'],(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

            # cv2.putText(frame,result['race'],(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

            cv2.imshow('Face Emotion Fun Play',frame)

            if cv2.waitKey(2) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

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
    obj=Face_Emotion(root)
    root.mainloop()