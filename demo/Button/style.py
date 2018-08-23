#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''
按钮样式
'''

from tkinter import Tk, Button
root = Tk()

B1 = Button(root, text='按扭一')
B1['height'] = 5
B1['width'] = 20

B2 = Button(root, text='按扭二')
B2['height'] = 5
B2['width'] = 18
B2['background'] = 'green'

B1.pack()
B2.pack()

root.mainloop()