from tkinter import *
from tkinter import ttk # import to use combobox
m=Tk()
m.title("BBQ")
icon_image=PhotoImage(file="res.png")
m.iconphoto(False,icon_image)
m.geometry("1365x713+0+0")
m.config(bg="grey")
f=Frame(m,bg="black",borderwidth=30)
f.place(x=930)
amount_and_quantities_in_data={'BURGER':200,'FRIES':50,'SANDWICH':150,'PIZZA':500,"BROAST":150,"BIRYANI":250,"TIKKA":400,"ROOL":150,"FISH":1000,"SOOP":200}
d={}
k=0
# for adding items name and amount in one side::
for x,y in amount_and_quantities_in_data.items():
    l = Label(f, text=x, bg="orange", font=("Arial", 15), fg="black", width=10).grid(row=k,column=6,  pady=10,padx=10)
    l = Label(f, text=y, bg="darkblue", font=("Arial", 15), fg="white", width=20).grid(row=k,column=7,  pady=10,padx=10)
    k+=1
# combobox is similar to entry box but show drop down menu:
choices=["BURGER","FRIES","SANDWICH","PIZZA","BROAST","TIKKA","BIRYANI","ROLL","FISH","SOOP"]
def Number_of_snacks():
    for i in range(1,int(e.get())+1):
        if int(e.get())<=10:
            if i<=5:
                Label(text=f"ENTER SNACK {i}",bg="orange",fg="black",width=15,font=("Arial",15)).grid(row=2*i-1,column=0,padx=0,pady=10)
                e1=ttk.Combobox(m,value=choices,width=18,font=("Arial",15))
                e1.set("Select snack")
                e1.grid(row=2*i-1,column=1,padx=15)
                Label(text="ENTER QUANTITY", bg="orange", fg="black", width=15, font=("Arial", 15)).grid(row=2*i,column=0, padx=0,pady=10)
                e2=Entry(m, fg="black", bg="white", width=20, font=("Arial", 15))
                e2.grid(row=2*i, column=1, padx=15)
                d[f"snack_{i}"]=(e1,e2)
            else:
                Label(text=f"ENTER SNACK {i}", bg="orange", fg="black", width=15, font=("Arial", 15)).grid(row=2 * (i-6),column=2, padx=0, pady=10)
                e1 = ttk.Combobox(m, value=choices, width=18, font=("Arial", 15))
                e1.set("Select snack")
                e1.grid(row=2 * (i-6), column=3, padx=15)
                Label(text="ENTER QUANTITY", bg="orange", fg="black", width=15, font=("Arial", 15)).grid(row=2 * (i-5)-1,column=2, padx=0,pady=10)
                e2 = Entry(m, fg="black", bg="white", width=20, font=("Arial", 15))
                e2.grid(row=2 * (i-5)-1, column=3, padx=15)
                d[f"snack_{i}"] = (e1, e2)
        
def amount():
    money=0
    for i in d:
        snack_name = (d[i][0].get()).upper()
        quantity = int(d[i][1].get())
        if snack_name in amount_and_quantities_in_data:
            money=money+amount_and_quantities_in_data[snack_name]*quantity
        else:
            money=money
    Label(m,text=f"Total amount is {money}", bg="darkblue", fg="white", width=25, font=("Arial", 15)).grid(row=18,column=1)


l=Label(m,text="ENTER NO OF SNACKS",bg="#00008B",font=("Arial",15),fg="white",width=20).grid(row=0,column=0,pady=10,padx=10)
e=Entry(m,fg="black",bg="white",width=20,font=("Arial",15))
e.grid(row=0,column=1,padx=15)
button1=Button(text="OK",bg="orange",fg="Black",width=15,font=("Arial",15),command=Number_of_snacks)
button1.grid(row=9,column=0,pady=3)
button2=Button(text="Bill",bg="orange",fg="Black",width=15,font=("Arial",15),command=amount)
button2.grid(row=15,column=1,pady=3)

m.mainloop()





