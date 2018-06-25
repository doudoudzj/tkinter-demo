#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 窗口居于 屏幕 正中央

import tkinter as tk

window = tk.Tk()
window.title('Hello World')

label = tk.Label(window, text="Hello, World")
label.pack(fill=tk.BOTH, expand=1)


def center_window(f, w, h):
    # 获取屏幕 宽、高
    ws = f.winfo_screenwidth()
    hs = f.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    f.geometry('%dx%d+%d+%d' % (w, h, x, y))


center_window(window, 500, 500)

window.mainloop()