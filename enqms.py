#Importing packages, modules
from tkinter import Tk , ttk
import tkinter as tk
from tkinter import *
from requests import *
from tkinter.scrolledtext import *
from tkinter import scrolledtext
from tkinter.messagebox import askokcancel
from sqlite3 import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import PhotoImage
import re

pattern = r'^[!@#$%^&*()+-_+{}\[\]:;<>,.?/\\|]+$'
regex = r'^[a-zA-Z]+$'
pattern1 =   r'^[+-]?\d*\.?\d+$'
					         	
def back2root():
	root.deiconify()
	aw.withdraw()
				
def admin():
	aw.deiconify()
	root.withdraw()
	
def deletepage():
   dw.deiconify()
   mw.withdraw()

def back2main():
   mw.deiconify()
   vw.withdraw()

def back3main():
   mw.deiconify()
   dw.withdraw()

def back():
   aw.deiconify()
   mw.withdraw()

root = Tk()
root.geometry("650x650+400+100")
root.title("Enquiry Management System By Avanti")
root.configure(bg = "lightblue")
f = ("Arial",20, "bold")
root.resizable(height = FALSE, width =FALSE)

#Top frame
top = Frame(root, width=650, height=85, bg= "#4169E1")
top.grid(row=0, column=0)

icon = Image.open('C:/internship/mira/Python/task3/p3_enquiryapp/images/download.png')
icon = icon.resize((80, 80))
icon= ImageTk.PhotoImage(icon)

app_name = Label(top, image= icon, compound=LEFT, text=" Enquiry Management System",  height = 4, padx =20,pady =35, anchor = CENTER, font = f , bg = "#4169E1", fg = "black" )
app_name.place(x=50, y=8)

#Main frame
root1 = Frame(root, width=650, height=565, bg= "lightblue")
root1.grid(row=1, column=0)
f1 =("Helvetica", 18, "bold")
f2 = ("Roboto Slab", 17, "bold")

lab_enq = Label(root1, text=" Enquiry Form",font = f1, bg = "black", fg  = "white")
lab_enq.place(x=250, y =10)

#Admin Button
btn_admin = Button(root1, text="Admin", font = f2, fg= "white", bg = "purple",relief = "solid" , height =1, command = admin)
btn_admin.place(x=500, y =30)

#Name input
lab_name = Label(root1, text="Enter Name = ", font = f1, bg = "lightblue")
lab_name.place(x=10, y =100)
ent_name = Entry(root1, font = f1, relief = "solid", width = 20)
ent_name.place(x=250, y =100)

#Phone Number Input
lab_phonenum = Label(root1, text="Enter Phone No. = ", font = f1, bg = "lightblue")
lab_phonenum.place(x=10, y =160)
ent_phonenum = Entry(root1, font = f1, relief = "solid", width = 20)
ent_phonenum.place(x=250, y =160)

#Address Input
lab_address = Label(root1, text="Enter Address = ", font = f1, bg = "lightblue")
lab_address.place(x=10, y =220)
st_address =scrolledtext.ScrolledText(root1, font = f1, relief = "solid", width = 21, height = 2)
st_address.place(x=250, y =220)

#Select Products
lab_select = Label(root1, text = "Select Products : ", font = f1, bg = "lightblue")
lab_select.place(x=10, y =310)

#varibale for value of checkbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Create checkboxes for products 1 to 5
checkbox1 = tk.Checkbutton(root1, text="Product 1",variable=var1 , onvalue = 1, offvalue=0,  font = f2, bg = "lightblue")
checkbox2 = tk.Checkbutton(root1, text="Product 2",variable=var2 , onvalue = 1, offvalue=0,  font = f2, bg = "lightblue")
checkbox3 = tk.Checkbutton(root1, text="Product 3",variable=var3 , onvalue = 1, offvalue=0,  font = f2, bg = "lightblue")
checkbox4 = tk.Checkbutton(root1, text="Product 4",variable=var4 , onvalue = 1, offvalue=0,  font = f2, bg = "lightblue")
checkbox5 = tk.Checkbutton(root1, text="Product 5",variable=var5 , onvalue = 1, offvalue=0,  font = f2, bg = "lightblue")

