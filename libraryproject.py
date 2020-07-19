##LIBRARY

from tkinter import *
from tkinter import messagebox
import sqlite3
from array import *

con=sqlite3.connect("library.db")
cr=con.cursor()
# cr.execute("create table library (Book_Name varchar(50) primary key, Book_Category varchar(50), Book_Price integer, Book_Quantity integer)")
# con.commit()
                  
homepage=Tk()
homepage.resizable(False, False)
homepage.title("www.8357l18r4ry.com")
back=Canvas(homepage)
back.pack(expand=True, fill=BOTH)
image=PhotoImage(file="bg.png")
back.img=image
back.create_image(0,0, anchor=NW, image=image)
homepage.geometry('900x600')
def adminpage():
      admin=Tk()
      admin.resizable(False, False)
      admin.configure(background="Light pink")
      admin.title("Administrator")
      admin.geometry('900x600')
      
      def showbook():
            showbook=Tk()
            showbook.resizable(False, False)
            showbook.configure(background="Light pink")
            showbook.geometry('900x600')
            showbook.title("Menu")
            cr.execute("select Book_Name from library order by Book_Name")
            name=cr.fetchall()
            cr.execute("select Book_Category from library order by Book_Name")
            category=cr.fetchall()
            cr.execute("select Book_Price from library order by Book_Name")
            price=cr.fetchall()
            cr.execute("select Book_Quantity from library order by Book_Name")
            quantity=cr.fetchall()

            l=Label(showbook, text="Name", font="Calibri 17", fg="Orange", bg="Light pink", padx=20, pady=20)
            l.grid(row=0, column=0)
            l=Label(showbook, text="Category", font="Calibri 17", fg="Orange", bg="Light pink", padx=20, pady=20)
            l.grid(row=0, column=1)
            l=Label(showbook, text="Price", font="Calibri 17", fg="Orange", bg="Light pink", padx=20, pady=20)
            l.grid(row=0, column=2)
            l=Label(showbook, text="Quantity", font="Calibri 17", fg="Orange", bg="Light pink", padx=20, pady=20)
            l.grid(row=0, column=3)
            
            count=1
            for n in name:
                  l=Label(showbook, text=n, font="Calibri 15", fg="Dark green", bg="Light pink", padx=20, pady=20)
                  l.grid(row=count, column=0)
                  count+=1

            count=1
            for c in category:
                  l=Label(showbook, text=c, font="Calibri 15", fg="Dark green", bg="Light pink", padx=20, pady=20)
                  l.grid(row=count, column=1)
                  count+=1

            count=1
            for p in price:
                  l=Label(showbook, text=p, font="Calibri 15", fg="Dark green", bg="Light pink", padx=20, pady=20)
                  l.grid(row=count, column=2)
                  count+=1

            count=1
            for q in quantity:
                  l=Label(showbook, text=q, font="Calibri 15", fg="Dark green", bg="Light pink", padx=20, pady=20)
                  l.grid(row=count, column=3)
                  count+=1

            def goback():
                  showbook.destroy()
                  
            submit=Button(showbook, text="Ok", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=25, pady=5, command=goback)
            submit.grid(row=count+1, column=2, pady=5)
            showbook.mainloop()
            
      def addbook():
            addbook=Tk()
            addbook.resizable(False, False)
            addbook.configure(background="Light pink")
            addbook.geometry('900x600')
            addbook.title("Add")
            l1=Label(addbook, text="Name : ",  font="Calibri 15 bold", fg="Dark Green", bg="Light pink").grid(row=0, padx=200, pady=20)
            e1=Entry(addbook, bd =5, font="Calibri 15", fg="Orange")
            e1.grid(row=0, column=1)

            l2=Label(addbook, text="Category : ",  font="Calibri 15 bold", fg="Dark Green", bg="Light pink").grid(row=1, padx=200, pady=15)
            e2=Entry(addbook, bd =5, font="Calibri 15", fg="Orange")
            e2.grid(row=1, column=1)

            l3=Label(addbook, text="Price : ",  font="Calibri 15 bold", fg="Dark Green", bg="Light pink").grid(row=2, padx=200, pady=15)
            e3=Entry(addbook, bd =5, font="Calibri 15", fg="Orange")
            e3.grid(row=2, column=1)
            
            l4=Label(addbook, text="Quantity : ", font="Calibri 15 bold", fg="Dark Green", bg="Light pink").grid(row=3, padx=200, pady=15)
            e4=Entry(addbook, bd =5, font="Calibri 15", fg="Orange")
            e4.grid(row=3, column=1)

            def submit():
                  name=e1.get()
                  category=e2.get()
                  price=e3.get()
                  quantity=e4.get()
                  cr.execute("insert into library values (?, ?, ?, ?)", (name, category, price, quantity))
                  con.commit()
                  messagebox.showinfo("Successfull", "Book has been added to the library.", command=addbook.destroy())
              
            submit=Button(addbook, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=5, pady=5, command=submit)
            submit.grid(row=4, column=1, pady=50)
            addbook.mainloop()

      def removebook():
            removebook=Tk()
            removebook.resizable(False, False)
            removebook.geometry('900x600')
            removebook.configure(background="Light pink")
            removebook.title("Remove")
            l1=Label(removebook, text="Name : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=0, padx=175, pady=100)
            e1=Entry(removebook, bd =5, font="Calibri 15", fg="Orange")
            e1.grid(row=0, column=1)

            def submit():
                  name=e1.get()
                  cr.execute("delete from library where Book_Name=?", (name,))
                  con.commit()
                  messagebox.showinfo("Successfull", "Book has been deleted from the library.", command=removebook.destroy())
                  
            submit=Button(removebook, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=7, pady=7, command=submit)
            submit.grid(row=3, column=1, pady=100)
            removebook.mainloop()

      def changeprice():
            changeprice=Tk()
            changeprice.resizable(False, False)
            changeprice.geometry('900x600')
            changeprice.configure(background="Light Pink")
            changeprice.title("Price")
            l1=Label(changeprice, text="Name : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=0, padx=175, pady=100)
            e1=Entry(changeprice, bd =5, font="Calibri 15", fg="Orange")
            e1.grid(row=0, column=1)

            l2=Label(changeprice, text="Price : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=1, column=0)
            e2=Entry(changeprice, bd =5, font="Calibri 15", fg="Orange")
            e2.grid(row=1, column=1)

            def submit():
                  name=e1.get()
                  price=e2.get()
                  cr.execute("update library set Book_Price=? where Book_Name=?", (price, name,))
                  con.commit()
                  messagebox.showinfo("Successfull", "Book price has been changed.", command=changeprice.destroy())
                  
            submit=Button(changeprice, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=7, pady=7, command=submit)
            submit.grid(row=3, column=1, pady=50)
            changeprice.mainloop()

      
      def changequantity():
            changequantity=Tk()
            changequantity.resizable(False, False)
            changequantity.geometry('900x600')
            changequantity.configure(background="Light pink")
            changequantity.title("Quantity")
            l1=Label(changequantity, text="Name : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=0, padx=175, pady=100)
            e1=Entry(changequantity, bd =5, font="Calibri 15", fg="Orange")
            e1.grid(row=0, column=1)

            l2=Label(changequantity, text="Quantity : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=1, column=0)
            e2=Entry(changequantity, bd =5, font="Calibri 15", fg="Orange")
            e2.grid(row=1, column=1)

            def submit():
                  name=e1.get()
                  quantity=e2.get()
                  cr.execute("update library set Book_Quantity=? where Book_Name=?", (quantity, name,))
                  con.commit()
                  messagebox.showinfo("Successfull", "Book quantity has been changed.", command=changequantity.destroy())
                  
            submit=Button(changequantity, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=7, pady=7, command=submit)
            submit.grid(row=2, column=1, pady=50)
            changequantity.mainloop()

      op=0
      def assign0():
            global op
            op=0
      def assign1():
            global op
            op=1
      def assign2():
            global op
            op=2
      def assign3():
            global op
            op=3
      def assign4():
            global op
            op=4

      Label(admin, text="Choose:", font="Calibri 15 bold", fg="Dark green", bg="Light Pink").grid(padx=300, pady=10)
      Radiobutton(admin, text="Show book", command=assign0, value=0, font="Calibri 12", fg="Dark green", bg="Light pink").grid(pady=20)
      Radiobutton(admin, text="Add book", command=assign1, value=1, font="Calibri 12", fg="Dark green", bg="Light pink").grid(pady=20)
      Radiobutton(admin, text="Remove book", command=assign2, value=2, font="Calibri 12", fg="Dark green", bg="Light pink").grid(pady=20)
      Radiobutton(admin, text="Change price", command=assign3, value=3, font="Calibri 12", fg="Dark green", bg="Light pink").grid(pady=20)
      Radiobutton(admin, text="Change quantity", command=assign4, value=4, font="Calibri 12", fg="Dark green", bg="Light pink").grid(pady=30)

      def callfunc():
            global op
            if(op==0):
                  showbook()
            elif(op==1):
                  addbook()
            elif(op==2):
                  removebook()
            elif(op==3):
                  changeprice()
            elif(op==4):
                  changequantity()

      def gohome():
            global homepage
            homepage.iconify()
            homepage.deiconify()
            admin.destroy()
      submit=Button(admin, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=10, pady=10, command=callfunc)
      submit.grid(padx=20, pady=20)
      homepage=Button(admin, text="Home", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=10, pady=10, command=gohome).grid(padx=20, pady=0)
      admin.mainloop()

def adminrequest():
      adminrequest=Toplevel()
      adminrequest.resizable(False, False)
      adminrequest.title("Admin request")
      adminrequest.geometry('900x600')
      adminrequest.configure(background="Light pink")
      l1=Label(adminrequest, text="Login ID: ", font="Calibri 15 bold", fg="Dark green", bg="Light pink", padx=5, pady=5).grid(row=0, padx=150, pady=60)
      e1=Entry(adminrequest, bd=5, font="Calibri 20", fg="Orange")
      e1.grid(row=0, column=1)

      l2=Label(adminrequest, text="Password: ", font="Calibri 15 bold", fg="Dark green", bg="Light pink", padx=5, pady=5).grid(row=1, pady=60)
      e2=Entry(adminrequest, bd=5, font="Calibri 20", fg="Orange", show="*")
      e2.grid(row=1, column=1)

      def gohome():
            global homepage
            homepage.iconify()
            homepage.deiconify()
            adminrequest.destroy()
            
      def submit():
            login=e1.get()
            password=e2.get()
            if(login=="sanchit" and password=="sanchit123"):
                  adminrequest.destroy()
                  adminpage()
            else:
                  messagebox.showerror("Error in login", "The entered ID/Password combination is incorrect. \nPlease try again.")
              
      submit=Button(adminrequest, text="Submit", font="Calibri 15 bold", bg="Light grey", fg="Orange", padx=7, pady=7, command=submit)
      submit.grid(row=4, column=1, pady=30)
      homepage=Button(adminrequest, text="Home", font="Calibri 15 bold", bg="Light grey", fg="Orange", padx=7, pady=7, command=gohome)
      homepage.grid(row=5, column=1, pady=30)
      adminrequest.mainloop()

def userpage():
      user=Tk()
      user.resizable(False, False)
      user.title("User")
      user.geometry('900x600')
      user.configure(background="Light Pink")

      def issuee():
            issue=Toplevel()
            issue.resizable(False, False)
            issue.title("Issue")
            issue.geometry('900x600')
            issue.configure(background="Light Pink")
            con.commit()
            h1=Label(issue, text="Book Name", font="Calibri 15 bold", fg="Orange", bg="Light pink", padx=5, pady=5).grid(row=0, padx=50)
            h2=Label(issue, text="Price", font="Calibri 15 bold", fg="Orange", bg="Light pink", padx=5, pady=5).grid(row=0, column=1, padx=50)
            cr.execute("select Book_Name from library where Book_Quantity<>0 order by Book_Name")
            name=cr.fetchall()
            cr.execute("select Book_Price from library where Book_Quantity<>0 order by Book_Name")
            price=cr.fetchall()

            arr=[]
            namearr=[]
            checkbuttons=[]
            count=0
            def checkchecks():
                  total=0
                  for i in range(0,count):
                        if(arr[i].get()==True):
                              book=namearr[i]
                              [b]=book
                              cr.execute("select Book_Price from library where Book_Name=?", (b,))
                              price=cr.fetchone()[0]
                              total+=price
                              cr.execute("select Book_Quantity from library where Book_Name=?", (b,))
                              quantity=cr.fetchone()[0]
                              q=int(quantity)
                              q=q-1
                              cr.execute("update library set Book_Quantity=? where Book_Name=?", (q, b,))
                              con.commit()
                  message="Rs. "+str(total)+"\nPay the due amount at the Library Office."
                  messagebox.showinfo('Successfully issued', message, command=issue.destroy())
                              
            for n in name:
                  arr.append(BooleanVar())
                  check=BooleanVar()
                  chk=Checkbutton(issue, text=n, var=arr[count], font="Calibri 15", fg="Dark green", bg="Light pink", padx=5, pady=5)
                  chk.grid(row=count+1, sticky=W)
                  namearr.append(n)
                  checkbuttons.append(chk)
                  count=count+1

            count=0
            for p in price:
                  l=Label(issue, text=p, font="Calibri 15", fg="Dark green", bg="Light pink", padx=5, pady=5)
                  l.grid(row=count+1, column=1)
                  count+=1

            submit=Button(issue, text="Submit", font="Calibri 15 bold", fg="Orange", bg="Light grey", padx=10, pady=10, command=checkchecks).grid(row=count+2, column=1)            
            issue.mainloop()

      def returnn():
            returnn=Toplevel()
            returnn.resizable(False, False)
            returnn.geometry('900x600')
            returnn.configure(background="Light pink")
            l1=Label(returnn, text="Name : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=0, padx=150, pady=40)
            e1=Entry(returnn, bd =5, font="Calibri 15", fg="Orange")
            e1.grid(row=0, column=1, pady=50)

            l2=Label(returnn, text="No. of days since issued : ", font="Calibri 15 bold", bg="Light pink", fg="Dark green").grid(row=1, padx=150, pady=40)
            e2=Entry(returnn, bd =5, font="Calibri 15", fg="Orange")
            e2.grid(row=1, column=1, pady=50)

            def returnbook():
                  flag=0
                  book=e1.get()
                  days=int(e2.get())
                  if(days>100):
                        days=100
                  cr.execute("select Book_Name from library where Book_Name=?", (book,))
                  check=cr.fetchall()
                  for c in check:
                        flag=1
                  if(flag==1):
                        cr.execute("select Book_Price from library where Book_Name=?", (book,))
                        price=cr.fetchone()[0]
                        returnprice=(price-(days*price)/100)
                        cr.execute("select Book_Quantity from library  where Book_Name=?", (book,))
                        q=cr.fetchone()[0]
                        q=q+1
                        cr.execute("update library set Book_Quantity=? where Book_Name=?", (q, book,))
                        con.commit()
                        string="Thank you for returning the book!\nCollect Rs. "+str(returnprice)+" from the Library Office."
                        messagebox.showinfo("Return successfull", string, command=returnn.destroy())
                  else:
                        messagebox.showinfo("Return unsuccessfull", "Book name entered is invalid. Please try again.")
                        
            submit=Button(returnn, text="Submit", font="Calibri 15 bold", fg="Orange", padx=10, pady=10, command=returnbook)
            submit.grid(row=2, column=1, pady=50)            
            returnn.mainloop()
      
      op=0
      def assign1():
            global op
            op=1
      def assign2():
            global op
            op=2
            
      Label(user, text="Choose:", font="Calibri 15 bold", fg="Dark green", bg="Light pink").grid(padx=350, pady=30)
      Radiobutton(user, text="Issue", font="Calibri 15", fg="Dark green", bg="Light pink", command=assign1, value=1).grid(padx=20, pady=30)
      Radiobutton(user, text="Return", font="Calibri 15", fg="Dark green", bg="Light pink", command=assign2, value=2).grid(padx=20, pady=30)

      def callfunc():
            global op
            if(op==1):
                  issuee()
            elif(op==2):
                  returnn()

      def gohome():
            global homepage
            homepage.iconify()
            homepage.deiconify()
            user.destroy()
      submit=Button(user, text="Submit", font="Calibri 15 bold", fg="Orange", padx=10, pady=10, command=callfunc).grid(padx=50, pady=30)
      homepage=Button(user, text="Home", font="Calibri 15 bold", fg="Orange", padx=10, pady=10, command=gohome).grid(padx=50, pady=30)
      user.mainloop()

def admin():
      homepage.withdraw()
      adminrequest()

def user():
      homepage.withdraw()
      userpage()
home=Label(back, text="8357 L18r4ry", font="Isocteur 30 bold underline", fg="Orange", bg="#222").grid(padx=300, pady=70)
adminbutton=Button(back, command=admin, text="Admin", font="Calibri 15 bold", fg="Dark green", padx=10, pady=10, bg="Light grey", border=4).grid(padx=300, pady=30)
userbutton=Button(back, command=user, text="User", font="Calibri 15 bold", fg="Dark green", padx=17, pady=10, bg="Light grey", border=4).grid(pady=40)
homepage.mainloop()
