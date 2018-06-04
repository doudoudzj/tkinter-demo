#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
''' 控件: 标签Text
说明: 向该空间内输入文本
用法:
    t = Text(根对象)
        插入: t.insert(mark, 内容)
        删除: t.delete(mark1, mark2)
        其中, mark可以是行号, 或者特殊标识, 例如
    INSERT: 光标的插入点CURRENT:鼠标的当前位置所对应的字符位置
    END: 这个Textbuffer的最后一个字符
    SEL_FIRST: 选中文本域的第一个字符, 如果没有选中区域则会引发异常
    SEL_LAST: 选中文本域的最后一个字符, 如果没有选中区域则会引发异常
'''

from tkinter import *

root = Tk()
root.title("标签Text")
root.geometry('300x200')

t = Text(root)
t.insert(1.0, 'hello\n')
t.insert(END, 'hello000000\n')
t.insert(END, 'nono')
t.pack()

root.mainloop()