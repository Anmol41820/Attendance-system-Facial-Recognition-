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
import numpy as np
from time import strftime
from datetime import datetime

# from scipy.misc import face
# global connection 
# conn=mysql.connector.connect(host='localhost',username='root',password='Isha@41820',database='sys')




class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("face Recognition System")
        self.root.wm_iconbitmap("face.ico")

    #======Adding a tilte box contain the Train Data=======
        tilte_lbl= Label(self.root,text="Train Data",font=("times new roman",35,"bold"),bg="white",fg="green") 
        tilte_lbl.place(x=0,y=0,width=1530,height=45)

        def time():
            string =strftime('%H:%M:%S %p')   #take the current time
            lb1.config(text=string)
            lb1.after(1000,time)

        lb1 = Label(self.root,font=('times new roman',14,'bold'),background='white',fg='blue') #make tabel to show time
        lb1.place(x=0,y=0,width=110,height=50) #place the time

        time() #make a call to time function

    #===adding frame for buttons=====
        button_exit_Frame=Frame(self.root,bd=2.5,bg="white",relief=SUNKEN)
        button_exit_Frame.place(x=1365,y=7,width=150,height=37)
#===adding exit button=====
        exit_button=Button(button_exit_Frame,width=15,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=0)

        top_img=Image.open(r"image\train2.jpg")
        top_img=top_img.resize((1530,325),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.top_photoimg=ImageTk.PhotoImage(top_img)

        #======show left image in window=====
        f_lbl=Label(self.root,image=self.top_photoimg)
        f_lbl.place(x=0,y=50,width=1530,height=320)


    #===adding Trin button=====
        train_button=Button(self.root,text="Click here to train your data",command=self.train_classifier,font=("times new roman",20,"bold"),bg="red",fg="white")
        train_button.place(x=565,y=370)

        

    #====bottom left image=====

        bottom_img=Image.open(r"image\train1.jpg")
        bottom_img=bottom_img.resize((765,325),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.bottom_photoimg=ImageTk.PhotoImage(bottom_img)

        #======show bottom left image in window=====
        f_lbl=Label(self.root,image=self.bottom_photoimg)
        f_lbl.place(x=0,y=420,width=765,height=325)
        
    #====bottom right image=====

        bottom_img1=Image.open(r"image\train3.jpg")
        bottom_img1=bottom_img1.resize((765,325),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.bottom_photoimg1=ImageTk.PhotoImage(bottom_img1)

        #======show bottom rigth image in window=====
        f_lbl=Label(self.root,image=self.bottom_photoimg1)
        f_lbl.place(x=765,y=420,width=765,height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)] #store the path of sample image in variable path

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  #convert img from rgb to gray
            imageNp=np.array(img,'uint8')  #uint8==datatype and conver image to grayscale
            id=int(os.path.split(image)[1].split('.')[1]) #take the id no. from the path
            # print(id)
            faces.append(imageNp) # append faces
            ids.append(id) # append ids
            cv2.imshow("training",imageNp) #show the window on thw top
            cv2.waitKey(1)==13 # close the window on press the enter key
        
        ids=np.array(ids) #pass the ids to numpy


    #=======Now train the classifier and saving the data====
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids) #train
        clf.write("classifier.xml") #write the data in classifier.xml file
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")




            
#===making the exit button =====
    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Attendance Application","Are you sure, you want to exit ?",parent=self.root)
        if self.exit>0:
            self.root.destroy()
        else:
            return
    


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()