# Place checkboxes on the window
checkbox1.place(x=50, y =350)
checkbox2.place(x=230, y =350)
checkbox3.place(x=420, y =350)
checkbox4.place(x=160, y =400)
checkbox5.place(x=350, y =400)

#Save Enquiries
def save():
     con = None
     try:
      name = ent_name.get()
      phone = ent_phonenum.get()
      address = st_address.get("1.0", tk.END)

      if ((name == "") and (phone == "") and (st_address.get("1.0", tk.END).strip() == "")):
         messagebox.showerror("Error", "Please enter all fields") 
         return
      if(name == ""):
         messagebox.showerror("Error" , "Name is empty")
         return
      if(name.isspace()):
         messagebox.showerror("Error" , "Name should not contain spaces")
         ent_name.delete(0, tk.END)
         ent_name.focus_set()
         return
      if (len(name) < 2):
         messagebox.showerror("Error" , "Name should contain atleast 2 letters")
         ent_name.delete(0, tk.END)
         ent_name.focus_set()
         return
      if name.isdigit():
         messagebox.showerror("Error" , "Name should not contain numbers")
         ent_name.delete(0, tk.END)
         ent_name.focus_set()
         return
      if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", name):
         messagebox.showerror("Error" , "Name should not contain special characters")
         ent_name.delete(0, tk.END)
         ent_name.focus_set()
         return
      if (phone == ""):
         messagebox.showerror("Error" , "Phone number is empty")
         return 
      if (phone.isspace()):
         messagebox.showerror("Error" , "Phone number should not contain blank spaces")
         ent_phonenum.delete(0, tk.END)
         ent_phonenum.focus_set()
         return
      if re.search (regex, phone):
         messagebox.showerror("Error" , "Phone number should not contain alphabets")
         ent_phonenum.delete(0, tk.END)
         ent_phonenum.focus_set()
         return
      if re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", phone):
         messagebox.showerror("Error" , "Phone number should not contain special characters")
         ent_phonenum.delete(0, tk.END)
         ent_phonenum.focus_set()
         return
      if (len(phone) < 10 or len(phone) > 10):
         messagebox.showerror("Error" , "Phone number must contain 10 digits")
         ent_phonenum.delete(0, tk.END)
         ent_phonenum.focus_set()
         return
      if (address == "\n"):
         messagebox.showerror("Error", "Address is empty")
         st_address.delete(1.0, tk.END)
         st_address.focus_set()
         return
      if (address.isspace()):
         messagebox.showerror("Error" , "Address should not contain only blank spaces")
         st_address.delete(1.0, tk.END)
         st_address.focus_set()
         return
      if (len(address) < 10):
         messagebox.showerror("Error" , "Address cannot be too short")
         st_address.delete(1.0, tk.END)
         st_address.focus_set()
         return
      if not re.match (r'^[a-zA-Z0-9\s.,()/\'-]*$', address):
         messagebox.showerror("Error" , "Address should not contain this special characters")
         st_address.delete(1.0, tk.END)
         st_address.focus()
         return
      
      if var1.get() == 1:
         product = "product 1"
      if var2.get() == 1:
         product = "product 2"
      if var3.get() == 1:
         product = "product 3"
      if var4.get() == 1:
         product = "product 4"
      if var5.get() == 1:
         product = "product 5"
     
      if (var1.get() == 1) and (var2.get() == 1):
           product = "product 1" + " ," + "product 2"
      if (var1.get() == 1) and (var3.get() == 1):
           product = "product 1" + " ," + "product 3"
      if (var1.get() == 1) and (var4.get() == 1):
           product = "product 1" + " ," + "product 4"
      if (var1.get() == 1) and (var5.get() == 1):
           product = "product 1" + " ," + "product 5"
      if (var2.get() == 1) and (var3.get() == 1):
           product = "product 2" + " ," + "product 3"
      if (var2.get() == 1) and (var4.get() == 1):
           product = "product 2" + " ," + "product 4"
      if (var2.get() == 1) and (var5.get() == 1):
           product = "product 2" + " " + "product 5"
      if (var3.get() == 1) and (var4.get() == 1) :
           product = "product 3" + "," + "product 4"
      if (var3.get() == 1) and (var5.get() == 1):
           product = "product 3" + "," + "product 5"
      if (var4.get() == 1) and (var5.get() == 1):
           product = "product 4" + " ," + "product 5"

      if (var1.get() == 1) and (var2.get() == 1) and (var3.get() == 1):
           product = "product 1" + " ," + "product 2" + " ," + "product 3"
      if (var1.get() == 1) and (var2.get() == 1) and (var4.get() == 1):
           product = "product 1" + " ," + "product 2" + " ," + "product 4"
      if (var1.get() == 1) and (var2.get() == 1) and (var5.get() == 1):
           product = "product 1" + " ," + "product 2" + " ," + "product 2"
      if (var1.get() == 1) and (var3.get() == 1) and (var4.get() == 1):
           product = "product 1" + " ," + "product 3" + " ," + "product 4"
      if (var1.get() == 1) and (var3.get() == 1) and (var5.get() == 1):
           product = "product 1" + " ," + "product 3" + " ," + "product 5"
      if (var1.get() == 1) and (var4.get() == 1) and (var5.get() == 1):
           product = "product 1" + " ," + "product 4" + " ," + "product 5"
      if (var2.get() == 1) and (var3.get() == 1) and (var4.get() == 1):
           product = "product 2" + " ," + "product 3" + " ," + "product 4"
      if (var2.get() == 1) and (var3.get() == 1) and (var5.get() == 1):
           product = "product 2" + " ," + "product 3" + " ," + "product 5"
      if (var3.get() == 1) and (var4.get() == 1) and (var5.get() == 1):
           product = "product 3" + " ," + "product 4" + " ," + "product 5"

      if (var1.get() == 1) and (var2.get() == 1)  and (var3.get()== 1)  and (var4.get() == 1)  and (var5.get() == 1):
           product = "product 1" + "," + "product 2" + "," + "product 3" + "," + "product 4" + " ," +"product 5"
      elif (var1.get() == 0 and var2.get() == 0 and var3.get() == 0 and var4.get() == 0 and var5.get() == 0):
           messagebox.showerror("Error", "Select atleast one product")
    
      else:
           con = connect("enq.db")
           cursor = con.cursor()
           cursor.execute('select * from enquiries where phone = ?', (phone, ))
           existing_user = cursor.fetchone()

           if existing_user:
            messagebox.showerror("Error", "Phone number already exists. Please enter a different phone number.")
            ent_phonenum.delete(0, tk.END)
            ent_phonenum.focus_set()
           else:
            sql = "insert into enquiries values('%s', '%s', '%s', '%s')"
            cursor.execute(sql % (name, phone, address, product) )
            con.commit()
            messagebox.showinfo("Success", "Enquiry recorded")
            ent_name.delete(0, tk.END)
            ent_phonenum.delete(0, tk.END)
            st_address.delete(1.0, tk.END)
            checkbox1.deselect()
            checkbox2.deselect()
            checkbox3.deselect()
            checkbox4.deselect()
            checkbox5.deselect()
            ent_name.focus_set()
          
     except Exception as e:
          messagebox.showerror("Issue", e)
          con.rollback()
         
     finally:
         if con is not None:
             con.close()

