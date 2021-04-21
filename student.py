from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")  


        #=============== variables =================

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()








        #img 1
        img = Image.open(r"D:\__Programming\opencv\project\img\BestFacialRecognition.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image = self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #img 2
        img1 = Image.open(r"D:\__Programming\opencv\project\img\university.jpg")
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image = self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130) 

        #img 3
        img2 = Image.open(r"D:\__Programming\opencv\project\img\images.jpg")
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image = self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


         #background image
        img3 = Image.open(r"D:\__Programming\opencv\project\img\dev.jpg")
        img3 = img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root,image = self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman",35,"bold"),bg="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left  label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=1,width=730,height=590)

        img_left = Image.open(r"D:\__Programming\opencv\project\img\girl.jpeg")
        img_left = img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label( Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

                #current course
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=130)

                            #department
        dep_label = Label(current_course_frame, text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10, sticky=W )

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep ,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"] = ("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W) 


                            #course
        course_label = Label(current_course_frame, text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10, sticky=W )

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"] = ("Select Course","MCA","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W) 


                            #year
        year_label = Label(current_course_frame, text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10, sticky=W ) 

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)  
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W) 


                            #semester
        semester_label = Label(current_course_frame, text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10, sticky=W )

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"] = ("Select Semester","Semester-1","Semester-3","Semester-3")
        semester_combo.current(0)  
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W) 


        #Class student information
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=265,width=720,height=300)

                         #stidentId
        studentId_label = Label(class_student_frame, text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10, pady=5, sticky=W )

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10, pady=5, sticky=W)


                        #student name
        studentName_label = Label(class_student_frame, text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10, pady=5, sticky=W )

        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10, pady=5, sticky=W)


                         #class
        class_div_label = Label(class_student_frame, text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10, pady=5, sticky=W )

        class_div_entry = ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10, pady=5, sticky=W)


                        #roll no
        roll_no_label = Label(class_student_frame, text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10, pady=5, sticky=W )

        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10, pady=5, sticky=W)


                        #gender
        gender_label = Label(class_student_frame, text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10, pady=5,sticky=W )

        gender_entry = ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10, pady=5,sticky=W)


                        #dob
        dob_label = Label(class_student_frame, text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10, pady=5,sticky=W )

        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


                        #email
        email_label = Label(class_student_frame, text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5, sticky=W )

        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5, sticky=W)


                        #phone no
        phone_label = Label(class_student_frame, text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5, sticky=W )

        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5, sticky=W)


                         #address
        address_label = Label(class_student_frame, text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5, sticky=W )

        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5, sticky=W)


                         #teacher name
        teacher_label = Label(class_student_frame, text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5, sticky=W )

        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5, sticky=W)


        #radio buttons
        self.var_radios1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radios1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radios1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1)

        #buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=200,width=705,height=70)

        save_btn = Button(btn_frame, text="Save",command=self.add_data,font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame, text="Update",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame, text="Delete",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame, text="Reset",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)

        take_photo_btn = Button(btn_frame, text="Take Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn = Button(btn_frame, text="Update Photo Sample",font=("times new roman",12,"bold"),bg="blue",fg="white",width=19)
        update_photo_btn.grid(row=1,column=1)






        #right  label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE, text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=1,width=720,height=590)

        img_right = Image.open(r"D:\__Programming\opencv\project\img\student.jpg")
        img_right = img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label( Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # ==========search system============

        search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE,text="Search",font=("times new roman",12,"bold"),bg="white")
        search_frame.place(x=5,y=135,width=710,height=70 )

        search_label = Label(search_frame, text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10, pady=5, sticky=W )

        search_combo = ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"] = ("Select","Roll","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10, sticky=W) 


        search_entry = ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn = Button(search_frame, text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=14)
        showAll_btn.grid(row=0,column=4,padx=4 )

        #============table frame=============
        tabel_frame = Frame(Right_frame, bd=2, relief=RIDGE,bg="white")
        tabel_frame.place(x=5,y=210,width=710,height=350)

 
        scroll_x = ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(tabel_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        self.student_table.pack(fill=BOTH,expand=1)


    #============== function declaration ============

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required!!!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",user="root",password="arvindgolu@2588",database="face_recognizer",auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radios1.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)











if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop( )