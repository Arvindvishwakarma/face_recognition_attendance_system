from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
from cv2 import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System") 

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #header image
        img = Image.open(r"D:\__Programming\opencv\project\img\faceDetectionHeader.jpg")
        img = img.resize((1530,150),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=1530,height=150)


        # click detect

        title_lbl = Label(self.root, text="Click on the 'Take Attendace' button for take aattendence using face recognition", font=("times new roman",20,"bold"),fg="black")
        title_lbl.place(x=0,y=260,width=1530,height=45)

        #button
        b1_1 = Button(self.root, text="Take Attendace",command=self.face_recog, cursor="hand2",font=("times new roman",15,"bold"),bg="green",fg="white")
        b1_1.place(x=615,y=380,width=300,height=60)

 
     #========atendance=============
    def mark_attendance(self, i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")

                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                







    #========face recognition=======
    def face_recog(self):
            def draw_boundary(img,classifier,scaleFactor,minNeighbour,color,tex,clf):
                gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

                coord = []

                for (x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                    confidence = int((100*(1-predict/300)))

                    conn = mysql.connector.connect(host="localhost",user="root",password="arvindgolu@2588",database="face_recognizer",auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()

                    my_cursor.execute("select name from student where student_id ="+str(id))
                    n = my_cursor.fetchone()
                    n ="+".join(n)

                    my_cursor.execute("select roll from student where student_id ="+str(id))
                    r = my_cursor.fetchone()
                    r ="+".join(r)

                    my_cursor.execute("select dep from student where student_id ="+str(id))
                    d = my_cursor.fetchone()
                    d ="+".join(d)

                    my_cursor.execute("select student_id from student where student_id ="+str(id))
                    i = my_cursor.fetchone()
                    i ="+".join(i)

                    if confidence > 77:
                        cv2.putText(img, f"ID:{i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img, f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img, f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        cv2.putText(img, f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        self.mark_attendance(i,r,n,d)
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img, "Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord = [x,y,w,h]
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
                return img
            
            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")


            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                img = recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to face recognition",img)


                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            video_cap.release()
            cv2.destroyAllWindows()    




if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition(root)
    root.mainloop()