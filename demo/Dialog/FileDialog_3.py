#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''文件对话框, 格式限制, 保存文件'''

from tkinter import Tk, Button, filedialog


def openfile():
    r = filedialog.askopenfilename(
        title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(r)


def savefile():
    r = filedialog.asksaveasfilename(
        title='保存文件', initialdir='/', initialfile='hello.py')
    print(r)


root = Tk()
btn1 = Button(root, text='File Open', command=openfile)
btn2 = Button(root, text='File Save', command=savefile)

btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()
