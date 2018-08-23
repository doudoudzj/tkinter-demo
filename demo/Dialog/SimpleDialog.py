#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''简单对话框'''

from tkinter import Tk, Button, simpledialog


def inputStr():
    r = simpledialog.askstring('请输入', 'Input String', initialvalue='默认字符串')
    print(r)


def inputInt():
    r = simpledialog.askinteger('请输入', 'Input Integer')
    print(r)


def inputFloat():
    r = simpledialog.askfloat('请输入', 'Input Float')
    print(r)


root = Tk()
btn1 = Button(root, text='Input String', command=inputStr)
btn2 = Button(root, text='Input Integer', command=inputInt)
btn3 = Button(root, text='Input Float', command=inputFloat)

btn1.pack(side='left')
btn2.pack(side='left')
btn3.pack(side='left')

root.mainloop()