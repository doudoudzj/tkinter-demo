#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 点击按钮选择文件

from tkinter.filedialog import *
from tkinter import *

root = Tk()
# root.geometry('600x200')

selectedFile = Label(text=str('这里显示选中的文件路径'))
selectedFile.pack()


def openFileDialog():
    filename = askopenfilename()
    selectedFile['text'] = filename

buttonOpen = Button(text=str('打开'), command=openFileDialog)
buttonOpen.pack()

root.mainloop()