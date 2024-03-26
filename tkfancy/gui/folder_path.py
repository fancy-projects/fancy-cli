from tkinter import END
from tkinter.ttk import Label, Entry, Button
from tkinter.filedialog import askopenfile
from fancy.api import get_folder_icon
from pathlib import Path

folder_path = str(get_folder_icon()).replace(str(Path.home()), "~")


def select_folder_path():
    path = askopenfile(defaultextension='.icns')
    folder_entry.delete(0, END)
    folder_entry.insert(0, str(path))


folder_label = Label(text="Folder icon path: devs only")
folder_label.grid(row=3, column=0)

folder_entry = Entry()
folder_entry.insert(0, folder_path)
folder_entry.grid(row=3, column=1)

folder_button = Button(text="Select", command=select_folder_path)
folder_button.grid(row=3, column=2)
