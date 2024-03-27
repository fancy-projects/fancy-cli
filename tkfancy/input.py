import customtkinter as ctk
from base import BaseWidget


class Input(BaseWidget):
    """
    Initializes the Input object.

    Arguments:
        window: widget containing input, can be an App, Window, or Frame
        left: widget to left of input, if string will be converted to a label
        right: widget to right of input, if string will be converted to a label
        up: widget above input, if string will be converted to a label
        down: widget below input, if string will be converted to a label
        widget_type: 'entry' or 'text'
        text: prefilled text of input
        styles: style arguments, like bg (background color) or fg (foreground color)
    """

    def __init__(self, window: ctk.CTk = None, left: BaseWidget = None, right: BaseWidget = None,
                 up: BaseWidget = None, down: BaseWidget = None, *, widget_type: str = "entry",
                 text: str = "", **styles) -> None:

        self.config(window, left, right, up, down, widget_type=widget_type, text=text, **styles)

    def config(self, window: ctk.CTk = None, left: BaseWidget | str = None,
               right: BaseWidget | str = None, up: BaseWidget | str = None,
               down: BaseWidget | str = None, *, widget_type: str = "entry", text: str = "",
               **styles) -> None:
        """
        Configures the input options.

        Any of left, right, up, down will change rowspan and columnspan.

        Arguments:
            window: widget containing input, can be an App, Window, or Frame
            left: widget to left of input, if string will be converted to a label
            right: widget to right of input, if string will be converted to a label
            up: widget above input, if string will be converted to a label
            down: widget below input, if string will be converted to a label
            widget_type: 'entry' or 'text'
            text: prefilled text of input
            styles: style arguments, like bg (background color) or fg (foreground color)
        """

        super().config(window, left, right, up, down, **styles)

        if widget_type == "entry":
            self._input_widget = ctk.CTkEntry(window)
            self._input_widget.delete(0, "end")
            self._input_widget.insert(0, text)
        elif widget_type == "text":
            self._input_widget = ctk.CTkTextbox(window, font=styles.get('font'),
                                                bg_color=styles.get('bg') or "transparent",
                                                fg_color=styles.get('fg') or "transparent",
                                                border_width=3)
            self._input_widget.delete("0.0", "end")
            self._input_widget.insert("0.0", text)
        else:
            raise ValueError("Invalid widget_type. Must be 'entry' or 'text'.")

    def show(self, row: int = 0, column: int = 0, rowspan: int = 1, columnspan: int = 1,
             pady: int = 10, padx: int = 10, ipadx: int = 1, ipady: int = 1,
             sticky: str = 'nesw') -> None:
        """
        Displays the input on the grid.

        Arguments:
            row: row to display input in an imaginary grid
            column: column to display input in an imaginary grid
            rowspan: number of rows for input to span, to create stretched inputs
            columnspan: number of columns for input to span, to create tall inputs
            pady: extra pixels of padding in y direction
            padx: extra pixels of padding in x direction
            ipadx: extra pixels of inside-cell padding on the left and right sides of cell
            ipady: extra pixels of inside-cell padding on the top and bottom sides of cell
            sticky: which side for input to stick in its cell(s)
        """

        if self._side_options['left'] is not None:
            column += 1
        if self._side_options['up'] is not None:
            row += 1

        for side, widget in self._side_options.items():
            if side == "left":
                widget.grid(row=row, column=column - 1, padx=3, pady=3)
            elif side == "up":
                widget.grid(row=row - 1, column=column, padx=3, pady=3)
            elif side == "right":
                widget.grid(row=row - 1, column=column, padx=3, pady=3)

            self._input_widget.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                                    padx=padx, pady=pady, ipadx=ipadx, ipady=ipady, sticky=sticky)

    @classmethod
    def entry(cls, *args, **kwargs):
        """
        Returns an input with type 'entry'.
        """

        return cls(*args, widget_type="entry", **kwargs)

    @classmethod
    def text(cls, *args, **kwargs):
        """
        Returns an input with type 'text'.
        """

        return cls(*args, widget_type="text", **kwargs)


Entry, Text = Input.entry, Input.text
