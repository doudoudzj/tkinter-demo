#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''宽高自动'''

from tkinter import Tk
from tkinter.scrolledtext import ScrolledText


def example():
    root = Tk()
    root.title('输入框')
    root.geometry('500x500')
    stext = ScrolledText(
        root, bg='white', height=10, font=('Courier New', 13), fg='#333')
    stext.pack(fill='both', side='left', expand=True)
    stext.focus_set()

    stext.insert('insert', 'python')  # 插入字符
    # stext.delete(1.0, 'end) # 清空
    root.mainloop()


if __name__ == "__main__":
    example()
