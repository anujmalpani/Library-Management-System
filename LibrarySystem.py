#Module Imports
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image, ImageTk
import mysql.connector as a
from mysql.connector import Error
#Mysql Connection and Table Setup Query
con=a.connect(host="localhost",user="root",passwd="ANUJ",database="Library")
try:
    c=con.cursor()
    c.execute('''create table BookIssue(Name varchar(60),Bookcode varchar(50),
              Bookname varchar(60),Date varchar(10),
              Deposit_status varchar(50)); ''')
    con.commit()
except(Error):
    print("",end="")
try:
    c=con.cursor()
    c.execute('''create table BookDeposit(Name varchar(60),
               Bookcode varchar(50),Bookname varchar(60),
               Date varchar(10));''')
    con.commit()
except(Error):
    print("",end="")
try:
    c=con.cursor()
    c.execute('''create table Bookinfo(Bookname varchar(60),
               Authorname varchar(60),Book_code varchar(50) primary key,
               Total integer(20),Subject varchar(60));
              ''')
    con.commit()
except(Error):
    print("",end="")
try:
    c=con.cursor()
    c.execute('''create table Student(Name varchar(60),Mobile_No char(20),
               Email_ID  varchar(50) primary key,
               Aadhar_No char(50) unique,LibraryID varchar(50) unique);''')
    con.commit()
except(Error):
    print("",end="")
