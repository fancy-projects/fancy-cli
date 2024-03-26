import customtkinter as ctk
from input import Input, Entry, Text
from button import Button


class App(ctk.CTk):
    def __init__(self, width=None, height=None, geometry=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        geometry = geometry or f"{width}x{height}"

        if isinstance(geometry, tuple):
            geometry = f"{geometry[0]}x{geometry[1]}"
        elif geometry == "NonexNone":
            geometry = f"{self.winfo_screenwidth() // 3}x{self.winfo_screenheight() // 3}"

        self.geometry(geometry)

    add_input = Input
    add_entry = Entry
    add_text = Text

    add_window = ctk.CTkToplevel
    add_toplevel = add_window


Tk = App


def filedialog_command(filedialog, entry):
    entry.delete(0, ctk.END)
    entry.insert(0, str(filedialog))


if __name__ == "__main__":
    app = App()
    Button(left="left", right="right", up="up", down="down", text='center',
           command=lambda: ctk.filedialog.askopenfile('hasdf')).show(row=0, column=0)
    app.mainloop()
