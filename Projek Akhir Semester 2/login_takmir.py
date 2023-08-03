from tkinter import *
from tkinter import messagebox as mbox
from csv import *
import csv


root = Tk()
root.title("Login Takmir")
root.geometry("1280x720")
root.config(bg="#c5ac8e")
root.resizable(False, False)

img = PhotoImage(file="bg login dan register.png")
Label (root,image=img,bg ="#c5ac8e").place(x=0,y=0)


def login():
    file = open("datauser.csv", 'r')
    csvfile = csv.reader(file)
    username = user.get()
    password = pasw.get()
    check = 0

    for i in csvfile:
        if  ([f"{username}",f"{password}"]) == i:
            check += 1
            root.destroy()
            import homepage
    if  check == 0:
        mbox.showerror("Alert!", "Password atau Username Salah!")
        
#------------------------------------------------------------------------------------
log_frame = Frame(root, width=483, height=390, bg="#EAE0D5")
log_frame.place(x=720, y=180)

header = Label(text="Login", fg="#E27070", bg="#EAE0D5", font=("Rowdies", 64, "bold"))
header.place(x=850, y=80)

def on_name(e):
    user.delete(0, "end")

def out_name(e):
    fill = user.get()
    if fill == "":
        user.insert(0, "Username")

def on_pass(e):
    pasw.delete(0, "end")

def out_pass(e):
    fill = pasw.get()
    if fill == "":
        pasw.insert(0, "Password")
def register():
    root.destroy()
    import register_takmir
        
#===============================================================================================        
        
user = Entry(log_frame, width=25, fg="black", border=0, bg="#EAE0D5", font=("Roboto", 12))
user.place(x=60, y=100)
user.insert(0, "Username")
user.bind("<FocusIn>", on_name)
user.bind("<FocusOut>", out_name)
Frame(log_frame, width=345, height=3, bg="black").place(x=60, y=130)

pasw = Entry(log_frame, width=25, fg="black", border=0, bg="#EAE0D5", font=("Roboto", 12))
pasw.place(x=60, y=180)
pasw.insert(0, "Password")
pasw.bind("<FocusIn>", on_pass)
pasw.bind("<FocusOut>", out_pass)
Frame(log_frame, width=345, height=3, bg="black").place(x=60, y=210)

Button(log_frame, width=33, pady=7, text="Login", font=("Rowdies", 14, "bold"), bg="white", fg="#E27070", command=login, border=0).place(x=40, y=250)
noacc = Label(log_frame, text="Don't have an account?", fg="black", bg="#EAE0D5", font=("Roboto", 15))
noacc.place(x=100, y=330)
Button(log_frame, text="Register", font=("Roboto", 16, "underline"), bg="#EAE0D5", fg="#585FFF",command=register, cursor="hand2", border=0).place(x=310, y=325)

root.mainloop()