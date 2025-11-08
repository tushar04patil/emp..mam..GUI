from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class employeee: 
  def  __init__(self,root):
        self.root=root
        self.root.geometry("800x800+0+0")
        self.root.title("hekko demo")

        #varible
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_id=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        self.var_email=StringVar()
        self.var_desi=StringVar()
        self.var_mrr=StringVar()
        self.var_add=StringVar()
       # ("dep","nam","id","gen","dob","doj","phone","country","salary","email","desi","marr","add","sa",
        
        lbl_title=Label(self.root,text="employee management system ",font=("times new roman",37,"bold"),fg="darkblue",bg="white")
        lbl_title.place(x=0,y=0,width=800,height=60)

#logo
        img_logo=Image.open("E:/python/download.png")
        img_logo=img_logo.resize((55,55),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=10,y=0,width=50,height=50)

 # image Frame
        inner_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        inner_frame.place(x=0,y=60,width=800,height=150)
 #img1
        img1=Image.open("E:\python\download (1).jpeg")
        
        img1=img1.resize((300,155),Image.Resampling.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img1=Label(inner_frame,image=self.photo1)
        self.img1.place(x=0,y=0,width=300,height=150)
# #img2
        img2=Image.open("E:\python\download.jpeg")
        img2=img2.resize((300,155),Image.Resampling.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img2=Label(inner_frame,image=self.photo2)
        self.img2.place(x=300,y=0,width=300,height=150)
 # # #img3
        img3=Image.open("E:\python\download.png")
        img3=img3.resize((300,155),Image.Resampling.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img3=Label(inner_frame,image=self.photo3)
        self.img3.place(x=600,y=0,width=300,height=150)
# main frame 2
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        main_frame.place(x=0,y=195,width=800,height=580)

#upper farme in main 
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="employee information",font=("times new roman",10,"bold"),fg="red")
        upper_frame.place(x=0,y=5,width=790,height=270)


 #content in upper farme
        lbl_dep=Label(upper_frame,text="deparment",font=("arial",10,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=20,state="raed only")
        combo_dep["value"]=("select deparment :","HR","SOFTWARE engineer","product manager")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

 #name
        lbl_name=Label(upper_frame,text="name :",font=("arial",10,"bold"),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=26,font=("arial",10,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)


 # email
        lbl_email=Label(upper_frame,text="email :",font=("arial",10,"bold"),bg="white")
        lbl_email.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=19,font=("arial",10,"bold"))
        txt_email.grid(row=0,column=5,padx=2,pady=7)

 # phone no add

        lbl_phone=Label(upper_frame,text="phone no :",font=("arial",10,"bold"),bg="white")
        lbl_phone.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=26,font=("arial",10,"bold"))
        txt_phone.grid(row=1,column=1,padx=2,pady=7)
        
        # designation 

        lbl_desi=Label(upper_frame,text="designation :",font=("arial",10,"bold"),bg="white")
        lbl_desi.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_desi=ttk.Entry(upper_frame,textvariable=self.var_desi,width=26,font=("arial",10,"bold"))
        txt_desi.grid(row=1,column=3,padx=2,pady=7)

        #contry
        lbl_con=Label(upper_frame,text="contry :",font=("arial",10,"bold"),bg="white")
        lbl_con.grid(row=5,column=2,padx=2,pady=7,sticky=W)

        txt_con=ttk.Entry(upper_frame,textvariable=self.var_country,width=20,font=("arial",10,"bold"))
        txt_con.grid(row=5,column=3,padx=2,pady=7)

        #addrest
        lbl_add=Label(upper_frame,text="address :",font=("arial",10,"bold"),bg="white")
        lbl_add.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        txt_add=ttk.Entry(upper_frame,textvariable=self.var_add,width=26,font=("arial",10,"bold"))
        txt_add.grid(row=2,column=3,padx=2,pady=7)

        # marride 
        lbl_add=Label(upper_frame,text="married s:",font=("arial",10,"bold"),bg="white")
        lbl_add.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        combo_add=ttk.Combobox(upper_frame,textvariable=self.var_mrr,font=("times new roman",10,"bold"),width=20,state="raed only")
        combo_add["value"]=("marride","unmarride")
        combo_add.current(0)
        combo_add.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #salaru in upper farim
        lbl_sa=Label(upper_frame,text="salary :",font=("arial",10,"bold"),bg="white")
        lbl_sa.grid(row=5,column=0,padx=2,pady=7,sticky=W)

        txt_sa=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",10,"bold"))
        txt_sa.grid(row=5,column=1,padx=2,pady=7)

        #birth day
        lbl_dob=Label(upper_frame,text="DOB :",font=("arial",10,"bold"),bg="white")
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=25,font=("arial",10,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #doj
        lbl_doj=Label(upper_frame,text="job d. :",font=("arial",10,"bold"),bg="white")
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=26,font=("arial",10,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)


        lbl_add1=Label(upper_frame,text="gender :",font=("arial",10,"bold"),bg="white")
        lbl_add1.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        combo_add1=ttk.Combobox(upper_frame,textvariable=self.var_gen,font=("times new roman",10,"bold"),width=20,state="raed only")
        combo_add1["value"]=("male","female","other")
        combo_add1.current(0)
        combo_add1.grid(row=4,column=1,padx=2,pady=10,sticky=W)

        lbl_add2=Label(upper_frame,text="emp id :",font=("arial",10,"bold"),bg="white")
        lbl_add2.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_dob1=ttk.Entry(upper_frame,textvariable=self.var_id,width=25,font=("arial",10,"bold"))
        txt_dob1.grid(row=4,column=3,padx=2,pady=7)

# upper ke andar chotu phome(save update delete clr)
        Button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        Button_frame.place(x=580,y=40,width=200,height=200)

        btn_add=Button(Button_frame,text="save",font=("times new roman",15,"bold"),width=15,background="blue",fg="white")
        btn_add.grid(row=0,column=0,padx=2,pady=5)

        btn_up=Button(Button_frame,text="update",font=("times new roman",15,"bold"),width=15,background="blue",fg="white")
        btn_up.grid(row=1,column=0,padx=2,pady=5)

        btn_del=Button(Button_frame,text="delete",font=("times new roman",15,"bold"),width=15,background="blue",fg="white")
        btn_del.grid(row=2,column=0,padx=2,pady=5)

        btn_clr=Button(Button_frame,text="clear",font=("times new roman",15,"bold"),width=15,background="blue",fg="white")
        btn_clr.grid(row=3,column=0,padx=2,pady=5)


 #down farmi in main fram
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="employee information table",font=("times new roman",10,"bold"),fg="red")
        down_frame.place(x=0,y=275,width=790,height=270)
# suarch frame 
        surach_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg="white",text="search employee iformation",font=("times new roman",10,"bold"),fg="black")
        surach_frame.place(x=0,y=0,width=785,height=60)

        btn_b1=Label(surach_frame,text="search by",font=("times new roman",15,"bold"),width=10,background="red",fg="white")
        btn_b1.grid(row=0,column=0,padx=1,pady=3)
        
        #comboBox
        combo_a1=ttk.Combobox(surach_frame,font=("times new roman",10,"bold"),width=20,state="raed only")
        combo_a1["value"]=("phone","id __proof ")
        combo_a1.current(0)
        combo_a1.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        txt_do1=ttk.Entry(surach_frame,width=25,font=("arial",10,"bold"))
        txt_do1.grid(row=0,column=2,padx=2,pady=7)

  # button 1 in down fram 
        btn_b5=Button(surach_frame,text="search ",font=("times new roman",15,"bold"),width=10,background="blue",fg="white")
        btn_b5.grid(row=0,column=3,padx=2,pady=5)
 # button 2 in down fram
        btn_b6=Button(surach_frame,text="search all ",font=("times new roman",15,"bold"),width=10,background="blue",fg="white")
        btn_b6.grid(row=0,column=4,padx=2,pady=5)

        #==========student emp table=======
 # thable fram
        table_frame=Frame(down_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=60,width=780,height=180)

        scoll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scoll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(table_frame,columns=("dep","nam","id","gen","dob","doj","phone","country","salary","email","desi","marr","add","sa",),xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)

        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)

        scoll_x.config(command=self.employee_table.xview)
        scoll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("dep",text="pepartment")
        self.employee_table.heading("nam",text="name")
        self.employee_table.heading("id",text="emp_id")
        self.employee_table.heading("gen",text="gender")
        self.employee_table.heading("dob",text="birthday")
        self.employee_table.heading("doj",text="job_d")
        self.employee_table.heading("phone",text="phone_no")
        self.employee_table.heading("country",text="country")
        self.employee_table.heading("salary",text="salary")
        self.employee_table.heading("email",text="email")
        self.employee_table.heading("desi",text="designation")
        self.employee_table.heading("marr",text="marride_s")
        self.employee_table.heading("add",text="address")

        self.employee_table["show"]="headings"
        self.employee_table.column("dep",width=100)
        self.employee_table.column("nam",width=100)
        self.employee_table.column("id",width=100)
        self.employee_table.column("gen",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("desi",width=100)
        self.employee_table.column("marr",width=100)
        self.employee_table.column("add",width=100)

        
        #self.employee_table.pack(fill=BOTH,expand=1)






        
        








 




 #content 
        






        











if __name__=="__main__":
    root=Tk()
    obj=employeee(root)
    root.mainloop()
        