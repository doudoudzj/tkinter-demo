#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 菜单栏

import tkinter

root = tkinter.Tk()

menubar = tkinter.Menu(root)


def callback():
    pass


filemenu = tkinter.Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=callback)
filemenu.add_command(label="保存", command=callback)
filemenu.add_separator()
filemenu.add_command(label="退出", command=callback)
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = tkinter.Menu(menubar, tearoff=False)
editmenu.add_command(label="复制", command=callback)
editmenu.add_command(label="粘贴", command=callback)
editmenu.add_separator()
editmenu.add_command(label="退出", command=callback)
menubar.add_cascade(label="编辑", menu=editmenu)

root.config(menu=menubar)
tkinter.mainloop()