btn_save = Button(root1, text="Submit", font = f1, bg = "lightgreen",width = 10, relief = "solid", command=save)
btn_save.place(x=200, y =460)

#Clear Button
def clear():
    ent_name.delete(0, tk.END)
    ent_phonenum.delete(0, tk.END)
    st_address.delete(1.0, END)
    checkbox1.deselect()
    checkbox2.deselect()
    checkbox3.deselect()
    checkbox4.deselect()
    checkbox5.deselect()
    ent_name.focus()
   
btn_clear = Button(root1, text = "Clear", font = f1, bg = "pink", relief = "solid", width = 5, command = clear)
btn_clear.place(x=400, y =460)

#Login Function
def login():
      passwd = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]+$'
      username = aw_ent_uname.get()
      password = aw_ent_password.get()
      if (username == "") and (password == ""):
           messagebox.showerror("Login Failed", "Please enter all the fields")
      elif (username == ""):
            aw_ent_uname.delete(0, tk.END)
            aw_ent_uname.focus()
            messagebox.showerror("Login Failed", "Username is empty")
      elif (username.isspace()):
            messagebox.showerror("Login Failed", "Username cannot be blank spaces")
            aw_ent_uname.delete(0, tk.END)
            aw_ent_uname.focus()
      elif (len(username) < 5):
            messagebox.showerror("Login Failed", "Length of username should be atleast 8 characters")
            aw_ent_uname.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif re.match(r"^\d+$", username):
            messagebox.showerror("Login Failed", "Username should not contain only digits")
            aw_ent_uname.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif re.search(r'~`@_!#$%^&*()<>?/|}{~:;.]"', username):
            messagebox.showerror("Login Failed", "Username should not contain only special characters")
            aw_ent_uname.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif (password == ""):
            messagebox.showerror("Login Failed", "Password is empty")
      elif (password.strip() == ""):
            messagebox.showerror("Login Failed", "Password cannot be blank spaces")
            aw_ent_password.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif (len(password)< 8):
            messagebox.showerror("Login Failed", "Length of password should be atleast 8 characters")
            aw_ent_password.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif not re.search(passwd, password):
            messagebox.showerror("Login Failed", "Password must contain atleast one alphabet, digit and special character")
            aw_ent_password.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      elif (username == "admin") and (password == "avanti@123"):
            messagebox.showinfo("Success!!", "Login Successful")
            mw.deiconify()
            aw.withdraw()
            aw_ent_uname.delete(0, tk.END)
            aw_ent_password.delete(0, tk.END)
            aw_ent_uname.focus()
            return
      else:
           messagebox.showerror("Login Failed", "Login credentials does not match")
           aw_ent_uname.delete(0, tk.END)
           aw_ent_password.delete(0, tk.END)
           aw_ent_uname.focus()
           return
      
