#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''打开一个选择文件对话框'''

from tkinter import Tk, filedialog

root = Tk()

filename = filedialog.askopenfilename(parent=root)

print(filename)

root.mainloop()
