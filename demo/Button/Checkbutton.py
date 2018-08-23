#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''Checkbutton'''

from tkinter import Tk, Label, Checkbutton, IntVar

root = Tk()

value_a = IntVar()
value_a.set(1)

Label(root, text='一般样式').pack()
Checkbutton(root, text='CheckButton1', variable=value_a, onvalue=1, offvalue=2).pack()
Checkbutton(root, text='CheckButton2', variable=value_a, onvalue=2, offvalue=2).pack()
Checkbutton(root, text='CheckButton3', variable=value_a, onvalue=3, offvalue=2).pack()
Checkbutton(root, text='CheckButton4', variable=value_a, onvalue=4, offvalue=2).pack()

value_b = IntVar()
value_b.set(2)

Label(root, text='平坦样式').pack()
Checkbutton(root, text='CheckButton1', variable=value_b, onvalue=1, offvalue=2, indicatoron=0).pack()
Checkbutton(root, text='CheckButton2', variable=value_b, onvalue=2, offvalue=2, indicatoron=0).pack()
Checkbutton(root, text='CheckButton3', variable=value_b, onvalue=3, offvalue=2, indicatoron=0).pack()
Checkbutton(root, text='CheckButton4', variable=value_b, onvalue=4, offvalue=2, indicatoron=0).pack()

root.mainloop()
