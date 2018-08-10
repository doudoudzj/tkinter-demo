#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# PanedWindow 控件
"""PanedWindow是一个窗口布局管理的插件，可以包含一个或者多个子控件。
用户可以用鼠标移动上面的分割线来改变每个子控件的大小。
PanedWindow可以用来创建2格或者3格的布局。
下面的例子演示了如何创建有2个窗格的PanedWindow插件。"""

from tkinter import *

win = Tk()

m = PanedWindow(win, orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane", bg="red")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

win.mainloop()
