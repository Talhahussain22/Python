from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyodbc

m=Tk()
m.geometry("500x400")
var1=StringVar()
var2=StringVar()
var3=StringVar()
var4=StringVar()
driver=[x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
print(driver)

conncetor = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Admin\Documents\project.accdb'
connect = pyodbc.connect(conncetor)
cursor = connect.cursor()
def clear():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
def display():
    cursor.execute("Select * from Student_p")
    rows=cursor.fetchall()
    i=1
    for row in rows:
            Label(f2,text=row,font=("Arial Black",15)).place(x=5,y=20+i)
            i+=50

def add():
    cursor.execute(f"INSERT INTO Student_p VALUES('{var1.get()}','{var2.get()}','{var3.get()}','{var4.get()}')")
    cursor.commit()
    messagebox.showinfo("One record has been added")

def update():
    cursor.execute(f"UPDATE Student_p SET Address='{var3.get()}' WHERE S_ID={var1.get()}")
    cursor.commit()
    messagebox.showinfo("One record has been UPDATED")

def delete():
    cursor.execute(f"DELETE FROM Student_p WHERE S_ID={var1.get()}")
    cursor.commit()
    messagebox.showinfo("One record has been DELETED")

l1=Label(m, text="Student Management System", bg="orange", fg="black", font=("Arial Black",20))
l1.pack(side=TOP,fill=X)
f1=Frame(bg="lightblue",width=500,height=750)
f1.place(x=0,y=45)
l2=Label(f1,text="S_ID",bg="orange", fg="black",width=10, font=("Arial Black",15)).grid(column=0,row=1,padx=50,pady=20)
l3=Label(f1,text="S_Name",bg="orange", fg="black",width=10, font=("Arial Black",15)).grid(column=0,row=2,padx=50,pady=20)
l4=Label(f1,text="Address",bg="orange", fg="black",width=10, font=("Arial Black",15)).grid(column=0,row=3,padx=50,pady=20)
l5=Label(f1,text="Dept_ID",bg="orange", fg="black",width=10, font=("Arial Black",15)).grid(column=0,row=4,padx=50,pady=20)
l5=Label(f1,text="Program",bg="orange", fg="black",width=10, font=("Arial Black",15)).grid(column=0,row=5,padx=50,pady=20)
e1=Entry(f1,textvariable=var1,font=("Arial Black",15)).grid(column=1,row=1,padx=50,pady=20)
e2=Entry(f1,textvariable=var2,font=("Arial Black",15)).grid(column=1,row=2,padx=50,pady=20)
e3=Entry(f1,textvariable=var3,font=("Arial Black",15)).grid(column=1,row=3,padx=50,pady=20)
e4=Entry(f1,textvariable=var4,font=("Arial Black",15)).grid(column=1,row=4,padx=50,pady=20)

lst=Listbox(f1,bg="grey",fg="white",font=("Arial Black",10))
lst.insert(1,"SE")
lst.insert(2,"CSIT")
lst.insert(3,"EE")
lst.insert(4,"CIS")
lst.grid(column=1,row=5)

b1=Button(f1,text="Display",bg="black",fg="white",font=("Arial Black",15),command=display).grid(column=0,row=10,padx=50,pady=20)
b2=Button(f1,text="Add",bg="black",fg="white",font=("Arial Black",15),command=add).grid(column=1,row=10,padx=50,pady=20)
b3=Button(f1,text="Delete",bg="black",fg="white",font=("Arial Black",15),command=delete).grid(column=0,row=11,padx=50,pady=20)
b4=Button(f1,text="Update",bg="black",fg="white",font=("Arial Black",15),command=update).grid(column=1,row=11,padx=50,pady=20)
b4=Button(f1,text="Clear",bg="red",fg="white",font=("Arial Black",15),command=clear).grid(column=1,row=5,padx=50,pady=20)

f2=Frame(bg="white",width=800,height=750)
f2.place(x=600,y=45)


m.mainloop()