#Admin Login Panel
aw = Tk()
aw.title("Admin Panel")
aw.geometry("500x500+500+100")
aw.configure(bg="lightpink")
aw_lab_adm = Label(aw, text = "Admin Login", font = f,bg = "black", fg = "white")
aw_lab_uname = Label(aw, text = "Enter username", font = f, bg = "lightpink")
aw_ent_uname = Entry(aw, font = f1,  width = 22, relief="solid")
aw_lab_password = Label(aw, text = "Enter password", font = f,  bg = "lightpink")
aw_ent_password = Entry(aw, font = f1, show="*",  width = 22, relief="solid")
aw_btn_login = Button(aw, text = "Login", font = f1, width = 8,bg= "violet", relief = "solid", command=login)
aw_btn_back = Button(aw, text = "Back", font = f1, command = back2root, bg = "lightblue",relief = "solid" ,fg = "black")

aw_lab_adm.place(x = 170, y = 30)
aw_lab_uname.place(x = 100, y = 100)
aw_ent_uname.place(x = 100, y = 150)
aw_lab_password.place(x = 100, y = 220)
aw_ent_password.place(x = 100, y = 280)
aw_btn_login.place(x = 120, y = 350)
aw_btn_back.place(x = 300, y = 350)
aw.withdraw()

#View Function
def view():
	vw.deiconify()
	mw.withdraw()
	vw_enq_data.delete(1.0, END)
		
	con = None
	try:
				con = connect("enq.db")
				cursor = con.cursor()
				sql = "select * from enquiries"
				cursor.execute(sql)
				data = cursor.fetchall()
				info = ""
				for d in data:
						info += "Name = " + str(d[0])  + "\n"
						info += "Phone = " + str(d[1])  + "\n"
						info += "Address = " + str(d[2]) + "\n"
						info += "Product = " + str(d[3]) + "\n"
						info +=  "- - - - - - - - - - - - - - - - - - - - - - -" + "\n"
				vw_enq_data.insert(INSERT, info)
	except Exception as e:
			con.rollback()
			messagebox.showerror("Issue", e)
	finally:
			if con is not None:
				con.close()
                    
