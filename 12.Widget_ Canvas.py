#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 控件: Canvas

from tkinter import Tk, Canvas, mainloop

root = Tk()

w = Canvas(root)
w.configure(width=200, height=200, background='red')
w.create_line(0, 0, 200, 177)
w.create_line(0, 100, 200, 0, fill="gray")
w.create_rectangle(50, 25, 100, 75, fill="blue")  #矩形对角的两个坐标
w.pack()

mainloop()
