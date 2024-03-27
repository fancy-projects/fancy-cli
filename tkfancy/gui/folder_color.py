from tkinter import StringVar
from tkinter.ttk import *

folder_color_label = Label(text="Folder color:")
folder_color_label.grid(row=5, column=0)

colors = ["default", "windows", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]
folder_color_var = StringVar()
folder_color_var.set("default")

folder_color_menu = OptionMenu(None, folder_color_var, *colors)
folder_color_menu.grid(row=5, column=1)
