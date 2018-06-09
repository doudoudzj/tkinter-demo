#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 弹出菜单

import tkinter

root = tkinter.Tk()


def callback():
    pass6


menubar = tkinter.Menu(root)
menubar.add_command(label="撤销", command=callback)
menubar.add_command(label="重置", command=callback)
menubar.add_command(label="复制", command=callback)

frame = tkinter.Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menubar.post(event.x_root, event.y_root)


frame.bind("<Button-3>", popup)
tkinter.mainloop()