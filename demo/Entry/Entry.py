#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''单行文本输入框'''

from tkinter import Tk, Entry, StringVar

root = Tk()
root.title("标签Entry")

# 定义变量inputValue
inputValue = StringVar(value="默认值")


# 修改变量的值, 值会同步到输入框内
def callback(event):
    inputValue.set("输入框点击之后的内容")


inputText = Entry(root, textvariable=inputValue)
inputText.bind("<Button-1>", callback)

inputText.pack()

root.mainloop()
