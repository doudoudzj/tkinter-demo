#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''颜色对话框'''

from tkinter import Tk, Button, Label, StringVar, colorchooser

root = Tk()
root.geometry('400x500')

text = StringVar()
text.set('请选择颜色')

lab = Label(root, textvariable=text).pack()


def open_color():
    color = colorchooser.askcolor(title='选择颜色', color='#333', parent=root)
    print(color == (None, None))
    if (color == (None, None)):
        text.set('未选择颜色')
    else:
        text.set('选中的颜色为:' + color[1])


Button(root, text='选择颜色', command=open_color).pack()

root.mainloop()
