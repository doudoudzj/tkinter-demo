#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 如何disable右键菜单里面的某个命令？
# 使用mehu的entryconfigure方法，demo如下：

from tkinter import *

root = Tk()

#panel = Frame(root)

#panel.pack()

m = Menu(root, tearoff=0)

m.add_command(label='test1')

m.add_command(label='test2')


def context_menu(event):

    m.post(event.x, event.y)


root.geometry("400x400+0+0")

root.bind('<3>', context_menu)

m.entryconfigure(1, state='disabled')

root.mainloop()