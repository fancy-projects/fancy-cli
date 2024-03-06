from PIL import Image, ImageDraw, ImageTk

root = tk.Tk()

entry = tk.Entry(borderwidth=0, highlightthickness=0)
entry.grid(column=0, row=0)

image = Image.new("RGBA", (int(entry.winfo_reqwidth() * 1.1), int(entry.winfo_reqheight() * 1.1)))
draw = ImageDraw.Draw(image)
draw.rounded_rectangle(((0, 0), (int(entry.winfo_reqwidth() * 1.1), int(entry.winfo_reqheight() * 1.1))), 5,
                       outline="black", width=2)

image = ImageTk.PhotoImage(image)
entry_border = tk.Label(image=image)
entry_border.grid(column=0, row=0)

entry.tkraise(entry_border)
