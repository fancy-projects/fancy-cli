import tkinter as tk
from tkinter import ttk

App = tk.Tk
Tk = App


class App(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("640x360")


class Input:
    def __init__(self, window=None, default_text="", label=None, label_side="left", **styles):
        self._input_widget = ttk.Entry(window, font=styles.get('font'), background=styles.get('bg'),
                                       foreground=styles.get('fg'))
        self._input_widget.insert(0, default_text)

        self._label = label
        if isinstance(self._label, str):
            self._label = ttk.Label(text=self._label)
        self._label_side = label_side

    def config(self, window=None, default_text="", label=None, label_side="left", **styles):
        self._input_widget = ttk.Entry(window, font=styles.get('font'), background=styles.get('bg'),
                                       foreground=styles.get('fg'))

        self._input_widget.delete(0, tk.END)
        self._input_widget.insert(0, default_text)

        self._label = label
        if isinstance(self._label, str):
            self._label = ttk.Label(text=self._label)
        self._label_side = label_side

    def show(self, row=0, column=0, rowspan=1, columnspan=1, padx=0, pady=0, ipadx=7, ipady=7, sticky='nesw'):
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


Entry = Input

# app = App()
# Input(label="hello").show(row=0, column=0)
# Input(label='hello').show(row=0, column=1)
# app.mainloop()
