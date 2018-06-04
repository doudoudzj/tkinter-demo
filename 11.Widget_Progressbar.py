#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 控件: 进度条Progressbar

from tkinter.ttk import *
from tkinter import *

root = Tk()
root.title('进度条Progressbar')


def oncolClick():
    print('you clicked', tv['value'] / tv['maximum'] * 100, '%')
    tv.step(5)


# command 指定按钮调用的函数
b = Button(root, text='点击', command=oncolClick)
# b['text'] = '哈哈'
b['width'] = 10
b['height'] = 2
b.pack()

tv = ttk.Progressbar(
    root, orient='horizontal', length=500, mode='determinate', value=0)
tv.pack()

root.mainloop()