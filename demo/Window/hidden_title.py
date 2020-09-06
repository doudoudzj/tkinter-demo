#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 隐藏窗口的标题栏
# Toplevel
# 只对Toplevel级别的窗口有效，使用其overrideredirect方法

from tkinter import Tk, Toplevel

root = Tk()
root.title('主窗口')

top = Toplevel(root)
top.title('子窗口')

# root.overrideredirect(True)
top.overrideredirect(True)

root.mainloop()
