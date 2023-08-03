from tkinter import *
from tkinter import messagebox



root = Tk()
root.title ('homepage')
root.geometry('1280x720')
root.configure(bg="#c5ac8e")
root.resizable (False,False)


def tampilkan_task():
    root.destroy()
    import tampilkan_task

def hapus_task():
    root.destroy()
    import delete_task

def tambah_task():
    root.destroy()
    import tambah_task

def edit_task():
    root.destroy()
    import edit_task

img = PhotoImage(file="bg homepage.png")
Label (root,image=img,bg ="#c5ac8e").place(x=0,y=0)

#------------------------------------------------------------------

#button tampilan task
button_tampilan_task = PhotoImage(file="tampilkan task.png")
button = Button(root, bd=0, highlightthickness=0, activebackground="#c5ac8e")
button.config(image=button_tampilan_task, width=390, height=120, bg="#c5ac8e", command=tampilkan_task)
button.place(x=120,y=200)

#button hapus task
button_hapus_task = PhotoImage(file="hapus task.png")
button = Button(root, bd=0, highlightthickness=0, activebackground="#c5ac8e")
button.config(image=button_hapus_task, width=390, height=120, bg="#c5ac8e", command=hapus_task)
button.place(x=120,y=400)

#button tambah task
button_tambah_task = PhotoImage(file="tambah task.png")
button = Button(root, bd=0, highlightthickness=-1, activebackground="#EAE0D5")
button.config(image=button_tambah_task, width=390, height=120, bg="#EAE0D5", command=tambah_task)
button.place(x=800,y=200) 

#button edit task
button_edit_task = PhotoImage(file="edit task.png")
button = Button(root, bd=0, highlightthickness=-1, activebackground="#EAE0D5")
button.config(image=button_edit_task, width=390, height=120, bg="#EAE0D5", command=edit_task)
button.place(x=800,y=400)

root.mainloop()