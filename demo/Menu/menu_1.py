#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 菜单栏

from tkinter import Tk, Menu

root = Tk()

def callback():
    print("点击事件")


menubar = Menu(root)  # 创建根级菜单，作为菜单栏

filemenu = Menu(menubar, tearoff=False)  # 创建菜单，作为下拉菜单列表
menubar.add_cascade(label="文件", menu=filemenu)  # 作为下拉菜单的标题
filemenu.add_command(label="打开", command=callback)  # 作为菜单项添加到下拉菜单里
filemenu.add_command(label="保存", command=callback)  # 作为菜单项添加到下拉菜单里
filemenu.add_separator()  # 在菜单里添加分割线
filemenu.add_command(label="退出", command=callback)  # 作为菜单项添加到下拉菜单里

editmenu = Menu(menubar)  # 创建菜单
menubar.add_cascade(label="编辑", menu=editmenu)  # 作为下拉菜单的标题

# 在菜单里添加命令菜单
for each in ['复制', '粘贴', '剪切']:
    editmenu.add_command(label=each)

root.config(menu=menubar)
root.mainloop()
