import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Sticky Notes")
root.geometry("250x300")


notes = []

def add_note():
    new_note = note_input.get("1.0", "end-1c")
    if new_note != "":
        notes.append(new_note)
        update_list()
        note_input.delete("1.0", "end")
    else:
        messagebox.showerror("Error", "Please enter a note.")

def delete_note():
    if note_list.curselection():
        selected_index = note_list.curselection()[0]
        notes.pop(selected_index)
        update_list()
    else:
        messagebox.showerror("Error", "Please select a note to delete.")
def update_list():
    note_list.delete(0, "end")
    for note in notes:
        note_list.insert("end", note)

note_input = tk.Text(root, height=5, width=30)
note_input.pack()

add_button = tk.Button(root, text="Add", command=add_note)
add_button.pack()

note_list = tk.Listbox(root)
note_list.pack()

update_list()

delete_button = tk.Button(root, text="Delete", command=delete_note)
delete_button.pack()

root.mainloop()
