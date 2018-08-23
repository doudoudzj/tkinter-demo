#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 导入滚动文本框的模块

from tkinter import Tk
from tkinter.scrolledtext import ScrolledText

# or from tkinter import scrolledtext
# use scrolledtext.ScrolledText


def app():
    root = Tk()
    root.title("滚动文本框")
    textarea = ScrolledText(root, width=30, height=3, wrap='word')
    textarea.grid(column=0, columnspan=3)
    root.mainloop()


if __name__ == '__main__':
    app()
