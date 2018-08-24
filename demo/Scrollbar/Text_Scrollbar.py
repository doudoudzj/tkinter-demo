#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""文本输入框和滚动条结合"""

from tkinter import Tk, Frame, Text, Scrollbar

root = Tk()
root.title("文本输入框和滚动条结合")

# frame容器用来包含文本输入框和滚动条
frame = Frame(root)

# 滚动条
vbar = Scrollbar(frame)

# 文本输入框
text_area = Text(frame, highlightcolor='#ddd')

# 绑定滚动
# vbar.config(command=text_area.yview)
# or
vbar['command'] = text_area.yview

text_area.config(yscrollcommand=vbar.set)

# 滚动条在frame的右边，上下填充
vbar.pack(side="right", fill="y")

# 文本输入框在左边，填充frame内剩余空间
text_area.pack(side="left", fill="both", expand=True)

# frame填充全部窗口
frame.pack(side="left", fill="both", expand=True)

root.mainloop()
