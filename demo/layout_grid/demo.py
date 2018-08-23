# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Grid几何布局管理器
# 跟html的表格类似

import tkinter as gui

window = gui.Tk()
window.title('Grid')
window.geometry('400x400+250+140')

gui.Label(text='Label', fg='red', bg='white').grid(row=0, column=0) # 第一行第一列
gui.Label(text='豆豆', fg='red', bg='white').grid(row=0, column=1) # 第一行第二列
gui.Label(text='你好', fg='#ff4', bg='#234').grid(row=1, column=1) # 第二行第二列
gui.Label(text='哈哈', fg='#fff', bg='#828').grid(row=1, column=2, sticky=gui.E+gui.W) # 第二行第三列, 使用sticky充满当前格子
gui.Label(text='你好', fg='#ff4', bg='#438').grid(row=1, column=3) # 第二行第四列

gui.Label(text='标签1', fg='#fff', bg='#395').grid(row=2, column=0) # 第三行第一列
gui.Label(text='标签1', fg='#fff', bg='#345').grid(row=2, column=3) # 第三行第四列

gui.Label(text='五行三列', fg='#fff', bg='#645').grid(row=4, column=2) # 第五行第三列
gui.Label(text='标签', fg='#fff', bg='#645').grid(row=4, column=3) # 第五行第四列
gui.Label(text='五行五列', fg='#fff', bg='#345').grid(row=4, column=4) # 第五行第五列

gui.Label(text='第六行第六列', fg='red', bg='blue').grid(row=5, column=5)

window.mainloop()
