#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' 控件: 标签Button
说明: 创建按钮
用法:
    Button(根对象, [属性列表])
'''

from tkinter import *

root = Tk()
root.title("标签Button")
root.geometry('500x500')

t = Text(root)
t.insert(1.0, 'hello\n')
t.insert(END, 'hello000000\n')
t.insert(END, 'nono')
t.pack()


def doPrint():
    t.insert(END, "你好你好\n")


Button(root, text='点击插入字符串', command=doPrint).pack()

root.mainloop()