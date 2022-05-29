# from asyncio import as_completed
import tkinter
import cv2
from matplotlib import pyplot as plt
import numpy as np
from tkinter import*
from tkinter import ttk
# from tkinter.font import BOLD
# from turtle import st
from PIL import Image , ImageTk
from tkinter import messagebox

from scipy.misc import face


class Sketch:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #geometry of the window
        self.root.title("Convert your image to sketch")
        self.root.wm_iconbitmap("face.ico")

        #====set background image =======
        img4=Image.open(r"image\sketch.jpg")
        img4=img4.resize((1530,770),Image.ANTIALIAS)#resise and convert high level img to low level img
        self.photoimg4=ImageTk.PhotoImage(img4)

        #======show backgrond image in window=====
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1530,height=770)

    #===adding frame for buttons=====
        button_Frame=Frame(bg_img,bd=2.5,bg="white",relief=SUNKEN)
        button_Frame.place(x=540,y=500,width=360,height=37)

        #===adding play button=====
        play_button=Button(button_Frame,width=19,command=self.play,text="Make Sketch",font=("times new roman",12,"bold"),bg="green",fg="white")
        play_button.grid(row=0,column=0)

        #===adding exit button=====
        exit_button=Button(button_Frame,width=19,command=self.exit,text="Exit",font=("times new roman",12,"bold"),bg="red",fg="white")
        exit_button.grid(row=0,column=1)


    def play(self):
        def sketch_transform(img):
            img_grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            img_grayscale_blur = cv2.GaussianBlur(img_grayscale,(7,7),0)
            img_canny = cv2.Canny(img_grayscale_blur,10,80)
            _, mask = img_canny_invert = cv2.threshold(img_canny,30,255,cv2.THRESH_BINARY_INV)
            return mask


        video_cap=cv2.VideoCapture(0)
        cv2.destroyAllWindows()

        while True:
            _, im0 = video_cap.read()
            showCrosshair = False
            fromCenter = False
            r = cv2.selectROI("Image", im0, fromCenter, showCrosshair)
            break
                
        while True:   
            _, image_frame = video_cap.read()
            
            rect_img = image_frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
                
            sketcher_rect = rect_img
            sketcher_rect = sketch_transform(sketcher_rect)
                
            #Conversion for 3 channels to put back on original image (streaming)
            sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)
                
            #Replacing the sketched image on Region of Interest
            image_frame[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] = sketcher_rect_rgb
                
            cv2.imshow("Sketcher ROI", image_frame)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
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


#==========calling main============
if __name__=="__main__":
    root=Tk()
    obj=Sketch(root)
    root.mainloop()