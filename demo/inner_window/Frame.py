#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter.constants import *

root = tkinter.Tk()

frame = tkinter.Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=10)

label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)

button = tkinter.Button(frame, text="Exit", command=root.destroy)
button.pack(side=BOTTOM)

root.mainloop()
