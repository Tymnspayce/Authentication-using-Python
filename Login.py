import pymysql
from tkinter import messagebox
from tkinter import *
from Signup import signLogic


#-------------------------This is the Starting of the section is for the Database Coding--------------------------#
def CreateConn():
    return pymysql.connect(host="localhost",database="pyworks",user="root",password="Aditya@1003",port=3306)


def Login_Logic(eem,eps):
    username=eem.get()
    password=eps.get()
    if(username=="" or password==""):
        messagebox.showinfo("Error","All Fields are Mandatory")
    else:  
        conn=CreateConn()
        cursor=conn.cursor()
        args=(username,password)
        query="Select email,password from ai_users where email=(%s) and password=(%s)"
        cursor.execute(query,args)
        dataname = cursor.fetchone()
        if(dataname==None):
            messagebox.showinfo("Error!!","Invalid Login")
            eem.delete(0,END)
            eps.delete(0,END)
        else:
            messagebox.showinfo("Success!!","Successfully Logged in")
            t.destroy()
            from default import fetchlogic
            fetchlogic()
            

            


#-------------------------This is the Ending of the section is for the Database Coding--------------------------#


def loginLogic():
    def twofuncn():
        t.destroy()
        signLogic()

    global t
    t=Tk()

    # To change icon of window
    photo = PhotoImage(file = "login.png")
    t.iconphoto(False,photo)

    # To set Window size
    t.geometry("400x470")

    # Name of the Window
    t.title(" Login page")

    # Background Color for window
    t.configure(bg="#333333")

    # login page Label
    lp = Label(t,text="Login Page",font=('Arial',30),background="#333333",fg="#fff")
    lp.place(x="100",y="15")

    # Labels like name,email,password,mobile number,city

    em = Label(t,text="E-mail",background="#333333",fg="#ff004f",font=('Times',14))
    em.place(x="40",y="156")

    ps = Label(t,text="Password",background="#333333",fg="#ff004f",font=('Times',14))
    ps.place(x="40",y="216")

    # Textfields for the labels

    eem=Entry(width="30")
    eem.place(x="170",y="160")

    eps=Entry(width="30")
    eps.place(x="170",y="220")

    # Function to clear all data in the textfields
    def Clear():
        eem.delete(0,END)
        eps.delete(0,END)

    # Adding Buttons to window
    submit=Button(t,text="Submit",background="#ff004f",width="5",fg="white",height="1",command=lambda: Login_Logic(eem,eps))
    submit.place(x="70",y="410")

    reset=Button(t,text="Reset ",background="#ff004f",width="5",fg="white",height="1",command=Clear)
    reset.place(x="180",y="410")

    Signup=Button(t,text="Signup",background="#ff004f",fg="white",width="5",height="1",command=twofuncn)
    Signup.place(x="280",y="410")


    # Mainloop so that windows can run continuously
    mainloop()

loginLogic()