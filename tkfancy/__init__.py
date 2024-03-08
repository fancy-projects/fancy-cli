import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry(f"{self.winfo_screenwidth() // 4}x{self.winfo_screenheight() // 4}")

    @staticmethod
    def add_input(*args, **kwargs):
        return Input(*args, **kwargs)

    add_entry = add_input

    @staticmethod
    def add_window(*args, **kwargs):
        return ctk.CTkToplevel(*args, **kwargs)


Tk = App


class Input:
    def __init__(self, window=None, default_text="", left=None, right=None,
                 up=None, down=None, widget_type="entry", **styles):

        self._input_widget = None
        self._label = None

        self.config(window, default_text, left, right, up, down, widget_type, **styles)

    def config(self, window=None, default_text="", left=None, right=None,
               up=None, down=None, widget_type="entry", **styles):
        if widget_type == "entry":
            self._input_widget = ctk.CTkEntry(window, font=styles.get('font'),
                                              bg_color=styles.get('bg') or "transparent",
                                              fg_color=styles.get('fg') or "transparent")
            self._input_widget.delete(0, "end")
            self._input_widget.insert(0, default_text)
        elif widget_type == "text":
            self._input_widget = ctk.CTkTextbox(window, font=styles.get('font'),
                                                bg_color=styles.get('bg') or "transparent",
                                                fg_color=styles.get('fg') or "transparent")
            self._input_widget.delete("0.0", "end")
            self._input_widget.insert("0.0", default_text)
        else:
            raise ValueError("Invalid widget_type. Must be 'entry' or 'text'.")

        self._label = left or right or up or down
        self._label_side = "left" if left else ("right" if right else ("up" if up else ("down"
                            if down else "left")))

        if isinstance(self._label, str):
            self._label = ctk.CTkLabel(window, text=self._label)

    def show(self, row=0, column=0, rowspan=1, columnspan=1, pady=10, padx=10, ipadx=1, ipady=1,
             sticky='nesw'):
        if self._label:
            match self._label_side:
                case "left":
                    self._label.grid(row=row, column=column)
                    column += 1
                case "right":
                    self._label.grid(row=row, column=column + 1)
                case "up":
                    self._label.grid(row=row, column=column)
                    row += 1
                case "down":
                    self._label.grid(row=row + 1, column=column)
        self._input_widget.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                                padx=padx, pady=pady, ipadx=ipadx, ipady=ipady, sticky=sticky)

    grid = show

    @classmethod
    def entry(cls, *args, **kwargs):
        return cls(*args, widget_type="entry", **kwargs)

    @classmethod
    def text(cls, *args, **kwargs):
        return cls(*args, widget_type="text", **kwargs)


def Entry(*args, **kwargs):
    return Input.entry(*args, **kwargs)


def Text(*args, **kwargs):
    return Input.text(*args, **kwargs)

if __name__ == "__main__":
    app = App()
    Input(left="Wow!").show(row=0, column=1)
    app.mainloop()
