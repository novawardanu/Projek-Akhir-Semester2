from tkinter import *
from datetime import datetime
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import Combobox
import tkinter as tk
import openpyxl ,xlrd
from openpyxl import Workbook
import pathlib
import csv
from tkinter import Tk, Label, PhotoImage
from PIL import ImageTk, Image

root = Tk()
root.title("Tambahkan Task")
root.geometry("1280x720")
root.resizable(False,False)
root.configure(bg= "white")

img = PhotoImage(file="bg tambah task.png")
Label (root,image=img,bg ="#c5ac8e").place(x=0,y=0)

def tambahkan():
    nama_task = namaEntry.get()
    kategori = kategori_combobox.get()
    tanggal_dibuat = TglEntry.get()
    deadline = deadlineEntry.get()
    lokasi = Lokasi.get()

    if not nama_task or not kategori or not tanggal_dibuat or not deadline or not lokasi:
        messagebox.showerror("Error", "Harap lengkapi semua field")
    else:
        task = {
            'nama_task': nama_task,
            'kategori': kategori,
            'tanggal_dibuat': tanggal_dibuat,
            'deadline': deadline,
            'lokasi': lokasi
        }
        with open('tasks.csv', 'a', newline='') as file:
            fieldnames = ['nama_task', 'kategori', 'tanggal_dibuat', 'deadline', 'lokasi']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(task)
        messagebox.showinfo("Sukses", "Task berhasil ditambahkan")

        namaEntry.delete(0, END)
        kategori_combobox.set("")
        TglEntry.delete(0, END)
        TglEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        deadlineEntry.delete(0, END)
        deadlineEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
        Lokasi.delete(0, END)

def reset():
    namaEntry.delete(0, END)
    kategori_combobox.set("")
    TglEntry.delete(0, END)
    TglEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    deadlineEntry.delete(0, END)
    deadlineEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))
    Lokasi.delete(0, END)

def kembali():
    root.destroy()
    import homepage

namaEntry = Entry(root, width=45, bd=1, font=20)
namaEntry.place(x=400, y=167)

kategori_combobox = Combobox(root, values=["Tugas Kuliah", "Event Ormawa", "Lomba", "Lainnya"], font="arial 11", state="r", width=14)
kategori_combobox.place(x=400, y=247)
kategori_combobox.current(0)

TglEntry = Entry(root, width=15, bd=1, font="arial 10")
TglEntry.place(x=400, y=324)
TglEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))

deadlineEntry = Entry(root, width=15, bd=1, font="arial 10")
deadlineEntry.place(x=400, y=404)
deadlineEntry.insert(0, datetime.now().strftime("%Y-%m-%d"))

Lokasi = Entry(root, bd=1, font="arial 10")
Lokasi.place(x=400, y=480)

Button(root, text="Tambahkan", bg="#9C6666", fg="white", width=15, height=2, command=tambahkan).place(x=940, y=600)
Button(root, text="Reset", bg="#9C6666", fg="white", width=15, height=2, command=reset).place(x=800, y=600)

back_button = PhotoImage(file="back button.png")
button = Button(root, bd=0, highlightthickness=-1, activebackground="#EAE0D5")
button.config(image=back_button, width=27, height=35, bg="#EAE0D5", command=kembali)
button.place(x=30, y=105)

root.mainloop()
