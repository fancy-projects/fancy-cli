from functools import wraps


def doc(docstring):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            func.__doc__ = docstring
            return func(*args, **kwargs)
        return wrapper
    return decorator


input_init = (
    """
    Initializes the Button object.

    Arguments:
        window: widget containing button, can be an App, Window, or Frame
        left: widget to left of button, if string will be converted to a label
        right: widget to right of button, if string will be converted to a label
        up: widget above button, if string will be converted to a label
        down: widget below button, if string will be converted to a label
        text: button label
        styles: style arguments, like bg (background color) or fg (foreground color)
    """
)
