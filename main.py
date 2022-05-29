from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from help import Help
from games import Games

# import numpy
# from numpy import delete


# class face:


class Face_Recognition_System:
        def __init__(self,root):
                self.root = root
                self.root.geometry("1530x790+0+0")  #geometry of the window
                self.root.title("face Recognition System")
                self.root.wm_iconbitmap("face.ico")

                #====set image 1=======
                img1=Image.open(r"image\giphy.gif")
                img1=img1.resize((500,130),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg1=ImageTk.PhotoImage(img1)

                #======show image 1 in window=====
                f_lbl=Label(self.root,image=self.photoimg1)
                f_lbl.place(x=0,y=0,width=500,height=130)


                #====set image 2=======
                img2=Image.open(r"image\img2.png")
                img2=img2.resize((500,130),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg2=ImageTk.PhotoImage(img2)

                #======show image 2 in window=====
                f_lbl=Label(self.root,image=self.photoimg2)
                f_lbl.place(x=500,y=0,width=500,height=130)


                #====set image 3=======
                img3=Image.open(r"image\img3.jpg")
                img3=img3.resize((500,130),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg3=ImageTk.PhotoImage(img3)

                #======show image 3 in window=====
                f_lbl=Label(self.root,image=self.photoimg3)
                f_lbl.place(x=1000,y=0,width=540,height=130)


                #====set background image =======
                img4=Image.open(r"image\img4.jpg")
                img4=img4.resize((1530,710),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg4=ImageTk.PhotoImage(img4)

                #======show backgrond image in window=====
                bg_img=Label(self.root,image=self.photoimg4)
                bg_img.place(x=0,y=130,width=1530,height=710)


                #======Adding a tilte box contain the app name=======
                tilte_lbl= Label(bg_img,text="FACE RECOGNITION ATTENDANCE APPLICATION",font=("times new roman",35,"bold"),bg="white",fg="red") 
                tilte_lbl.place(x=0,y=0,width=1530,height=45)


        #=====adding time=======
                def time():
                     string =strftime('%H:%M:%S %p')   #take the current time
                     lb1.config(text=string)
                     lb1.after(1000,time)

                lb1 = Label(tilte_lbl,font=('times new roman',14,'bold'),background='white',fg='blue') #make tabel to show time
                lb1.place(x=0,y=0,width=110,height=50) #place the time

                time() #make a call to time function


        #====set button 1(student details) image =======
                img5=Image.open(r"image\img5.jpg")
                img5=img5.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg5=ImageTk.PhotoImage(img5)

        #======show button 1 image in window=====
                b1 =Button(bg_img,image=self.photoimg5,command=self.student_detail,cursor="hand2")
                b1.place(x=200,y=100,width=200,height=200)
        #======show button 1 text in window======
                b1_1=Button(bg_img,text="Student Details",command=self.student_detail,font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2")
                b1_1.place(x=200,y=300,width=200,height=38)


        #====set button 2(detect face) image =======
                img6=Image.open(r"image\img6.jpeg")
                img6=img6.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg6=ImageTk.PhotoImage(img6)

        #======show button 2 image in window=====
                b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.face_data)
                b2.place(x=500,y=100,width=200,height=200)
        #======show button 2 text in window======
                b2_1=Button(bg_img,text="Give Attendance",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.face_data)
                b2_1.place(x=500,y=300,width=200,height=38)


        #====set button 3(Attendance) image =======
                img7=Image.open(r"image\img7.jpg")
                img7=img7.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg7=ImageTk.PhotoImage(img7)

        #======show button 3 image in window=====
                b3=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.attendance_data)
                b3.place(x=800,y=100,width=200,height=200)
        #======show button 3 text in window======
                b3_1=Button(bg_img,text="See Attendence",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.attendance_data)
                b3_1.place(x=800,y=300,width=200,height=38)



        #====set button 4(help) image =======
                img8=Image.open(r"image\img8.png")
                img8=img8.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg8=ImageTk.PhotoImage(img8)

        #======show button 4 image in window=====
                b4=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.help_data)
                b4.place(x=1100,y=100,width=200,height=200)
        #======show button 4 text in window======
                b4_1=Button(bg_img,text="Help",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.help_data)
                b4_1.place(x=1100,y=300,width=200,height=38)



        #====set button 5(Train Data) image =======
                img9=Image.open(r"image\img9.jpg")
                img9=img9.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg9=ImageTk.PhotoImage(img9)

        #======show button 5 image in window=====
                b5=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.train_data)
                b5.place(x=200,y=370,width=200,height=200)
        #======show button 5 text in window======
                b5_1=Button(bg_img,text="Train Data",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.train_data)
                b5_1.place(x=200,y=570,width=200,height=38)

        #====set button 6(Photos) image =======
                img10=Image.open(r"image\img10.jpg")
                img10=img10.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg10=ImageTk.PhotoImage(img10)

        #======show button 6 image in window=====
                b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
                b6.place(x=500,y=370,width=200,height=200)
        #======show button 6 text in window======
                b6_1=Button(bg_img,text="Photos",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.open_img)
                b6_1.place(x=500,y=570,width=200,height=38)


        #====set button 7(Developer) image =======
                img11=Image.open(r"image\game.jpg")
                img11=img11.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg11=ImageTk.PhotoImage(img11)
        #======show button 7 image in window=====
                b7=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.games_data)
                b7.place(x=800,y=370,width=200,height=200)
        #======show button 7 text in window======
                b7_1=Button(bg_img,text="Funny Games",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.games_data)
                b7_1.place(x=800,y=570,width=200,height=38)



        #====set button 8(Exit) image =======
                img12=Image.open(r"image\img12.png")
                img12=img12.resize((230,230),Image.ANTIALIAS)#resise and convert high level img to low level img
                self.photoimg12=ImageTk.PhotoImage(img12)

        #======show button 8 image in window=====
                b8=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.exit)
                b8.place(x=1100,y=370,width=200,height=200)
        #======show button 8 text in window======
                b8_1=Button(bg_img,text="Exit",font=("times new roman",20,"bold"),bg="white",fg="red",cursor="hand2",command=self.exit)
                b8_1.place(x=1100,y=570,width=200,height=38)
        
    
    
        def open_img(self):
                os.startfile("data")
        


#===making the sudent detail function button call======        
        def student_detail(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Student(self.new_window)


#===making the photo sample train=====
        def train_data(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Train(self.new_window)

#===making the face recognition =====
        def face_data(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Face_Recognition(self.new_window)

#===making the face attendance =====
        def attendance_data(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Attendance(self.new_window)

#===making the help button =====
        def help_data(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Help(self.new_window)    

#===making the games button =====
        def games_data(self):
                self.new_window=Toplevel(self.root) #new window to on the top of old window
                self.app=Games(self.new_window)     

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
    obj=Face_Recognition_System(root)
    root.mainloop()