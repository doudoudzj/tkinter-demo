# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# grid几何布局管理器

import tkinter as gui

window = gui.Tk()
window.title('Grid')
window.geometry('400x400+250+140')

label = gui.Label(
    text='My Label', fg='red', bg='white').grid(
        row=0, column=0, sticky=gui.E)
label = gui.Label(
    text='你好', fg='blue', bg='white').grid(
        row=1, column=1, sticky=gui.E)

window.mainloop()
