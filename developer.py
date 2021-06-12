from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from cv2 import cv2

class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")  

        #img 1
        img = Image.open(r"img\developerHeader.jpg")
        img = img.resize((1530,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=150)

        #main frame
        main_frame = Frame(self.root,bd=2,bg="white")
        main_frame.place(x=550,y=200,width=500,height=500 )

        dev_img = Image.open(r"img\arvind_pic.jpg")
        dev_img = dev_img.resize((200,200),Image.ANTIALIAS)
        self.photo_dev_img = ImageTk.PhotoImage(dev_img)

        f_lbl_img = Label( main_frame,image = self.photo_dev_img)
        f_lbl_img.place(x=150,y=0,width=200,height=200)

        #developer info
        dev_label = Label(main_frame, text="Project Name: Face Recognition Student Attendance System",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=210)

        dev_label = Label(main_frame, text="Name: Arvind Vishwakarma",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=255)

        dev_label = Label(main_frame, text="Course: Master in Computer Application",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=300)

        dev_label = Label(main_frame, text="Semester: 6th Sem",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=345)

        dev_label = Label(main_frame, text="Department: Department of Computer Application",font=("times new roman",12,"bold"),bg="white")
        dev_label.place(x=0,y=390)

        


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()