#View Delete Window
mw = Tk()
mw.title("View and Delete Window")
mw.geometry("600x600+400+100")
mw.configure(bg="#967bb6")
mw_lab = Label(mw, text = "Admin Panel", bg = "black", fg = "white", font = f, relief = "solid" )
mw_btn_view = Button(mw, text = "View Enquiry", font = f, relief = "solid", command = view, bg = "lightyellow")
mw_btn_delete = Button(mw, text = "Delete Enquiry", font = f,relief = "solid" ,command = deletepage, bg = "lightyellow")
mw_btn_back = Button(mw, text = "Back", font = f,relief = "solid" ,command = back, bg = "lightpink")
mw_lab.place(x = 220, y =20)
mw_btn_view.place( x =200, y = 100)
mw_btn_delete.place( x =200, y = 220)
mw_btn_back.place( x =250, y = 350)
mw.withdraw()

#View Enquiry Window
vw =Tk()
vw.title("View Enquiry Window")
vw.geometry("600x600+400+100")
vw.configure(bg="orange")
vw_enq_data =  ScrolledText(vw,relief = "solid", width=35, height=15, font =f, padx = 10 )
vw_enq_data.place(x=10, y =10)
vw_enq_back =  Button(vw, text = "Back",  font =f , command = back2main, bg = "#967bb6")
vw_enq_back.place(x = 250, y =500)
vw.withdraw()

def delete():
   con = None
   try:
      con =connect("enq.db")
      cursor = con.cursor()
      phone = dw_ent_phonenum.get()
      if (phone == ""):
         messagebox.showerror("Error" , "Phone number  is empty")
      elif (phone.isspace()):
         messagebox.showerror("Error" , "Phone number should not contain blank spaces")
         dw_ent_phonenum.delete(0, tk.END)
         dw_ent_phonenum.focus_set()
      elif (len(phone) < 10):
         messagebox.showerror("Error" , "Phone number must contain 10 digits")
         dw_ent_phonenum.delete(0, tk.END)
         dw_ent_phonenum.focus_set()
      elif re.search (regex, phone):
         messagebox.showerror("Error" , "Phone number should not contain alphabets")
         dw_ent_phonenum.delete(0, tk.END)
         dw_ent_phonenum.focus_set()
      elif re.search ("[~`@_!#$%^&*()<>?/|}{~:;.]", phone):
         messagebox.showerror("Error" , "Phone number should not contain special characters")
         dw_ent_phonenum.delete(0, tk.END)
         dw_ent_phonenum.focus_set()
         return
      
      else:
         sql = "delete from enquiries where phone = '%s' "
         cursor.execute(sql % (phone))
         if cursor.rowcount == 1:
            con.commit()
            messagebox.showinfo("Success", "Enquiry deleted successfully!!!")
            dw_ent_phonenum.delete(0, tk.END)
            dw_ent_phonenum.focus_set()
         else:
            messagebox.showerror("Error", "Enquiry for this phone number does not exists")
            dw_ent_phonenum.delete(0, tk.END)
            dw_ent_phonenum.focus()
            return

   except Exception as e:
      con.rollback()
      messagebox.showerror("Issue ", e)
   finally:
        if con is not None:
             con.close()
                        
#Delete Enquiry Window
dw = Tk()
dw.title("Delete Enquiry Window")
dw.geometry("600x600+400+100")
dw.configure(bg="#D70040")
dw_delete = Label(dw, text="Delete Enquiry", font = f1, bg = "black", fg = "white")
dw_delete.place(x=200, y =40)
dw_phonenum = Label(dw, text="Enter Phone No", font = f1, bg = "#D70040")
dw_phonenum.place(x=200, y =100)
dw_ent_phonenum = Entry(dw, font = f1, relief = "solid", width = 20)
dw_ent_phonenum.place(x=170, y =150)
dw_enq_delete =  Button(dw, text = "Delete",  font =f , command = delete, bg = "orange", relief = "solid", width = 12)
dw_enq_delete.place(x=200, y =220)
dw_enq_back =  Button(dw, text = "Back",  font =f , command = back3main, bg = "#967bb6", relief = "solid", width = 6)
dw_enq_back.place(x=250, y =350)
dw.withdraw()

#Closing Window
def on_closing():
   if askokcancel("Close",  "Do you want to exit?"):
      root.destroy()
      aw.destroy()
      mw.destroy()
      vw.destroy()
      dw.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
aw.protocol("WM_DELETE_WINDOW", on_closing)
mw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()