#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 如何打开一个选择文件对话框？

from tkinter import *
from tkinter.filedialog import *
root = Tk()

filename = askopenfilename(parent=root)

print(filename)

root.mainloop()