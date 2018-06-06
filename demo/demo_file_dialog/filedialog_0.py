# -*- coding: CP936 -*-

from tkinter import *
from tkinter.filedialog import *
root = Tk()

filename = askopenfilename(parent=root)

print(filename)

root.mainloop()