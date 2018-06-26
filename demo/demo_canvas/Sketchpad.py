#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 模拟画板Sketchpad

import tkinter as gui

root = gui.Tk()

w = gui.Canvas(root, width=600, height=600)

w.pack()


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill="red")


w.bind("<B1-Motion>", paint)

gui.Label(root, text="使用鼠标左键开始画图").pack(side=gui.BOTTOM)

gui.mainloop()
