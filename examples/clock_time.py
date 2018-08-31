#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 实时时钟
# 应该记住这个算法，在trickit函数中隔一秒钟调用自己一次达到时钟的效果。

import tkinter
import sys
import time

root = tkinter.Tk()
root.minsize(200, 100)
Label1 = tkinter.Label(
    text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
Label1.pack()


def trickit():
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S',
                                time.localtime(time.time()))
    Label1.config(text=currentTime)
    root.update()
    Label1.after(1000, trickit)


Label1.after(1000, trickit)

root.mainloop()
