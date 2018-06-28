#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Scale控件, 滑动条

import tkinter as gui

window = gui.Tk()

# 默认创建
gui.Scale(window, from_=0, to=100).pack()

# 水平方向
gui.Scale(window, from_=0, to=200, orient=gui.HORIZONTAL).pack()

var1 = gui.StringVar()
label = gui.Label(window, bg='yellow', width=30, heigh=2, text="empty")
label.pack()


def select(v):
    label.config(text='你选择的是：' + v)


# scale 尺子属性注释：
# orient ＝ gui.HORIZONTAL 水平还是竖直
# legnth 是长度
# showvalue 0:不显示，1:显示
# tickinterval 标注分成几段
# resolution 最小单位或者说保留到几位
# command 方法需要由一个参数接收选择的当前刻度
sc = gui.Scale(
    window,
    label="拉动",
    from_=0,
    to=12,
    orient=gui.HORIZONTAL,
    length=500,
    showvalue=1,
    tickinterval=3,
    resolution=0.01,
    command=select).pack()

window.mainloop()
