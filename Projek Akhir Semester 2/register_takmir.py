from tkinter import *
from tkinter import messagebox as mbox
from csv import *
import csv

root = Tk()
root.title("register")
root.geometry("1280x720")
root.config(bg="#c5ac8e")
root.resizable(False, False)

background = PhotoImage(file="bg login dan register.png")
Label(root,image=background, bg="#c5ac8e").place(x=0,y=0)
#--------------------------------------------------------------------------

log_frame = Frame(root, width=483, height=450, bg='#EAE0D5')#"#c5ac8e")
log_frame.place(x=720, y=150)

header = Label(text="Register", fg="#E27070", bg="#EAE0D5", font=("Rowdies", 64, "bold"))
header.place(x=780, y=60)

def signup():
    username = user.get()
    password = pasw.get()
    confirm_password = con_pasw.get()

    if confirm_password == password:
        file = open("datauser.csv", 'a', newline="")
        data = [username,password]
        csvfile = writer(file)
        csvfile.writerow(data)
        mbox.showinfo("Selamat", "Register Telah Berhasil")
        file.close()
    else:
        mbox.showerror("Peringatatan", "Password yang anda masukkan salah")

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

def on_confirm(e):
    con_pasw.delete(0, "end")

def out_confirm(e):
    fill = con_pasw.get()
    if fill == "":
        con_pasw.insert(0, "Confirm Password")

def login():
    root.destroy()
    import login_takmir
    
#===============================================================================================  

user = Entry(log_frame, width=25, fg="black", border=0, bg="#EAE0D5", font=("Roboto", 12))
user.place(x=60, y=100)
user.insert(0, "Username")
user.bind("<FocusIn>", on_name)
user.bind("<FocusOut>", out_name)
Frame(log_frame, width=345, height=3, bg='black').place(x=60, y=130)

pasw = Entry(log_frame, width=25, fg="black", border=0, bg="#EAE0D5", font=("Roboto", 12))
pasw.place (x=60,y=180)
pasw.insert(0, "Password")
pasw.bind("<FocusIn>", on_pass)
pasw.bind("<FocusOut>", out_pass)
Frame(log_frame, width=345, height=3, bg='black').place(x=60, y=210)

con_pasw =Entry(log_frame, width=25, fg="black", border=0, bg="#EAE0D5", font=("Roboto", 12))
con_pasw.place(x=60,y=260)
con_pasw.insert(0, "Confirm Password")
con_pasw.bind("<FocusIn>", on_confirm)
con_pasw.bind("<FocusOut>", out_confirm)
Frame(log_frame, width=345, height=3, bg='black').place(x=60, y=290)

Button(log_frame, width=33, pady=7, text="Register", font=("Rowdies", 14, "bold"), bg='white', fg='#E27070', command=signup, border=0).place(x=30, y=310)
noacc = Label(log_frame, text="Already have an account?", fg='black', bg='#EAE0D5', font=("Roboto", 15))
noacc.place(x=95, y=390)

Button(log_frame, text="Login", font=("Roboto", 16, "underline"),  bg="#EAE0D5", fg="#585FFF", command=login, cursor="hand2", border=0).place(x=327, y=383)

root.mainloop()



