import customtkinter as ctk


class BaseWidget:
    """Base widget class"""

    def config(self, window: ctk.CTk = None, left: ctk.CTkLabel = None, right: ctk.CTkLabel = None,
               up: ctk.CTkLabel = None, down: ctk.CTkLabel = None, **styles) -> None:
        """Configure widget placement"""

        self._side_options = {"left": left, "right": right, "up": up, "down": down}

        self._side_options = {widget_side: ctk.CTkLabel(window, text=widget)
                              if isinstance(widget, str) else widget
                              for widget_side, widget in self._side_options.items()}

        self._side_options = {key: value for key, value in self._side_options.items()
                              if value is not None}
