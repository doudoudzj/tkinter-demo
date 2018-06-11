#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 控件: 下拉菜单OptionMenu

import tkinter

master = tkinter.Tk()

variable = tkinter.StringVar(master)
variable.set("one")  # <em>default value</em>

w = tkinter.OptionMenu(master, variable, "one", "two", "three")
w.pack()


def ok():
    print("选中的值为: " + variable.get())
    master.quit()


button = tkinter.Button(master, text="OK", command=ok)
button.pack()



tkinter.mainloop()
