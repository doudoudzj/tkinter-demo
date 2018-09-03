#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""控件: 下拉菜单OptionMenu"""

from tkinter import StringVar, Tk, OptionMenu
from tkinter.ttk import Button

master = Tk()

variable = StringVar(value="默认选项")

w = OptionMenu(master, variable, "默认选项", "选项一", "选项二")
w.pack()


def ok():
    print("选中的值为: " + variable.get())
    master.quit()


button = Button(master, text="OK", command=ok)
button.pack()

master.mainloop()
