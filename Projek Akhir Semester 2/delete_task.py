from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

root = Tk()
root.title("Delete Task")
root.geometry("1280x720")
root.resizable(False,False)
root.configure(bg= "white")


img = PhotoImage(file="bg tampilkan task.png")
Label (root,image=img,bg ="#c5ac8e").place(x=0,y=0)

table_frame = Frame(root, width=1000, height=600, bg="black")
table_frame.place(x=180,y=150)
listbox_data = Listbox(table_frame, width=100)
listbox_data.pack(fill=BOTH, expand=True)

tree_scroll = Scrollbar(listbox_data)
tree_scroll.pack(side=RIGHT, fill=Y)

style = ttk.Style()
style.configure("Treeview", font=("Arial", 15))
style.configure("Treeview", rowheight=30)
style.configure("Treeview.Heading", font=("Arial", 16))

tree = ttk.Treeview(listbox_data, columns=("nama_task", "kategori", "tanggal_dibuat", "deadline", "lokasi"), show="headings")
tree.heading("nama_task", text="Nama Task", command=lambda: sort_data(tree, "nama_task"))
tree.heading("kategori", text="Kategori", command=lambda: sort_data(tree, "kategori"))
tree.heading("tanggal_dibuat", text="Tanggal Dibuat", command=lambda: sort_data(tree, "tanggal_dibuat"))
tree.heading("deadline", text="Deadline", command=lambda: sort_data(tree, "deadline"))
tree.heading("lokasi", text="Lokasi", command=lambda: sort_data(tree, "lokasi"))

tree.column("nama_task", width=210)
tree.column("kategori", width=160)
tree.column("tanggal_dibuat", width=180)
tree.column("deadline", width=180)
tree.column("lokasi", width=180)

tree.configure(yscrollcommand=tree_scroll.set)
tree_scroll.configure(command=tree.yview)


with open('tasks.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

    for row in data:
        tree.insert("", END, values=(row['nama_task'], row['kategori'], row['tanggal_dibuat'], row['deadline'], row['lokasi']))

tree.pack(fill=BOTH, expand=True)

search_frame = Frame(root, width=500, height=500)
search_frame.place(x=800,y=10)

search_label = Label(search_frame, text="Search:")
search_label.pack(side=LEFT)

search_entry = Entry(search_frame, font=("Arial", 14), width=20)
search_entry.pack(side=LEFT, padx=5, pady=5)


search_button = Button(search_frame, text="Cari", command=lambda: search_data(tree, search_entry.get()))
search_button.pack(side=LEFT)

sort_frame = Frame(root)
sort_frame.place(x=800,y=50)

sort_label = Label(sort_frame, text="Sort by:")
sort_label.pack(side=LEFT)

sort_combobox = ttk.Combobox(sort_frame, values=["Deadline Terdekat", "Deadline Terlama", "A-Z Nama Task", "Z-A Nama Task"], state="readonly", font=("Arial", 10))
sort_combobox.pack(side=LEFT)
sort_combobox.current(0)

sort_button = Button(sort_frame, text="Sort", command=lambda: sort_data_callback(sort_combobox, tree))
sort_button.pack(side=LEFT)


def binary_search(data, keyword):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid]['nama_task'].lower() == keyword.lower():
            return mid
        elif data[mid]['nama_task'].lower() < keyword.lower():
            low = mid + 1
        else:
            high = mid - 1

    return -1


def search_data(tree, keyword):
    tree.delete(*tree.get_children())

    if keyword:
        sorted_data = sorted(data, key=lambda x: x['nama_task'].lower())  # Sorting data berdasarkan nama_task
        index = binary_search(sorted_data, keyword)
        if index != -1:
            item = sorted_data[index]
            tree.insert("", END, values=(item['nama_task'], item['kategori'], item['tanggal_dibuat'], item['deadline'], item['lokasi']))
    else:
        for item in data:
            tree.insert("", END, values=(item['nama_task'], item['kategori'], item['tanggal_dibuat'], item['deadline'], item['lokasi']))




def merge_sort(data, column, descending=False):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]

    left_half = merge_sort(left_half, column, descending)
    right_half = merge_sort(right_half, column, descending)

    return merge(left_half, right_half, column, descending)


def merge(left, right, column, descending=False):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (left[i][0].lower() < right[j][0].lower() and not descending) or (left[i][0].lower() > right[j][0].lower() and descending):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def tree_sort_by_column(tree, column, descending=False):
    data = [(tree.set(child, column), child) for child in tree.get_children("")]
    sorted_data = merge_sort(data, column, descending)

    for index, (value, child) in enumerate(sorted_data):
        tree.move(child, "", index)



def sort_data_callback(column_var, tree):
    column = column_var.get()
    if column == "Deadline Terdekat":
        tree_sort_by_column(tree, "deadline", descending=False)
    elif column == "Deadline Terlama":
        tree_sort_by_column(tree, "deadline", descending=True)
    elif column == "A-Z Nama Task":
        tree_sort_by_column(tree, "nama_task", descending=False)
    elif column == "Z-A Nama Task":
        tree_sort_by_column(tree, "nama_task", descending=True)


def delete_task():
    selected_items = tree.selection()

    if selected_items:
        confirmation = messagebox.askyesno("Delete Task", "Apakah Anda yakin ingin menghapus task ini?")

        if confirmation:
            for item in selected_items:
                values = tree.item(item, "values")
                nama_task = values[0]

                tree.delete(item)

                with open('tasks.csv', 'r') as file:
                    reader = csv.DictReader(file)
                    data = list(reader)

                for i, row in enumerate(data):
                    if row['nama_task'] == nama_task:
                        del data[i]
                        break

                with open('tasks.csv', 'w', newline='') as file:
                    fieldnames = ['nama_task', 'kategori', 'tanggal_dibuat', 'deadline', 'lokasi']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(data)

            messagebox.showinfo("Delete Task", "Task berhasil dihapus.")
    else:
        messagebox.showwarning("Delete Task", "Mohon pilih task yang ingin dihapus.")


def back_to_menu():
    root.destroy()
    import homepage



delete_button = Button(root, text="Delete Task",bg="#9C6666" ,fg="white",width=15, height=2, command=delete_task)
delete_button.place(x=860, y=550)


back_button = PhotoImage(file="back_to_menu.png")
button = Button(root, bd=0, highlightthickness=-1, activebackground="#EAE0D5")
button.config(image=back_button, width=270, height=35, bg="#EAE0D5", command=back_to_menu)
button.place(x=10,y=105)



root.mainloop()