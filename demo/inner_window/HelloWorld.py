#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

window = tkinter.Tk()
window.title('Hello World')
window.geometry("200x200+100+100")

label = tkinter.Label(window, text="Hello, World")
label.pack(fill=tkinter.BOTH, expand=1)

button = tkinter.Button(window, text="Exit", command=window.destroy)
button.pack(side=tkinter.BOTTOM)

window.mainloop()
