from tkinter import *

root = Tk()
canvas = Canvas(root)
canvas.pack()
canvas.config(width=500, height=500)

line = canvas.create_line(40, 70, 79, 140, fill='red', width=1)

root.mainloop()
