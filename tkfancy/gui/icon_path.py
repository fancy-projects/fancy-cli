from tkinter import filedialog, END
from tkinter.ttk import Label, Button, Entry

from pathlib import Path


def select_icon_path():
    path = filedialog.askopenfilename(defaultextension=".icns")
    path = str(path).replace(str(Path.home()), "~")
    icon_entry.delete(0, END)
    icon_entry.insert(0, str(path))
    return path


def select_output_path():
    path = filedialog.asksaveasfile(defaultextension=".icns")
    path = str(path).replace(str(Path.home()), "~")
    output_entry.delete(0, END)
    output_entry.insert(0, str(path))
    return path


icon_label = Label(text="Icon path:")
icon_label.grid(row=1, column=0)

icon_entry = Entry()
icon_entry.grid(row=1, column=1)

icon_button = Button(text="Select", command=select_icon_path)
icon_button.grid(row=1, column=2)

output_label = Label(text="Output folder path:")
output_label.grid(row=2, column=0)

output_entry = Entry()
output_entry.insert(0, "~/Downloads/icon.icns")
output_entry.grid(row=2, column=1)

output_button = Button(text="Select", command=select_icon_path)
output_button.grid(row=2, column=2)
