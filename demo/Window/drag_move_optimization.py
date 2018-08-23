#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 窗口拖动移动, 窗口大小可调节, 但是窗口会抖动

from tkinter import Tk, Canvas

root = Tk()

# 初始窗口居中
window_w = 300  # 默认宽度
window_h = 200  # 默认高度
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws - window_w) / 2
y = (hs - window_h) / 2 - 30  # 去掉窗口标题栏高度差
root.geometry('%dx%d+%d+%d' % (window_w, window_h, x, y))

canvas = Canvas(root)
canvas.configure(width=300, height=200, bg="blue")
canvas.configure(highlightthickness=0)
canvas.pack()


def move(event):
    global x, y
    new_x = (event.x - x) + root.winfo_x()
    new_y = (event.y - y) + root.winfo_y()
    s = '%dx%d+%d+%d' % (window_w, window_h, new_x, new_y)
    root.geometry(s)
    print("s = ", s)
    print(root.winfo_x(), root.winfo_y())
    print(event.x, event.y)
    print()


def button_1(event):
    global x, y
    x, y = event.x, event.y
    global window_w, window_h
    window_w, window_h = root.winfo_width(), root.winfo_height()
    print("event.x, event.y = ", event.x, event.y)


canvas.bind("<B1-Motion>", move)
canvas.bind("<Button-1>", button_1)

root.mainloop()
