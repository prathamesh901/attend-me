from re import search
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
# import mysql.connector
# import cv2
class Student:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        
        #===============variables==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        #baground img
        img3=Image.open("C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\bg2.jpg")
        img3=img3.resize((1500,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=800)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=20,y=135,width=1480,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=185,width=1480,height=600)


        #left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=775,height=580)

        # img_left=Image.open("C:\\Users\\Prathamesh\\Desktop\\attend me\\images\\traindata1.png")
        # img_left=img_left.resize((760,130),Image.ANTIALIAS)
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=760,height=130)


        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=135,width=773,height=115)


        #deparment
        dep_label=Label(current_course_frame,text="DEPARTMENT",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Mechnical","Civil","Electrical","Chemical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)


        #course
        course_label=Label(current_course_frame,text="COURSE",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FY","SY","TY")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)


         #year
        year_label=Label(current_course_frame,text="YEAR",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         #semester
        semester_label=Label(current_course_frame,text="SEMESTER",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","semester-1","semester-2","semester-3","semester-4","semester-5","semester-6","semester-7","semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10)


        
         #classs student information
        class_student_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=250,width=773,height=300)


        #stident id
        studentid_label=Label(class_student_frame,text="STUDENT ID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)


        #student name
        studentName_label=Label(class_student_frame,text="STUDENT NAME:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


         #class division
        class_div_label=Label(class_student_frame,text="CLASS DIVISION:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,sticky=W)

        #dob
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Roll NO
        roll_no_label=Label(class_student_frame,text="ROLL NO:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #gender
        gender_label=Label(class_student_frame,text="GENDER:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email
        email_label=Label(class_student_frame,text="EMAIL:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        #phone no
        phone_label=Label(class_student_frame,text="PHONE NO:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #address
        address_label=Label(class_student_frame,text="ADDRESS:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher name
        teacher_label=Label(class_student_frame,text="TEACHER NAME:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)



        self.var_radio1=StringVar()
        Radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take photo sample",value="yes")
        Radiobtn1.grid(row=6,column=0)
        Radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="no")
        Radiobtn2.grid(row=6,column=1)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=770,height=35)

        save_btn=Button(btn_frame,text="Save",font=("times new roman",13,"bold"),bg="blue",fg="white",width=18)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",font=("times new roman",13,"bold"),bg="blue",fg="white",width=18)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",font=("times new roman",13,"bold"),bg="blue",fg="white",width=19)
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=770,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=80)
        take_photo_btn.grid(row=0,column=0)








        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=805,y=10,width=660,height=580)
    
        # img_right=Image.open("C:\\Users\\Ajinkya\Desktop\\face_recognition system\\college_image\\tk.jpg")
        # img_right=img_right.resize((720,115),Image.ANTIALIAS)
        # self.photoimg_right=ImageTk.PhotoImage(img_right)

        # f_lbl=Label(right_frame,image=self.photoimg_right)
        # f_lbl.place(x=5,y=0,width=720,height=115)

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=120,width=650,height=70)

        
        search_label=Label(search_frame,text="SEARCH BY:",font=("times new roman",12,"bold"),bg="black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No","DOB","Gender","Department","Course","year","Semester","Student Id","Division","Email","Address","teacher_Name","Photo_Sample_Status")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=14,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        showAll_btn.grid(row=0,column=4,padx=4)

        # ========================table frame==========================
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=200,width=650,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1) 
        # self.student_table.bind("<ButtonRelease>",self.get_cursor)
        # self.fetch_data()




if __name__== "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()