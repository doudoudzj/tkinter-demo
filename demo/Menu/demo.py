#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""菜单 demo"""

from tkinter import Tk, Menu
root = Tk()

# 创建菜单
menubar = Menu(root)

# 创建菜单，作为下拉菜单列表，是menubar的下一级
filemenu = Menu(menubar)

# 将下拉菜单filemenu放入菜单栏menubar上，直接依次显示
menubar.add_cascade(label="文件", menu=filemenu)

# 将菜单项添加到下拉菜单里，是filemenu的下一级
filemenu.add_command(label="文件打开")
filemenu.add_command(label="文件保存")
filemenu.add_command(label="文件关闭")

# 将菜单menubar放到窗口上，成为窗口菜单栏
# root.config(menu=menubar)
# or
root["menu"] = menubar
root.mainloop()