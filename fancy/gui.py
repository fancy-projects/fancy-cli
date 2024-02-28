from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("640x360")
root.title("FANCY Folders")

color_options = ["default", "red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink"]

color_var = StringVar(root)
color_var.set("default")

Label(text="Select Color:").grid(row=0, column=1)
OptionMenu(root, color_var, *color_options).grid(row=0, column=2)

Style().configure('bd', font=('', '50', ''), background='red')
Button(root, text="Create Folder", name="bd", style='bd', command=lambda: ...).grid_configure(row=1, column=1,
                                                                                              columnspan=2)

root.mainloop()
