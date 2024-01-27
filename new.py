from tkinter import *
import pyodbc
m=Tk()
connector=r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Admin\Documents\New.accdb'
# conncetor = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Admin\Documents\OPEN_ENDED.accdb'

connect=pyodbc.connect(connector)
cursor=connect.cursor()

def even_odd():
    if(int(e.get())%2)==0:
        l3.config(text="even")
        cursor.execute(f"Insert into data values('{e.get()}','even')")
        cursor.commit()
    else:
        l3.config(text="odd")
        cursor.execute(f"Insert into data values('{e.get()}','odd')")
        cursor.commit()


l2=Label(m,text="Enter Number",font=("Arial black",12),bg='red',fg="black").grid(row=0,column=0)
e=Entry(m,font=("Arial black",12))
e.grid(row=0,column=1)
b=Button(m,text="Even_or_odd",font=("Arial black",12),command=even_odd)
b.grid(row=3,column=1)
l3=Label(m,font=("Arial black",12),bg="yellow",fg="black")
l3.grid(row=2,column=0)
m.mainloop()




