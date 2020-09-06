# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
设置Toplevel的属性
title设置标题
geometry设置宽和高
'''

from tkinter import *
root = Tk()

tl = Toplevel()

# 设置tl的title
tl.title('hello Toplevel')

# 设置tl在宽和高
tl.geometry('400x300')

# 为了区别root和tl，我们向tl中添加了一个Label
Label(tl, text='hello label').pack()

root.mainloop()
