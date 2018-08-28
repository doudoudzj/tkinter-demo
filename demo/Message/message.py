#!/usr/bin/env python3
#-*- coding: UTF-8 -*-

from tkinter import Tk, Label, Message

root = Tk()
root.title("多行文本")
root.geometry("300x300")

Label(root, text="单行文本").pack()
Label(root, text="单行文本单行文本单行文本单行文本单行文本").pack()

Message(root, text="这是可以换行的文本", width="20").pack()
Message(root, text="这是可以换行的文本这是可以换行的文本").pack(fill="both", expand=True)

root.mainloop()
