#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
# grid几何布局管理器

from tkinter import *

root = Tk()

Button(root, text="1").grid(row=0, column=0)  #按钮1放置于0行0列
Button(root, text="2").grid(row=0, column=1)  #按钮1放置于0行1列
Button(root, text="3").grid(row=0, column=2)  #按钮1放置于0行2列
Button(root, text="4").grid(row=1, column=0)
Button(root, text="5").grid(row=1, column=1)
Button(root, text="6").grid(row=1, column=2)
Button(root, text="7").grid(row=2, column=0)
Button(root, text="8").grid(row=2, column=1)
Button(root, text="9").grid(row=2, column=2)
Button(
    root, text="0").grid(
        row=3, column=0, columnspan=2, sticky=E + W)  #跨两列，左右紧贴
Button(root, text=".").grid(row=3, column=2, sticky=E + W)  #左右紧贴

root.mainloop()  #事件循环
