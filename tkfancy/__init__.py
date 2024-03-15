import customtkinter as ctk
from input import Input, Entry, Text


class App(ctk.CTk):
    def __init__(self, width=None, height=None, geometry=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        geometry = geometry or f"{width}x{height}"
        print(geometry)
        if isinstance(geometry, tuple):
            geometry = f"{geometry[0]}x{geometry[1]}"
        elif geometry == "NonexNone":
            print('hi')
            geometry = f"{self.winfo_screenwidth() // 4}x{self.winfo_screenheight() // 4}"
            print(geometry)

        self.geometry(geometry)
        self.configure()

    add_input = Input
    add_entry = add_input

    add_window = ctk.CTkToplevel
    add_toplevel = add_window


Tk = App





if __name__ == "__main__":
    app = App()
    Input.entry(left="Wow!").show(row=0, column=0)
    Text(up="T!").show(row=0, column=2)
    app.mainloop()
