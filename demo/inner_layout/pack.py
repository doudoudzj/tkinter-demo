#!/usr/bin/env python3
#-*- coding: UTF-8 -*-
# pack几何布局管理器

from tkinter import *  #导入tkinter模块的所有内容

root = Tk()
root.title("登录")  #窗口标题

f1 = Frame(root)
f1.pack()  #界面分为三个Frame
f2 = Frame(root)
f2.pack()
f3 = Frame(root)
f3.pack()
Label(f1, text="用户名").pack(side=LEFT)  #标签放置在f1中，左停靠
Entry(f1).pack(side=LEFT)  #单行文本框放置在f1中，左停靠
Label(f2, text="密  码").pack(side=LEFT)  #标签放置在f2中，左停靠
Entry(f2, show="*").pack(side=LEFT)  #单行文本框放置在f2中，左停靠
Button(f3, text="取消").pack(side=RIGHT)  #取消按钮放置在f3中，右停靠
Button(f3, text="登录").pack(side=RIGHT)  #登录按钮放置在f3中，右停靠

root.mainloop()
