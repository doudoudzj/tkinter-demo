#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' 控件: 标签Entry
说明: 创建单行文本框
用法:
    创建: lb =Entry(根对象, [属性列表])
    绑定变量: var=StringVar() lb=Entry(根对象, textvariable = var)
    获取文本框中的值: var.get()
    设置文本框中的值: var.set(item1)
'''

from tkinter import *

root = Tk()
root.title("标签Entry")

# 定义变量inputValue
inputValue = StringVar()
inputValue.set("你好")
inputText = Entry(root, textvariable=inputValue)


inputText.pack()

root.mainloop()