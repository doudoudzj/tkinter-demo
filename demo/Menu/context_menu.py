#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 弹出菜单, 利用鼠标右击事件触发

from tkinter import Frame, Menu, Tk, Toplevel

window = Tk()
window.title("右键弹出菜单")


def callback():
    print("回调")


# 创建窗口
def createWindow():
    w = Toplevel()
    w.title("新建窗口")
    # 绑定右键事件，在窗口的任意位置都可以右键弹出菜单
    w.bind("<ButtonPress-2>", popup)


menuBar = Menu(window)  # 菜单栏

text_menu = Menu(menuBar)  # 创建菜单，作为下拉菜单列表
menuBar.add_cascade(label="文本", menu=text_menu, command=callback)  # 作为下拉菜单的标题

# 二级菜单
text_menu.add_command(label="复制", command=callback)
text_menu.add_command(label="粘贴", command=callback)
text_menu.add_command(label="撤销", command=callback)
text_menu.add_separator()
text_menu.add_command(label="重置", command=callback)
text_menu.add_command(label="新建窗口", command=createWindow)

# 一级菜单，直接放在菜单栏上，窗口菜单栏上不会生效
menuBar.add_separator()
menuBar.add_command(label="重置2", command=callback)  # 窗口菜单栏不现实
menuBar.add_command(label="新建窗口2", command=createWindow)  # 窗口菜单栏不现实

# 没有置顶menu参数的情况下，在顶部菜单栏是无效的
menuBar.add_cascade(label="顶部菜单栏是无效的")

# 禁用某个菜单
menuBar.entryconfigure(2, state='disabled')

frame = Frame(window, width=512, height=512)
frame.pack()


def popup(event):
    # print(event.x_root + 10, event.y_root + 10)
    menuBar.post(event.x_root + 1, event.y_root)


# frame绑定事件popup
frame.bind("<Button-2>", popup)
# or
# frame.bind("<ButtonPress-2>", popup)

# window绑定事件popup，此时的
# window.bind("<ButtonPress-2>", popup)

window.mainloop()
