from tkinter import *
import pymysql
from tkinter import messagebox

def CreateConn():
    return pymysql.connect(host="localhost",database="pyworks",user="root",password="Aditya@1003",port=3306)


def fetchlogic():
    conn=CreateConn()
    cursor=conn.cursor()
    query="select * from ai_users"
    cursor.execute(query)
    data=cursor.fetchall()
    name,email,password,mobile_number,city=data[0]
    conn.close()

    t=Tk()

    # To change icon of window
    # photo = PhotoImage(file = "login.png")
    # t.iconphoto(False,photo)

    # To set Window size
    t.geometry("400x500")

    # Name of the Window
    t.title(" Your Data")

    # Background Color for window
    t.configure(bg="#333333")

    # login page Label
    lp = Label(t,text="Your Details",font=('Arial',30),background="#333333",fg="#fff")
    lp.place(x="80",y="15")

    # Labels like name,email,password,mobile number,city
    nm = Label(t,text=f"{name}",background="#333333",fg="#ff004f",font=('Times',14))
    nm.place(x="130",y="96")

    em = Label(t,text=f"{email}",background="#333333",fg="#ff004f",font=('Times',14))
    em.place(x="130",y="156")

    ps = Label(t,text=f"{password}",background="#333333",fg="#ff004f",font=('Times',14))
    ps.place(x="130",y="216")

    mn = Label(t,text=f"{mobile_number}",background="#333333",fg="#ff004f",font=('Times',14))
    mn.place(x="130",y="276")

    ct = Label(t,text=f"{city}",background="#333333",fg="#ff004f",font=('Times',14))
    ct.place(x="130",y="336")

    close=Button(t,text="close ",background="#ff004f",width="5",fg="white",height="1",command=t.destroy)
    close.place(x="160",y="450")

    mainloop()

fetchlogic()