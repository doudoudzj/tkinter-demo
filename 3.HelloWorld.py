#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter.constants import *

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=10)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()