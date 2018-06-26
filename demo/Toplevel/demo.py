# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 顶级窗口,

import tkinter as gui

root = gui.Tk()
root.title('主窗体')

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - 100
y = (hs / 2) - 100
root.geometry('%dx%d+%d+%d' % (200, 200, x, y))

top = gui.Toplevel()
top.title('默认弹出新窗口')


def create():
    x = gui.Toplevel()
    x.title('点击新增')
    x.geometry('200x100')
    msg = gui.Label(x, text='你好你好你好你好')
    msg.pack(expand=gui.YES, fill=gui.BOTH)
    msg = gui.Message(x, text='类似于弹出窗口，具有独立的窗口属性。', width=150)
    msg.pack()


gui.Button(
    root, text='创建顶级窗口', command=create).pack(
        expand=gui.YES)

gui.mainloop()
