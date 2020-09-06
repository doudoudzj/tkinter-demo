#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# LabelFrame
# labelframe是一个简单的容器构件。其主要目的是作为一个间隔或复杂的窗口布局容器.
# 如同本例中lab_1使用grid布局，而button部分不使用grid布局
# 使用LabelFrame作为子容器，使用grid布局，内部的button则使用pack直接居左排列，

import tkinter
from tkinter import ttk

win = tkinter.Tk()

lab_1 = tkinter.Label(win, text="LabelFrame示例").grid(
    row=0, column=1, sticky="nswe")

head_frame = tkinter.LabelFrame(win, text="操作")
head_frame.grid(row=1)

tkinter.Label(head_frame, text="标签").pack()
tkinter.Label(head_frame, text="哈哈").pack()

btn_info = tkinter.Button(head_frame, text="详情", command=lambda: print("详情"))
btn_edit = tkinter.Button(head_frame, text="编辑", command=lambda: print("编辑"))
btn_delete = tkinter.Button(head_frame, text="删除", command=lambda: print("删除"))
btn_info.pack(side="left")
btn_edit.pack(side="left")
btn_delete.pack(side="left")

win.mainloop()
