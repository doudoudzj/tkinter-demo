#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''Radiobutton'''

from tkinter import Tk, Label, Radiobutton, StringVar

root = Tk()

value_a = StringVar()
value_a.set('1')

Label(root, text='一般样式').pack()
Radiobutton(root, variable=value_a, value='1', text='Radio1').pack()
Radiobutton(root, variable=value_a, value='2', text='Radio2').pack()
Radiobutton(root, variable=value_a, value='3', text='Radio3').pack()
Radiobutton(root, variable=value_a, value='4', text='Radio4').pack()

value_b = StringVar()
value_b.set('1')

Label(root, text='平坦样式').pack()
Radiobutton(root, variable=value_b, value='3', text='Radio1', indicatoron=0).pack()
Radiobutton(root, variable=value_b, value='4', text='Radio2', indicatoron=0).pack()
Radiobutton(root, variable=value_b, value='5', text='Radio3', indicatoron=0).pack()
Radiobutton(root, variable=value_b, value='6', text='Radio4', indicatoron=0).pack()

root.mainloop()
