#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 菜单栏

from tkinter import Tk, Menu

root = Tk()

menubar = Menu(root)  # 菜单栏

filemenu = Menu(menubar)  # 顶级菜单节点项
radio_menus = Menu(menubar)  # 顶级菜单节点项
check_menus = Menu(menubar)  # 顶级菜单节点项
menubar.add_cascade(label="文件", menu=filemenu)  # 增加级联关系
menubar.add_cascade(label="单选", menu=radio_menus)  # 增加单选下拉菜单
menubar.add_cascade(label="复选", menu=check_menus)  # 增加复选下拉菜单

# 给菜单实例增加菜单项
for each in ['文件', '视图', '编辑', '关于']:
    filemenu.add_cascade(label=each)

menubar.add_cascade(label="保存")  # 不生效

radio_menus.add_radiobutton(label="是")
radio_menus.add_radiobutton(label="不是")
radio_menus.add_separator()
radio_menus.add_radiobutton(label="不知道")

check_menus.add_checkbutton(label="选A")
check_menus.add_checkbutton(label="选B")
check_menus.add_checkbutton(label="选C")
check_menus.add_separator()
check_menus.add_checkbutton(label="无所谓")

root.config(menu=menubar)
root.mainloop()
