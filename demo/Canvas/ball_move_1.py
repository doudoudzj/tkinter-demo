#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# https://medium.com/@elan_73479/python-tkinter-module-tutorial-1-b1c097773f18
# https://medium.com/@elan_73479/python-tkinter-tutorial-4-making-a-animation-in-canvas-ff5801358e4e
# https://medium.com/@elan_73479/python-tkinter-tutorial-2-making-a-very-simple-login-889295115981
# https://medium.com/@elan_73479/python-tkinter-tutorial-3-radiobuttons-canvas-and-more-d38a0f457ff6

import tkinter as gui
import time

window = gui.Tk()
window.title("正在运动")

# var = gui.IntVar()
window.geometry("800x800")
c = gui.Canvas(window, width=800, height=800)
c.pack()

oval = c.create_oval(5, 5, 60, 60, fill='pink')
a = 5
b = 5
for x in range(0, 100):
    c.move(oval, a, b)
    window.update()
    time.sleep(.01)

window.title("哈哈")
window.mainloop()
