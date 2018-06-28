#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 弹出菜单, 利用鼠标右击事件触发

import tkinter as gui

window = gui.Tk()
window.title("右键菜单")


def callback():
    pass


# 创建窗口
def createWindow():
    w = gui.Toplevel()
    w.title("新建窗口")


menuBar = gui.Menu(window)
menuBar.add_command(label="复制", command=callback)
menuBar.add_command(label="粘贴", command=callback)
menuBar.add_command(label="撤销", command=callback)
menuBar.add_separator()
menuBar.add_command(label="重置", command=callback)
menuBar.add_command(label="新建窗口", command=createWindow)

# 禁用某个菜单
menuBar.entryconfigure(2, state='disabled')

frame = gui.Frame(window, width=512, height=512)
frame.pack()


def popup(event):
    # print(event.x_root + 10, event.y_root + 10)
    menuBar.post(event.x_root + 1, event.y_root)


# frame绑定事件popup
# frame.bind("<Button-2>", popup)
# or
frame.bind("<ButtonPress-2>", popup)

# window绑定事件popup
# window.bind("<ButtonPress-2>", popup)

window.mainloop()
