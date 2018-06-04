#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 点击按钮选择文件

from tkinter.filedialog import *
from tkinter import *


def opensdialog():
    filename = askopenfilename()
    label_filename['text'] = filename


root = Tk()

label_filename = Label(text=str('这里显示选中的文件路径'))
label_filename.pack()

button_opensdialog = Button(text=str('打开'), command=opensdialog)
button_opensdialog.pack()

root.mainloop()