#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' 控件: 标签Frame
说明: 在屏幕上创建一块矩形区域,多作为容器来布局窗体
用法: Frame(根对象, [属性列表])
属性:
'''

from tkinter import *

root = Tk()
root.title("标签Frame")
root.geometry('200x100')

Label(root, text='少说多做', font=('Arial', 20)).pack()

# 创建Frame示例: 外层框框
frm = Frame(root)

# 创建Frame示例: frm内的左侧框框
frm_L = Frame(frm)
Label(frm_L, text='好好', font=('Arial', 15)).pack(side=TOP)
Label(frm_L, text='学习', font=('Arial', 15)).pack(side=TOP)
frm_L.pack(side=LEFT)

# 创建Frame示例: frm内的右侧框框
frm_R = Frame(frm)
Label(frm_R, text='天天', font=('Arial', 15)).pack(side=TOP)
Label(frm_R, text='向上', font=('Arial', 15)).pack(side=TOP)
frm_R.pack(side=RIGHT)

frm.pack()

root.mainloop()