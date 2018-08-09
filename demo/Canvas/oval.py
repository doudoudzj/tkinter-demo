#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 使用 Canvas 画椭圆

from tkinter import Tk, Canvas

window = Tk()
window.title("画椭圆")
window.resizable(False, False)

top = 130
bottom = 130
canvas = Canvas(window, width=500, height=500, bg='white')
for i in range(20):
    canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
    top -= 5
    bottom += 5

canvas.pack()

window.mainloop()