#GUI Window Generation 
LMS=tk.Tk()
LMS.title("Library Management System")
#window size 
screen_width = LMS.winfo_screenwidth()
screen_height = LMS.winfo_screenheight()
LMS.geometry(f"{screen_width}x{screen_height}")
x=screen_width
y=screen_height
#Book Issue Button Function
def bookissue():
    BI=tk.Toplevel(LMS) 
    BI.title("Book Issue Record")
    screen_width = BI.winfo_screenwidth()
    screen_height = BI.winfo_screenheight()
    x=screen_width
    y=screen_height
    BI.geometry(f"{screen_width}x{screen_height}")
    #Navigation
    Nav=Label(BI,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="BOOK ISSUE RECORD ENTRY")
    Nav.pack()
    #Outer Body Frame
    Outerframe=Frame(BI,width=x,height=((16*y)//20),bg="brown")
    Outerframe.pack()
    #Inner Body Frame
    Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
    Innerframe.place(x=140,y=22)
    #String Variables Declaration
    va=tk.StringVar()
    vb=tk.StringVar()
    vc=tk.StringVar()
    vd=tk.StringVar()
    ve=tk.StringVar()
    #Input Student Name
    L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Student Name")
    L1.place(x=50,y=40)
    E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
    E1.place(x=400,y=40)
    #Input Book Code
    L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Code")
    L2.place(x=50,y=120)
    E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
    E2.place(x=400,y=120)
    #Input Book Name
    L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Name")
    L3.place(x=50,y=200)
    E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
    E3.place(x=400,y=200)
    #Input Issue Date
    L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Date of Issue")
    L4.place(x=50,y=280)
    E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
    E4.place(x=400,y=280)
    #Input Deposit Status
    L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Deposit Status")
    L5.place(x=50,y=360)
    E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
    E5.place(x=400,y=360)
    #Clear Button Function
    def clear():
         E1.delete(0,tk.END)
         E2.delete(0,tk.END)
         E3.delete(0,tk.END)
         E4.delete(0,tk.END)
         E5.delete(0,tk.END)
    #Submit Button Function
    def submit():
        N=(va.get()).lower()
        CO=(vb.get()).lower()
        BN=(vc.get()).lower()
        D=(vd.get()).lower()
        DS=(ve.get()).lower()
        if(N=="" or CO=="" or BN=="" or D=="" or DS==""):
            messagebox.showwarning("Empty Set:Cant Insert",parent=BI)
        else:
            a="insert into BookIssue values(%s,%s,%s,%s,%s);"
            data=(N,CO,BN,D,DS)
            c=con.cursor()
            c.execute(a,data)
            con.commit()
            messagebox.showinfo("Record Inserted Successfully",parent=BI)
    #Exit Button Function
    def exitapp():
        BI.destroy()
    #Clear Input Button
    CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
    CB.place(x=300,y=500)
    #Submit Input Button
    SB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Submit",command=submit)
    SB.place(x=520,y=500)
    #Exit Window Button
    EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
    EB.place(x=740,y=500)
#Book Return Button Function
def bookdeposit():
    BD=tk.Toplevel(LMS) 
    BD.title("Book Return Record")
    screen_width = BD.winfo_screenwidth()
    screen_height = BD.winfo_screenheight()
    x=screen_width
    y=screen_height
    BD.geometry(f"{screen_width}x{screen_height}")
    #Navigation
    Nav=Label(BD,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="BOOK RETURN RECORD ENTRY")
    Nav.pack()
    #Outer Body Frame
    Outerframe=Frame(BD,width=x,height=((16*y)//20),bg="brown")
    Outerframe.pack()
    #Inner Body Frame
    Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
    Innerframe.place(x=140,y=22)
    #String Variables Declaration
    va=tk.StringVar()
    vb=tk.StringVar()
    vc=tk.StringVar()
    vd=tk.StringVar()
    ve=tk.StringVar()
    #Input Student Name
    L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Student Name")
    L1.place(x=50,y=40)
    E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
    E1.place(x=400,y=40)
    #Input Book Code
    L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Code")
    L2.place(x=50,y=120)
    E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
    E2.place(x=400,y=120)
    #Input Book Name
    L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Name")
    L3.place(x=50,y=200)
    E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
    E3.place(x=400,y=200)
    #Input Return Date
    L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Date of Return")
    L4.place(x=50,y=280)
    E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
    E4.place(x=400,y=280)
    #Input Deposit Status
    L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Deposit Status")
    L5.place(x=50,y=360)
    E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
    E5.place(x=400,y=360)
    #Clear Button Function
    def clear():
         E1.delete(0,tk.END)
         E2.delete(0,tk.END)
         E3.delete(0,tk.END)
         E4.delete(0,tk.END)
         E5.delete(0,tk.END)
    #Submit Button Function
    def submit():
        N=(va.get()).lower()
        CO=(vb.get()).lower()
        BN=(vc.get()).lower()
        D=(vd.get()).lower()
        DS=(ve.get()).lower()
        if(N=="" or CO=="" or BN=="" or D=="" or DS==""):
            messagebox.showwarning("Empty Set:Cant Insert",parent=BD)
        else:
            c=con.cursor() 
            a='''update BookIssue set Deposit_status=%s where Name=%s and Bookcode=%s
            and Bookname=%s;'''
            data1=(DS,N,CO,BN)
            c.execute(a,data1)
            con.commit()
            b='''insert into BookDeposit values(%s,%s,%s,%s);'''
            data2=(N,CO,BN,D)
            c=con.cursor()
            c.execute(b,data2)
            con.commit()
            messagebox.showinfo("Record Inserted Successfully",parent=BD)
    #Exit Button Function
    def exitapp():
        BD.destroy()
    #Clear Input Button
    CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
    CB.place(x=300,y=500)
    #Submit Input Button
    SB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Submit",command=submit)
    SB.place(x=520,y=500)
    #Exit Window Button
    EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
    EB.place(x=740,y=500)
#Exit Button Function
def exitapp():
    LMS.destroy()
#Admin Menu Button Function
def admin():
    AM=tk.Toplevel(LMS) 
    AM.title("Administration Menu")
    screen_width = AM.winfo_screenwidth()
    screen_height = AM.winfo_screenheight()
    x=screen_width
    y=screen_height
    AM.geometry(f"{screen_width}x{screen_height}")
    #Navigation
    Nav=Label(AM,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="ADMINISTRATION MENU")
    Nav.pack()
    #Outer Body Frame
    Outerframe=Frame(AM,width=x,height=((16*y)//20),bg="brown")
    Outerframe.pack()
    #Inner Body Frame
    Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
    Innerframe.place(x=140,y=22)
    #Button Function Row 1 B1
    def sturecord():
        SR=tk.Toplevel(AM) 
        SR.title("Student Record")
        screen_width = SR.winfo_screenwidth()
        screen_height = SR.winfo_screenheight()
        x=screen_width
        y=screen_height
        SR.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(SR,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="STUDENT RECORD ENTRY")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(SR,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)  
        #String Variables Declaration
        va=tk.StringVar()
        vb=tk.StringVar()
        vc=tk.StringVar()
        vd=tk.StringVar()
        ve=tk.StringVar()
        #Input Student Name
        L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Student Name")
        L1.place(x=50,y=40)
        E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
        E1.place(x=400,y=40)
        #Input Mobile Number
        L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Mobile No.")
        L2.place(x=50,y=120)
        E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
        E2.place(x=400,y=120)
        #Input Email Id
        L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Email Id")
        L3.place(x=50,y=200)
        E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
        E3.place(x=400,y=200)
        #Input Aadhar Number
        L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Aadhar Number")
        L4.place(x=50,y=280)
        E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
        E4.place(x=400,y=280)
        #Input LibraryID
        L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Library ID")
        L5.place(x=50,y=360)
        E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
        E5.place(x=400,y=360)
        #Clear Button Function
        def clear():
            E1.delete(0,tk.END)
            E2.delete(0,tk.END)
            E3.delete(0,tk.END)
            E4.delete(0,tk.END)
            E5.delete(0,tk.END)
        #Submit Button Function
        def submit():
            N=(va.get()).lower()
            M=(vb.get()).lower()
            E=(vc.get()).lower()
            ADH=(vd.get()).lower()
            LID=(ve.get()).lower()
            if(N=="" or M=="" or E=="" or ADH=="" or LID==""):
                messagebox.showwarning("Empty Set:Cant Insert",parent=SR)
            else:
                a="insert into Student values(%s,%s,%s,%s,%s);"
                data=(N,M,E,ADH,LID)
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Inserted Successfully",parent=SR)
        #Exit Button Function
        def exitapp():
            SR.destroy()
        #Clear Input Button
        CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
        CB.place(x=300,y=500)
        #Submit Input Button
        SB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Submit",command=submit)
        SB.place(x=520,y=500)
        #Exit Window Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
        EB.place(x=740,y=500)
    #Button Function Row 1 B4
    def modifystudent():
        MSR=tk.Toplevel(AM) 
        MSR.title("Modify Student Record")
        screen_width = MSR.winfo_screenwidth()
        screen_height = MSR.winfo_screenheight()
        x=screen_width
        y=screen_height
        MSR.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(MSR,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="MODIFY STUDENT RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(MSR,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #String Variables Declaration
        va=tk.StringVar()
        vb=tk.StringVar()
        vc=tk.StringVar()
        vd=tk.StringVar()
        ve=tk.StringVar()
        #Input Student Name
        L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Student Name")
        L1.place(x=50,y=40)
        E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
        E1.place(x=400,y=40)
        #Input Mobile Number
        L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Mobile No.")
        L2.place(x=50,y=120)
        E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
        E2.place(x=400,y=120)
        #Input Email Id
        L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Email Id")
        L3.place(x=50,y=200)
        E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
        E3.place(x=400,y=200)
        #Input Aadhar Number
        L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Aadhar Number")
        L4.place(x=50,y=280)
        E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
        E4.place(x=400,y=280)
        #Input LibraryID
        L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Library ID")
        L5.place(x=50,y=360)
        E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
        E5.place(x=400,y=360)
        #Clear Button Function
        def clear():
            E1.delete(0,tk.END)
            E2.delete(0,tk.END)
            E3.delete(0,tk.END)
            E4.delete(0,tk.END)
            E5.delete(0,tk.END)
        #Update Button Function
        def update():
            N=(va.get()).lower()
            M=(vb.get()).lower()
            E=(vc.get()).lower()
            ADH=(vd.get()).lower()
            LID=(ve.get()).lower()
            if(N=="" or M=="" or E=="" or ADH=="" or LID==""):
                messagebox.showwarning("Empty Set:Cant Update",parent=MSR)
            else:
                a='''update Student set Name=%s,Mobile_No=%s,Email_ID=%s,
                     Aadhar_No=%s where LibraryID=%s;'''
                data=(N,M,E,ADH,LID)
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Updated Successfully",parent=MSR)
        #Exit Button Function
        def exitapp():
            MSR.destroy()
        #Clear Input Button
        CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
        CB.place(x=300,y=500)
        #Update Input Button
        UB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Update",command=update)
        UB.place(x=520,y=500)
        #Exit Window Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
        EB.place(x=740,y=500)
    #Button Function Row 1 B2
    def showstudent():
        DS=tk.Toplevel(AM) 
        DS.title("Display Student Record")
        screen_width = DS.winfo_screenwidth()
        screen_height = DS.winfo_screenheight()
        x=screen_width
        y=screen_height
        DS.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DS,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY STUDENT RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DS,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        a="select * from Student;"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        temp=[]
        if(myresult==temp):
            messagebox.showinfo("Empty Set",parent=DS)
        else:
            columns=[desc[0] for desc in c.description]
            DT["columns"] = columns
            DT["show"] = "headings"
            for col in columns:
                DT.heading(col, text=col)
                DT.column(col, width=150, anchor="center")
            for row in myresult:
                DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DS.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=500,y=530)
    #Button Function Row 1 B3
    def specificstudent():
        DSS=tk.Toplevel(AM) 
        DSS.title("Display Specific Student Record")
        screen_width = DSS.winfo_screenwidth()
        screen_height = DSS.winfo_screenheight()
        x=screen_width
        y=screen_height
        DSS.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DSS,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY SPECIFIC STUDENT RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DSS,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        #Display Button Function
        def show():
            Input=simpledialog.askstring("Input","Enter Library-ID",parent=DSS)
            a="select * from Student where LibraryID=%s;"
            data=(Input,)
            c=con.cursor()
            c.execute(a,data)
            myresult=c.fetchall()
            temp=[]
            if(myresult==temp):
                messagebox.showinfo("Empty Set",parent=DSS)
            else:
                columns=[desc[0] for desc in c.description]
                DT["columns"] = columns
                DT["show"] = "headings"
                for col in columns:
                    DT.heading(col, text=col)
                    DT.column(col, width=150, anchor="center")
                for row in myresult:
                    DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DSS.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=400,y=530)
        #Display Button
        DB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="display",command=show)
        DB.place(x=650,y=530)
    #Menu Buttons Row 1
    B1=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Create Student Record",command=sturecord)
    B1.place(x=80,y=80)
    B2=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Display Student Record",command=showstudent)
    B2.place(x=350,y=80)
    B3=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Specific Student Record",command=specificstudent)
    B3.place(x=620,y=80)
    B4=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Modify Student Record",command=modifystudent)
    B4.place(x=890,y=80)
    #Button Function Row 2 B5
    def addbook():
        BR=tk.Toplevel(AM) 
        BR.title("Book Record")
        screen_width = BR.winfo_screenwidth()
        screen_height = BR.winfo_screenheight()
        x=screen_width
        y=screen_height
        BR.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(BR,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="BOOK RECORD ENTRY")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(BR,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #String Variables Declaration
        va=tk.StringVar()
        vb=tk.StringVar()
        vc=tk.StringVar()
        vd=tk.IntVar()
        ve=tk.StringVar()
        #Input Book Name
        L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Name")
        L1.place(x=50,y=40)
        E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
        E1.place(x=400,y=40)
        #Input Author Name
        L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Author Name")
        L2.place(x=50,y=120)
        E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
        E2.place(x=400,y=120)
        #Input Book Code
        L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Code")
        L3.place(x=50,y=200)
        E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
        E3.place(x=400,y=200)
        #Input Total
        L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Total No.")
        L4.place(x=50,y=280)
        E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
        E4.place(x=400,y=280)
        #Input Subject
        L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Subject")
        L5.place(x=50,y=360)
        E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
        E5.place(x=400,y=360)
        #Clear Button Function
        def clear():
            E1.delete(0,tk.END)
            E2.delete(0,tk.END)
            E3.delete(0,tk.END)
            E4.delete(0,tk.END)
            E5.delete(0,tk.END)
        #Submit Button Function
        def submit():
            BN=(va.get()).lower()
            BA=(vb.get()).lower()
            CO=(vc.get()).lower()
            T=vd.get()
            S=(ve.get()).lower()
            if(BN=="" or BA=="" or CO=="" or S==""):
                messagebox.showwarning("Empty Set:Cant Insert",parent=BR)
            else:
                data=(BN,BA,CO,T,S)
                a="insert into Bookinfo values(%s,%s,%s,%s,%s);"
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Inserted Successfully",parent=BR)
        #Exit Button Function
        def exitapp():
            BR.destroy()
        #Clear Input Button
        CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
        CB.place(x=300,y=500)
        #Submit Input Button
        SB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Submit",command=submit)
        SB.place(x=520,y=500)
        #Exit Window Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
        EB.place(x=740,y=500)
    #Button Function Row 2 B8
    def modifybook():
        MBR=tk.Toplevel(AM) 
        MBR.title("Modify Book Record")
        screen_width = MBR.winfo_screenwidth()
        screen_height = MBR.winfo_screenheight()
        x=screen_width
        y=screen_height
        MBR.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(MBR,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="MODIFY BOOK RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(MBR,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #String Variables Declaration
        va=tk.StringVar()
        vb=tk.StringVar()
        vc=tk.StringVar()
        vd=tk.IntVar()
        ve=tk.StringVar()
        #Input Book Name
        L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Name")
        L1.place(x=50,y=40)
        E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
        E1.place(x=400,y=40)
        #Input Author Name
        L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Author Name")
        L2.place(x=50,y=120)
        E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
        E2.place(x=400,y=120)
        #Input Book Code
        L3=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Code")
        L3.place(x=50,y=200)
        E3=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vc)
        E3.place(x=400,y=200)
        #Input Total
        L4=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Total No.")
        L4.place(x=50,y=280)
        E4=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vd)
        E4.place(x=400,y=280)
        #Input Subject
        L5=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Subject")
        L5.place(x=50,y=360)
        E5=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=ve)
        E5.place(x=400,y=360)
        #Clear Button Function
        def clear():
            E1.delete(0,tk.END)
            E2.delete(0,tk.END)
            E3.delete(0,tk.END)
            E4.delete(0,tk.END)
            E5.delete(0,tk.END)
        #Submit Button Function
        def update():
            BN=(va.get()).lower()
            BA=(vb.get()).lower()
            CO=(vc.get()).lower()
            T=vd.get()
            S=(ve.get()).lower()
            if(BN=="" or BA=="" or CO=="" or S==""):
                messagebox.showwarning("Empty Set:Cant Update",parent=MBR)
            else:
                data=(BN,BA,T,S,CO)
                a='''update Bookinfo set Bookname=%s,Authorname=%s,
                     Total=%s,Subject=%s where Book_code=%s;'''
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Updated Successfully",parent=MBR)
        #Exit Button Function
        def exitapp():
            MBR.destroy()
        #Clear Input Button
        CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Clear",command=clear)
        CB.place(x=300,y=500)
        #Update Input Button
        UB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Update",command=update)
        UB.place(x=520,y=500)
        #Exit Window Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
        EB.place(x=740,y=500)
    #Button Function Row 2 B6
    def showbook():
        DB=tk.Toplevel(AM) 
        DB.title("Display Book Record")
        screen_width = DB.winfo_screenwidth()
        screen_height = DB.winfo_screenheight()
        x=screen_width
        y=screen_height
        DB.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DB,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY BOOK RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DB,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        a="select * from Bookinfo;"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        temp=[]
        if(myresult==temp):
            messagebox.showinfo("Empty Set",parent=DB)
        else:
            columns=[desc[0] for desc in c.description]
            DT["columns"] = columns
            DT["show"] = "headings"
            for col in columns:
                DT.heading(col, text=col)
                DT.column(col, width=150, anchor="center")
            for row in myresult:
                DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DB.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=500,y=530)
    #Button Function Row 2 B7
    def specificbook():
        DSB=tk.Toplevel(AM) 
        DSB.title("Display Specific Book Record")
        screen_width = DSB.winfo_screenwidth()
        screen_height = DSB.winfo_screenheight()
        x=screen_width
        y=screen_height
        DSB.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DSB,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY SPECIFIC BOOK RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DSB,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        #Display Button Function
        def show():
            Input=simpledialog.askstring("Input","Enter Book-Code",parent=DSB)
            a="select * from Bookinfo where Book_code=%s;"
            data=(Input,)
            c=con.cursor()
            c.execute(a,data)
            myresult=c.fetchall()
            temp=[]
            if(myresult==temp):
                messagebox.showinfo("Empty Set",parent=DSB)
            else:
                columns=[desc[0] for desc in c.description]
                DT["columns"] = columns
                DT["show"] = "headings"
                for col in columns:
                    DT.heading(col, text=col)
                    DT.column(col, width=150, anchor="center")
                for row in myresult:
                    DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DSB.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=400,y=530)
        #Display Button
        DB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="display",command=show)
        DB.place(x=650,y=530)
    #Menu Buttons Row 2
    B5=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Create Book Record",command=addbook)
    B5.place(x=80,y=210)
    B6=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Display Book Record",command=showbook)
    B6.place(x=350,y=210)
    B7=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Specific Book Record",command=specificbook)
    B7.place(x=620,y=210)
    B8=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Modify Book Record",command=modifybook)
    B8.place(x=890,y=210)
    #Button Function Row 3 B12
    def deleterecord():
        DR=tk.Toplevel(AM) 
        DR.title("Delete Book/Student Record")
        screen_width = DR.winfo_screenwidth()
        screen_height = DR.winfo_screenheight()
        x=screen_width
        y=screen_height
        DR.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DR,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DELETE BOOK/STUDENT RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DR,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #String Variables Declaration
        va=tk.StringVar()
        vb=tk.StringVar()
        #Input Book Code
        L1=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Book Code")
        L1.place(x=50,y=40)
        E1=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=va)
        E1.place(x=400,y=40)
        #Function
        def deletebook():
            CO=(va.get()).lower()
            if(CO==""):
                messagebox.showwarning("Can't delete",parent=DR)
            else:
                a="delete from Bookinfo where Book_code=%s;"
                data=(CO,)
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Deleted Successfully",parent=DR)
        #Delete Button
        DB1=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="delete book record",command=deletebook)
        DB1.place(x=520,y=150)
        #Input Library ID
        L2=Label(Innerframe,width=x//80,bg="white",fg="black",font=("Arial",20,"bold"),text="Library ID")
        L2.place(x=50,y=270)
        E2=Entry(Innerframe,bd=10,bg="white",fg="black",width=x//40,font=("Arial",20,"bold"),textvariable=vb)
        E2.place(x=400,y=270)
        #Function
        def deletestudent():
            LID=(vb.get()).lower()
            if(LID==""):
                messagebox.showwarning("Can't delete",parent=DR)
            else:
                a="delete from Student where LibraryID=%s;"
                data=(LID,)
                c=con.cursor()
                c.execute(a,data)
                con.commit()
                messagebox.showinfo("Record Deleted Successfully",parent=DR)
        #Delete Button
        DB2=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="delete student record",command=deletestudent)
        DB2.place(x=520,y=380)
        #Clear Button Function
        def clear():
            E1.delete(0,tk.END)
            E2.delete(0,tk.END)
        #Clear Button
        CB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="clear",command=clear)
        CB.place(x=50,y=500)
        #Exit Button Function
        def exitapp():
            DR.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=990,y=500)
    #Button Function Row 3 B9
    def displaybookissue():
        DBI=tk.Toplevel(AM) 
        DBI.title("Display Bookissue Record")
        screen_width = DBI.winfo_screenwidth()
        screen_height = DBI.winfo_screenheight()
        x=screen_width
        y=screen_height
        DBI.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DBI,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY BOOKISSUE RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DBI,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        a="select * from BookIssue;"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        temp=[]
        if(myresult==temp):
            messagebox.showinfo("Empty Set",parent=DBI)
        else:
            columns=[desc[0] for desc in c.description]
            DT["columns"] = columns
            DT["show"] = "headings"
            for col in columns:
                DT.heading(col, text=col)
                DT.column(col, width=150, anchor="center")
            for row in myresult:
                DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DBI.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=500,y=530)
    #Button Function Row 3 B10
    def displaybookreturn():
        DBD=tk.Toplevel(AM) 
        DBD.title("Display Bookreturn Record")
        screen_width = DBD.winfo_screenwidth()
        screen_height = DBD.winfo_screenheight()
        x=screen_width
        y=screen_height
        DBD.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DBD,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY BOOKRETURN RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DBD,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        a="select * from BookDeposit;"
        c=con.cursor()
        c.execute(a)
        myresult=c.fetchall()
        temp=[]
        if(myresult==temp):
            messagebox.showinfo("Empty Set",parent=DBD)
        else:
            columns=[desc[0] for desc in c.description]
            DT["columns"] = columns
            DT["show"] = "headings"
            for col in columns:
                DT.heading(col, text=col)
                DT.column(col, width=150, anchor="center")
            for row in myresult:
                DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DBD.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=500,y=530)
    #Button Function Row 3 B11
    def specificbookissue():
        DBI=tk.Toplevel(AM) 
        DBI.title("Display Specific Bookissue Record")
        screen_width = DBI.winfo_screenwidth()
        screen_height = DBI.winfo_screenheight()
        x=screen_width
        y=screen_height
        DBI.geometry(f"{screen_width}x{screen_height}")
        #Navigation
        Nav=Label(DBI,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="DISPLAY SPECIFIC BOOKISSUE RECORD")
        Nav.pack()
        #Outer Body Frame
        Outerframe=Frame(DBI,width=x,height=((16*y)//20),bg="brown")
        Outerframe.pack()
        #Inner Body Frame
        Innerframe=Frame(Outerframe,width=((4*x)//5),height=((28*y)//40),bg="black")
        Innerframe.place(x=140,y=22)
        #Table Setup
        DT=ttk.Treeview(Innerframe)
        DT.place(x=60,y=10,relwidth=0.9,relheight=0.85)
        #Scroll Setup
        scrollbar=ttk.Scrollbar(Innerframe, orient="vertical", command=DT.yview)
        DT.configure(yscrollcommand=scrollbar.set)
        def place_scrollbar():
            scrollbar.place(x=60+int(0.9*Innerframe.winfo_width())-2,y=10,
            width=15,height=int(0.85*Innerframe.winfo_height()))
        Innerframe.after(100, place_scrollbar)
        #Display Button Function
        def show():
            Input=simpledialog.askstring("Input","Enter Student Name",parent=DBI)
            a="select * from BookIssue where Name=%s;"
            data=(Input,)
            c=con.cursor()
            c.execute(a,data)
            myresult=c.fetchall()
            temp=[]
            if(myresult==temp):
                messagebox.showinfo("Empty Set",parent=DBI)
            else:
                columns=[desc[0] for desc in c.description]
                DT["columns"] = columns
                DT["show"] = "headings"
                for col in columns:
                    DT.heading(col, text=col)
                    DT.column(col, width=150, anchor="center")
                for row in myresult:
                    DT.insert("", "end", values=row)
        #Exit Button Function
        def exitapp():
            DBI.destroy()
        #Exit Button
        EB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="exit",command=exitapp)
        EB.place(x=400,y=530)
        #Display Button
        DB=Button(Innerframe,width=x//100,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="display",command=show)
        DB.place(x=650,y=530)
    #Menu Button Row 3
    B9=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Show Bookissue Record",command=displaybookissue)
    B9.place(x=80,y=340)
    B10=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Show Bookreturn Record",command=displaybookreturn)
    B10.place(x=350,y=340)
    B11=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Specific Issue Record",command=specificbookissue)
    B11.place(x=620,y=340)
    B12=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Delete Record",command=deleterecord)
    B12.place(x=890,y=340)
    #Exit Button Function
    def exitapp():
        AM.destroy()
    #Exit Button 
    EB=Button(Innerframe,width=x//80,height=y//300,bg="brown",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
    EB.place(x=490,y=480)
#navbar
Nav=Label(LMS,width=x,height=y//220,bg="black",fg="white",font=("Arial",28,"bold"),text="WELCOME TO LIBRARY DASHBOARD")
Nav.pack()
#image container
img_width = x
img_height = y // 2
original_image = Image.open(r"C:\Users\anujm\OneDrive\Desktop\AUR\Python\LMSimage.png")
resized_image = original_image.resize((img_width, img_height), Image.LANCZOS)
I1 = ImageTk.PhotoImage(resized_image)
Imagelabel=Label(LMS,width=x,height=y//2,bg="blue",image=I1)
Imagelabel.pack()
#main body frame
Bodyframe=Frame(LMS,width=(10*x),height=(y//7),bg="brown")
Bodyframe.pack()
#Issue Book Button
B1=Button(Bodyframe,width=x//100,height=y//300,bg="black",fg="white",font=("Arial",15,"bold"),text="Issue Book",command=bookissue)
B1.place(x=290,y=25)
#Return Book Button
B2=Button(Bodyframe,width=x//100,height=y//300,bg="black",fg="white",font=("Arial",15,"bold"),text="Return Book",command=bookdeposit)
B2.place(x=540,y=25)
#Administration Menu Button
B3=Button(Bodyframe,width=x//100,height=y//300,bg="black",fg="white",font=("Arial",15,"bold"),text="Admin Menu",command=admin)
B3.place(x=790,y=25)
#Exit Button
B4=Button(Bodyframe,width=x//100,height=y//300,bg="black",fg="white",font=("Arial",15,"bold"),text="Exit",command=exitapp)
B4.place(x=1040,y=25)
#footer content 
Footer=Label(LMS,width=x,height=y//16,bg="black",fg="white",font=("Arial",15,"bold"),text="Library Management System v1.0   |   Developed By Anuj Malpani   |   GUI-Tk[Python]   |   ASET-Amity University Jaipur   |   B.Tech[CSE]")
Footer.pack()
LMS.mainloop()
