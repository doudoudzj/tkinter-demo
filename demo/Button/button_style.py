#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按钮 demo"""

from tkinter import Button, Tk

root = Tk()


def callback():
    return "aaa"


Button(
    root, text="按钮", fg="#555", bg="red", width=5, height=5,
    command=callback).pack()

root.mainloop()
