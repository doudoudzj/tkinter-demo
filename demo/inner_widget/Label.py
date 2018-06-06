#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 控件: 标签Label
'''
用法: Label(根对象, [属性列表])
属性:
    text    要显示的文本
    bg      背景颜色
    font    字体(颜色, 大小)
    width   控件宽度
    height  控件高度
'''

from tkinter import *

mainWindow = Tk()
mainWindow.title("标签Label")
mainWindow.geometry('500x200')

# 创建标签
l = Label(
    mainWindow,
    text='标签显示的文本',
    bg='green',
    font=("Arial", 12),
    width=50,
    height=2)

# 这里的side可以赋值为LEFT, RTGHT, TOP, BOTTOM
l.pack(side=LEFT)

mainWindow.mainloop()