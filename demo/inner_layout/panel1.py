#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# PanedWindow 控件
"""创建3窗格"""

from tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane", bg="#ddd")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top pane", bg="#333", fg="#fff")
m2.add(top)

bottom = Label(m2, text="bottom pane")
m2.add(bottom)

mainloop()