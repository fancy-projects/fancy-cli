import customtkinter as ctk
from base import BaseWidget
from docstrings import doc, input_init


class Button(BaseWidget):

    @doc(input_init)
    def __init__(self, window: ctk.CTk = None, left: BaseWidget = None, right: BaseWidget = None,
                 up: BaseWidget = None, down: BaseWidget = None, *, widget_type: str = "entry",
                 text: str = "", **styles) -> None:
        self.config(window, left, right, up, down, text=text, **styles)

    def config(self, window: ctk.CTk = None, left: BaseWidget | str = None,
               right: BaseWidget | str = None, up: BaseWidget | str = None,
               down: BaseWidget | str = None, *, text: str = "", command: callable = None,
               **styles) -> None:
        """Configures the button options.

        Any of left, right, up, down will change rowspan and columnspan.

        Arguments:
            window: widget containing button, can be an App, Window, or Frame
            left: widget to left of button, if string will be converted to a label
            right: widget to right of button, if string will be converted to a label
            up: widget above button, if string will be converted to a label
            down: widget below button, if string will be converted to a label
            text: button label
            command: function to call when button is clicked (can be a lambda)
            styles: style arguments, like bg (background color) or fg (foreground color)
        """

        super().config(window, left, right, up, down, **styles)

        self._button_widget = ctk.CTkButton(window, text=text, command=command)

    def show(self, row: int = 0, column: int = 0, rowspan: int = 1, columnspan: int = 1,
             pady: int = 10, padx: int = 10, ipadx: int = 1, ipady: int = 1,
             sticky: str = 'nesw') -> None:

        """
        Displays the button on the axis.

        Arguments:
            row: row to display button in an imaginary grid
            column: column to display button in an imaginary grid
            rowspan: number of rows for button to span, to create stretched buttons
            columnspan: number of columns for button to span, to create tall buttons
            pady: extra pixels of padding in y direction
            padx: extra pixels of padding in x direction
            ipadx: extra pixels of inside-cell padding on the left and right sides of cell
            ipady: extra pixels of inside-cell padding on the top and bottom sides of cell
            sticky: which side for button to stick in its cell(s)

        """

        if self._side_options['left'] is not None:
            column += 1
        if self._side_options['up'] is not None:
            row += 1

        for side, widget in self._side_options.items():
            print(row, column)
            if side == "left":
                widget.grid(row=row, column=column - 1, padx=3, pady=3)
            elif side == "up":
                widget.grid(row=row - 1, column=column, padx=3, pady=3)
            elif side == "right":
                widget.grid(row=row, column=column + 1, padx=3, pady=3)
            elif side == "down":
                widget.grid(row=row + 1, column=column, padx=3, pady=3)

        self._button_widget.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                                 padx=padx, pady=pady, ipadx=ipadx, ipady=ipady, sticky=sticky)
