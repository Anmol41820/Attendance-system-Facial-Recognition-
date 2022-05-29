# from pyexpat import features
from tkinter import*
from tkinter import ttk
import tkinter
# from tkinter.font import BOLD
# from turtle import st
from PIL import Image,ImageTk
from tkinter import messagebox

# from scipy.misc import face
import mysql.connector 
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys')

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

    #======Adding a tilte box contain the face recognition=======
        tilte_lbl= Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="blue") 
        tilte_lbl.place(x=0,y=0,width=1530,height=45)


    #=====adding time=======
        def time():
            string =strftime('%H:%M:%S %p')   #take the current time
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1 = Label(tilte_lbl,font=('times new roman',14,'bold'),background='white',fg='blue') #make tabel to show time
        lb1.place(x=0,y=0,width=110,height=50) #place the time

        time() #make a call to time function



    #==add image==
        bg_img=Image.open(r"image\giveattendance.jpg")
        bg_img=bg_img.resize((1530,700),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.bg_photoimg=ImageTk.PhotoImage(bg_img)

        #======show image in window=====
        f_lbl=Label(self.root,image=self.bg_photoimg)
        f_lbl.place(x=0,y=50,width=1530,height=700)

    #===adding frame for buttons=====
        button_exit_Frame=Frame(self.root,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=7,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)

    #===adding give attendance button=====
        giveattendance_button=Button(self.root,text="Give Attendance",command=self.face_recognition,font=("times new roman",24,"bold"),bg="green",fg="white")
        giveattendance_button.place(x=900,y=450)


#===make attendance button function=====
    def make_attendance(self,i,n,r,d):
        with open(r"attendance_data/attendance.csv","r+",newline="\n") as f: #open the csv file
            myDataList = f.readlines() #read the file
            name_list=[] #make the list
            for line in myDataList:
                entry = line.split((","))  #split it
                name_list.append(entry[0])  #insert the data
            


            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y") #store date
                dtString = now.strftime("%H:%M:%S") #store time
                # print(i)
                # print(n)
                f.writelines(f"\n{i},{n},{r},{d},{dtString},{d1},Present") #write the all details in the file



#===face recognition function to check with input data===
    def face_recognition(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #conver the image from rgb to gray scale
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) #take feature

            coord=[]
            #make rectangle
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict =clf.predict(gray_image[y:y+h,x:x+w])
                #predict the photo sample
            
                
                confidence=int((100*(1-predict/300)))#LBPH formula

            #make connection with mysql
                global conn
                conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys')
                
                cursor=conn.cursor()

            #take RollNo
                cursor.execute("select RollNo from student where RollNo="+ str(id))
                
                i=cursor.fetchone()[0]
                
                i="".join(str(i))
                

            #take name 
                cursor.execute("select Name from student where RollNo="+str(id))
                n=cursor.fetchone()[0]
                
                n="".join(str(n))
                

            #take email
                cursor.execute("select email from student where RollNo="+str(id))
                r=cursor.fetchone()[0]
                r="".join(str(r))

            #take department
                cursor.execute("select Department from student where RollNo="+ str(id))
                d=cursor.fetchone()[0]
                d="".join(str(d))


                if confidence>78:
                    cv2.putText(img,f"RollNo:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #text is given for rollNo

                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #text is given for name

                    cv2.putText(img,f"email:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #text is given for email

                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) #text is given for depatment

                    self.make_attendance(i,n,r,d)


                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Student",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3) 

                
                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #import the file
        clf=cv2.face.LBPHFaceRecognizer_create() #create LBPHFaceRecognizer
        clf.read("classifier.xml") #read the file for the input photosample

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW) #open web camera

        while True:
            ret,img=video_cap.read()  #read the photo
            img=recognize(img,clf,faceCascade) #recognize the img
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()

    #===making the exit button =====
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Attendance Application","Are you sure, you want to exit ?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return                

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()