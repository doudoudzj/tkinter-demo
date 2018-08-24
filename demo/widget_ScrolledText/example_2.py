#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''滚动框内容更新'''

import time
from tkinter import END, Button, Label, StringVar, Tk
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title('滚动框内容更新')

var = StringVar()
var.set('待处理')


# 滚动框输出项
def sl():
    for i in range(100):
        var.set('处理进度' + str(i))
        print('处理进度' + str(var.get()))
        time.sleep(0.1)
        text.insert(END, str(i) + '\n')  # 向文本框写入数据
        text.see(END)  # 始终显示文本框的底部
        text.update()  # 实时显示文本框内容
    var.set('处理完成')


Button(root, text='开始处理', font=('微软雅黑'), command=sl).grid(row=1, column=1)

Label(root, fg='red', textvariable=var).grid(row=2, column=1)

text = ScrolledText(root, font=('微软雅黑'))
text.grid(row=3, column=1, rowspan=4)

root.mainloop()
