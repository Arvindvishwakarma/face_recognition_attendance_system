from tkinter import *
from tkinter import ttk
import tkinter 
from PIL import Image, ImageTk
from student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from face_recognition import Face_Recognition
import os
from time import strftime

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #img 1
        img = Image.open(r"img\header.jpg")
        img = img.resize((1530,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=130)


        #background image
        img3 = Image.open(r"img\background.png")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)



        #student button
        img4 = Image.open(r"img\attendanceEdit.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image = self.photoimg4, command=self.student_details ,cursor="hand2")
        b1.place(x=200,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details ,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=260,width=220,height=40)


        #train button
        img8 = Image.open(r"img\trainingEdit.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, command=self.train_data,cursor="hand2")
        b1.place(x=500,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Train Face", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=260,width=220,height=40)

        #detect face button
        img5 = Image.open(r"img\faceEdit.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5,command=self.face_date, cursor="hand2")
        b1.place(x=800,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Take Attendance", cursor="hand2",command=self.face_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=260,width=220,height=40)


        #attendance button
        img6 = Image.open(r"img\attendanceEdit.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, command=self.attendance_date, cursor="hand2")
        b1.place(x=1100,y=50,width=220,height=220)

        b1_1 = Button(bg_img, text="Attendance System", cursor="hand2",command=self.attendance_date,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=260,width=220,height=40)


        

        #photos button
        img9 = Image.open(r"img\photoEdit.jpg")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, command=self.open_img,cursor="hand2")
        b1.place(x=200,y=350,width=220,height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=560,width=220,height=40)

        
        
        #developer button
        img10 = Image.open(r"img\trainingEdit.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img,command=self.developer_date ,image = self.photoimg10, cursor="hand2")
        b1.place(x=500,y=350,width=220,height=220)

        b1_1 = Button(bg_img,command=self.developer_date, text="Developer", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=560,width=220,height=40)



        #helpdesk button
        img7 = Image.open(r"img\helpEdit.jpg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command=self.help_date ,image = self.photoimg7, cursor="hand2")
        b1.place(x=800,y=350,width=220,height=220)

        b1_1 = Button(bg_img, text="Help Desk", command=self.help_date,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=560,width=220,height=40)


        #exit button
        img11 = Image.open(r"img\exitEdit.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img,command=self.iExit, image = self.photoimg11, cursor="hand2")
        b1.place(x=1100,y=350,width=220,height=220)

        b1_1 = Button(bg_img,command=self.iExit ,text="Exit", cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=560,width=220,height=40)

        # ======== functions buttons ==========


    def open_img(self):
        os.startfile("data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_date(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure exit this project?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()