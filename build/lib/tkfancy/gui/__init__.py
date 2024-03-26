from tkinter import Tk
from tkinter.ttk import Style, Label, Button
from fancy.api import overlay_icon
from pathlib import Path

root = Tk()
root.title("Folder Art with Neat Colors for You - FANCY")
root.geometry("640x360")

style = Style()
style.configure("Title.TLabel", font=("Arial", 50, "bold"))

style = Style()
style.configure("green_big.TLabel", font=("Arial", 50, "bold"), foreground="green")

title_label = Label(text="FANCY Beta", style="Title.TLabel")
title_label.grid(row=0, column=0, pady=20)

import icon_path
import folder_color
import icon_size
import folder_path


def run_fancy():
    icon_path_data = Path(icon_path.icon_entry.get()).expanduser()
    output_path_data = Path(icon_path.output_entry.get()).expanduser()
    folder_path_data = Path(folder_path.folder_entry.get()).expanduser()
    icon_size_data = float(icon_size.icon_size_entry.get())
    folder_color_data = folder_color.folder_color_var.get()

    overlay_icon(folder_path_data, icon_path_data, output_path_data, folder_color_data, icon_size_data)

    Label(text="Success", style="green_big.TLabel").grid(row=7, column=0, columnsoan=3)


Button(text="Make your folders fancy!", command=run_fancy).grid(row=6, column=0, columnspan=3)

root.mainloop()
