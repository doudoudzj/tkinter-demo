#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from tkinter import Tk, Checkbutton, Label
from tkinter import StringVar, IntVar

root = Tk()
root.title("界面更新示例-1")
root.geometry("200x100+200+200")
root.update()

text = StringVar()
text.set('默认值')
status = IntVar()

def change():
    if status.get() == 1:   # if clicked
        text.set('已选中')
    else:
        text.set('未选中')

Checkbutton(root, variable=status, command=change).pack()
Label(root, textvariable=text).pack()

root.mainloop()
