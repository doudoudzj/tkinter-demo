#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''不同参数'''

from tkinter import Tk, TOP, END, Label, StringVar
from tkinter.ttk import Button
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('各种参数的演示')

txt = ScrolledText(
    root,  # 父容器
    width=10,  # 宽度10个字符
    height=3,  # 高度3个字符
    borderwidth=5,  # 边框
    wrap='word',  # 以单个词汇为整体来换行
    background='#e8eaf6',  # 背景色
    highlightcolor='red',  # 激活边框颜色
    font=('Courier New', 15),  # 字体
    foreground='red'  # 字体颜色
)

txt.pack(fill='both', side='left', expand=True)


def print_text():
    '''输入文本框内容'''
    print(txt.get(0.0, END))


Button(root, text='打印出当前内容', command=print_text).pack(fill='both', side='top')

root.mainloop()
