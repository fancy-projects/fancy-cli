from tkinter.ttk import *

icon_size_label = Label(text="Icon size percent:")
icon_size_label.grid(row=4, column=0)

icon_size_entry = Entry()
icon_size_entry.grid(row=4, column=1)

icon_size_label = Label(text="%")
icon_size_label.grid(row=4, column=2, sticky="W")
